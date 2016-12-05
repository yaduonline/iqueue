import logging

from django.conf import settings
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext

from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets

from .models import Queue, Slot, QueueMember
from .forms import UserForm, QueueMemberForm
from .serializers import UserSerializer, QueueSerializer, SlotSerializer, QueueMemberSerializer

logger = logging.getLogger(settings.DEFAULT_LOGGER)

def index(request):
    return HttpResponse("Hello queue!")


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QueueViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

    @detail_route(methods=['post'])
    def enqueue(self, request, pk=None):
        queue = Queue.objects.get(pk=pk)
        user_id = request.data.get('user_id')
        if not user_id:
            user = request.user
            logger.info('User id not specified. Using authenticated user. %s', user)
        else:
            user = User.objects.get(id=user_id)
        queue_member = QueueMember.objects.get(user=user)
        slot = queue.enqueue(queue_member)
        serialized_slot = SlotSerializer(slot, context={'request': request})
        return Response(serialized_slot.data)

    @detail_route(methods=['post'])
    def dequeue(self, request, pk=None):
        queue = Queue.objects.get(pk=pk)
        owner = queue.owner.user
        if request.user != owner or request.user != queue.top().user:
            logger.warn('User not authorized for dequeue. Request user: %s', request.user)
            return Response(status=403)
        slot = queue.dequeue()
        serialized_slot = SlotSerializer(slot, context={'request': request})
        return Response(serialized_slot.data)


class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class QueueMemberViewSet(viewsets.ModelViewSet):
    queryset = QueueMember.objects.all()
    serializer_class = QueueMemberSerializer

    @list_route(methods=['post', 'get'])
    def register(self, request):
        if request.method == 'POST':
            user_form = UserForm(request.POST, prefix='user')
            queue_member_form = QueueMemberForm(request.POST, prefix='queuemember')
            if not user_form.is_valid():
                return ('User form is invalid', )
            if user_form.is_valid() * queue_member_form.is_valid():
                user = user_form.save()
                queue_member = queue_member_form.save(commit=False)
                queue_member.user = user
                queue_member.save()
                serializer = QueueMemberSerializer(queue_member, context={'request':request})
                return Response(serializer.data)
            else:
                return Response('Form is invalid', status=400)
        else:
            user_form = UserForm(prefix='user')
            queue_member_form = QueueMemberForm(prefix='queuemember')
            return  render_to_response('queue/register.html', dict(userform=user_form, queuememberform=queue_member_form),
                                       context_instance=RequestContext(request))

    @detail_route(methods=['get'])
    def owned_queues(self, request, pk=None):
        queue_member = QueueMember.objects.get(pk=pk)
        owned_queues = Queue.objects.filter(owner=queue_member)
        serializer = QueueSerializer(owned_queues, many=True, context={'request': request})
        return Response(serializer.data)

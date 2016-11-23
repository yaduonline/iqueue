from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from .models import Queue, Slot
from django.contrib.auth.models import User
from .serializers import UserSerializer, QueueSerializer, SlotSerializer
from django.http import HttpResponse


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
        user = User.objects.get(id=user_id)
        slot = queue.enqueue(user)
        serialized_slot = SlotSerializer(slot, context={'request': request})
        return Response(serialized_slot.data)

    @detail_route(methods=['post'])
    def dequeue(self, request, pk=None):
        queue = Queue.objects.get(pk=pk)
        slot = queue.dequeue()
        serialized_slot = SlotSerializer(slot, context={'request': request})
        return Response(serialized_slot.data)


class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

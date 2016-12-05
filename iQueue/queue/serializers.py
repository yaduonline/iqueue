from django.contrib.auth.models import User
from .models import Queue, Slot, QueueMember
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'first_name', 'last_name')


class QueueMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = QueueMember
        fields = ('id', 'user', 'phone_number')


class SlotSerializer(serializers.ModelSerializer):
    user = QueueMemberSerializer()

    class Meta:
        model = Slot
        fields = ('id', 'time_added', 'user', 'queue')


class QueueSerializer(serializers.ModelSerializer):
    slot_set = SlotSerializer(many=True, read_only=True)
    class Meta:
        model = Queue
        fields = ('id', 'name', 'creation_date', 'owner', 'slot_set')



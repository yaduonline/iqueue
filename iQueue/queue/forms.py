from django.forms import  ModelForm, PasswordInput, CharField
from django.contrib.auth.models import User
from .models import QueueMember, Queue


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class QueueMemberForm(ModelForm):
    class Meta:
        model = QueueMember
        exclude = ['user', 'is_phone_verified']


class QueueForm(ModelForm):
    class Meta:
        model = Queue
        exclude = ['creation_date', 'owner']
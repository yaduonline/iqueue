from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class QueueMember(models.Model):
    user = models.OneToOneField(User)
    phone_number = PhoneNumberField()
    is_phone_verified = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.user)



class QueueManager(models.Model):
    def create_queue(self, owner):
        queue = self.create(owner=owner)
        return queue


class Queue(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    owner = models.ForeignKey(QueueMember, on_delete=models.CASCADE)

    objects = QueueManager()

    def enqueue(self, user):
        s = Slot(user=user, queue=self)
        s.save()
        self.slot_set.add(s)
        return s

    def dequeue(self):
        s = self.slot_set.first()
        self.slot_set.remove(s)
        return s

    def __unicode__(self):
        return self.name


class Slot(models.Model):
    user = models.ForeignKey(QueueMember)
    time_added = models.DateTimeField(auto_now_add=True)
    appt_time = models.DateTimeField(auto_now_add=True)
    queue = models.ForeignKey(Queue, blank=True, null=True)

    class Meta:
        ordering = ['time_added']

    def __unicode__(self):
        return str(self.user)

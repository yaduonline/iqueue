from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class QueueManager(models.Model):
    def create_queue(self, owner):
        queue = self.create(owner=owner)
        return queue


class Queue(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

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
    user = models.ForeignKey(User)
    time_added = models.DateTimeField(auto_now_add=True)
    queue = models.ForeignKey(Queue, blank=True, null=True)

    class Meta:
        ordering = ['time_added']

    def __unicode__(self):
        return str(self.user)

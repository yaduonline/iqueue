from django.contrib import admin
from .models import Queue, Slot


class SlotsInline(admin.TabularInline):
    model = Slot
    fields = ('user', 'time_added',)
    readonly_fields = ('time_added',)


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'creation_date')
    inlines = (SlotsInline,)
    date_hierarchy = 'creation_date'


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_added')

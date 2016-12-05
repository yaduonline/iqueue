from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Queue, Slot, QueueMember


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
    list_display = ('user', 'time_added', 'appt_time')


class QueueMemberInline(admin.StackedInline):
    model = QueueMember
    can_delete = False
    verbose_name_plural = 'queuemember'


class UserAdmin(BaseUserAdmin):
    inlines = (QueueMemberInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

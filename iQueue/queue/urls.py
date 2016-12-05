from django.conf.urls import url, include
from queue.views import UserViewSet, QueueViewSet, SlotViewSet, QueueMemberViewSet
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'queues', QueueViewSet)
router.register(r'slots', SlotViewSet)
router.register(r'queuemembers', QueueMemberViewSet)

schema_view = get_swagger_view(title='Queue API')
urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-docs/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

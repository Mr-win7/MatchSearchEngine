from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from apiv1.views import *

routers = DefaultRouter()
routers.register(r'document/search', DocumentViewSet， base_name='document_search')

urlpatterns = [
    url(r'^', include(routers.urls)),
]

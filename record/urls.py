from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from record import views

router = DefaultRouter()

router.register(r'record', views.RecordViewset, basename='record')

urlpatterns = [
    re_path('^', include(router.urls))
]
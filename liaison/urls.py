from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from liaison import views

router = DefaultRouter()

router.register(r'liaison', views.LiaisonViewset, basename='liaison')

urlpatterns = [
    re_path('^', include(router.urls))
]
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from customer import views

router = DefaultRouter()

router.register(r'customer', views.CustomerViewset, basename='customer')

urlpatterns = [
    re_path('^', include(router.urls))
]
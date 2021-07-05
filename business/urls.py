from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from business import views

router = DefaultRouter()

router.register(r'business', views.BusinessViewset, basename='business')
router.register(r'all/business', views.AllBusinessViewset, basename='all_business')

urlpatterns = [
    re_path('^', include(router.urls))
]
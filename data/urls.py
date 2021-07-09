from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from data import views

router = DefaultRouter()

router.register(r'data', views.DataViewset, basename='data')
router.register(r'data/customer', views.DataCustomerViewset, basename='data_customer')
router.register(r'data/liaison', views.DataLiaisonViewset, basename='data_liaison')
router.register(r'data/record', views.DataRecordViewset, basename='data_record')
router.register(r'data/business', views.DataBusinessViewset, basename='data_business')

urlpatterns = [
    re_path('^', include(router.urls))
]

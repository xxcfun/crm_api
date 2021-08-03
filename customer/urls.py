from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from customer import views

router = DefaultRouter()

router.register(r'customer', views.CustomerViewset, basename='customer')
router.register(r'linkcustomer', views.LinkCustomerViewset, basename='linkcustomer')
router.register(r'linkallcustomer', views.LinkAllCustomerViewset, basename='linkallcustomer')
router.register(r'all/customer', views.AllCustomerViewset, basename='all_customer')

urlpatterns = [
    re_path('^', include(router.urls))
]
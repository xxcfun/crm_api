from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from customer import views

router = DefaultRouter()

router.register(r'customer', views.CustomerViewset, basename='customer')
router.register(r'linkcustomer', views.LinkCustomerViewset, basename='linkcustomer')

urlpatterns = [
    re_path('^', include(router.urls))
]
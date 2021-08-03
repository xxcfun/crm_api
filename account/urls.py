from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from account import views

router = DefaultRouter()
router.register(r'users', views.UserViewset, basename='users')
router.register(r'jsusers', views.JSUserViewset, basename='jsusers')

urlpatterns = [
    # JWT的认证接口
    path('login/', obtain_jwt_token),
    re_path('^', include(router.urls))
]

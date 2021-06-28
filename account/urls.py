from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from account import views


urlpatterns = [
    # JWT的认证接口
    path('login/', obtain_jwt_token)
]

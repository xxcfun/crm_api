from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import mixins, viewsets, authentication, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from account.serializers import UserDetailSerializer
from utils.permissions import IsOwnerOrReadOnly

User = get_user_model()


class CustomBackend(ModelBackend):
    """ 自定义用户验证 """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username) | Q(name=username)
            )
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

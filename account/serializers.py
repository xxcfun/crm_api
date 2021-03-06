from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """ 用户详情 """

    def update(self, instance, validated_data):
        # TODO 修改密码
        pass

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'role')


class JSUserSerializer(serializers.ModelSerializer):
    """ 技术角色用户列表 """

    class Meta:
        model = User
        fields = ('username', 'name', 'role')

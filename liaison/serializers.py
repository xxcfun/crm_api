from rest_framework import serializers

from account.serializers import UserDetailSerializer
from customer.serializers import LinkCustomerSerializer
from liaison.models import Liaison


class LiaisonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    job = serializers.CharField(source='get_job_display', required=True)
    injob = serializers.CharField(source='get_injob_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Liaison
        fields = ('id', 'name', 'customer', 'phone', 'job', 'injob', 'created_at', 'user')


class LiaisonDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Liaison
        fields = '__all__'


class LiaisonCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Liaison
        fields = '__all__'


class AllLiaisonSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    job = serializers.CharField(source='get_job_display', required=True)
    injob = serializers.CharField(source='get_injob_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)
    user = UserDetailSerializer()

    class Meta:
        model = Liaison
        fields = ('id', 'name', 'customer', 'phone', 'job', 'injob', 'created_at', 'user')

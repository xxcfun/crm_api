from rest_framework import serializers

from account.serializers import UserDetailSerializer
from customer.serializers import LinkCustomerSerializer
from business.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    winning_rate = serializers.CharField(source='get_winning_rate_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Business
        fields = ('id', 'name', 'customer', 'winning_rate', 'money', 'created_at', 'user')


class BusinessDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Business
        fields = '__all__'


class BusinessCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Business
        fields = '__all__'


class AllBusinessSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    winning_rate = serializers.CharField(source='get_winning_rate_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)
    user = UserDetailSerializer()

    class Meta:
        model = Business
        fields = ('id', 'name', 'customer', 'winning_rate', 'money', 'created_at', 'user')

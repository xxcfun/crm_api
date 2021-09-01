from rest_framework import serializers

from account.serializers import UserDetailSerializer
from customer.serializers import LinkCustomerSerializer
from record.models import Record


class RecordSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    status = serializers.CharField(source='get_status_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Record
        fields = ('id', 'theme', 'customer', 'status', 'main', 'product', 'next', 'created_at', 'user')


class RecordDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Record
        fields = '__all__'


class RecordCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Record
        fields = '__all__'


class AllRecordSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    status = serializers.CharField(source='get_status_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)
    user = UserDetailSerializer()

    class Meta:
        model = Record
        fields = ('id', 'theme', 'customer', 'status', 'main', 'product', 'next', 'created_at', 'user')

from rest_framework import serializers

from account.serializers import UserDetailSerializer
from backend.models import PreSupport, Implement, AfterSupport, Service, ServiceProcess
from customer.serializers import LinkAllCustomerSerializer


class PreSupportSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)
    user = UserDetailSerializer()

    class Meta:
        model = PreSupport
        fields = ('id', 'preplan', 'customer', 'product', 'cycle', 'date', 'des', 'user', 'created_at')


class PreSupportDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)

    class Meta:
        model = PreSupport
        fields = '__all__'


class PreSupportCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = PreSupport
        fields = '__all__'


class ImplementSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)

    class Meta:
        model = Implement
        fields = ('id', 'testplan', 'customer', 'report', 'date', 'user', 'created_at')


class ImplementDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)

    class Meta:
        model = Implement
        fields = '__all__'


class ImplementCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Implement
        fields = '__all__'


class AfterSupportSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)
    status = serializers.CharField(source='get_status_display', required=True)

    class Meta:
        model = AfterSupport
        fields = ('id', 'aftersupport', 'customer', 'status', 'des', 'date', 'user', 'created_at')


class AfterSupportDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)

    class Meta:
        model = AfterSupport
        fields = '__all__'


class AfterSupportCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = AfterSupport
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)

    class Meta:
        model = Service
        fields = ('id', 'problem', 'customer', 'other', 'result', 'user', 'created_at')


class ServiceDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = LinkAllCustomerSerializer(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class ServiceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Service
        fields = '__all__'


class ServiceProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceProcess
        fields = '__all__'

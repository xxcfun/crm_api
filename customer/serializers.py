from rest_framework import serializers

from account.serializers import UserDetailSerializer
from backend.models import PreSupport, Service, AfterSupport, Implement
from business.models import Business
from customer.models import Customer
from liaison.models import Liaison
from record.models import Record


class LiaisonSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    job = serializers.CharField(source='get_job_display', required=True)
    injob = serializers.CharField(source='get_injob_display', required=True)

    class Meta:
        model = Liaison
        fields = ('id', 'name', 'phone', 'job', 'injob', 'created_at', 'user')


class RecordSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    status = serializers.CharField(source='get_status_display', required=True)

    class Meta:
        model = Record
        fields = ('id', 'theme', 'status', 'main', 'product', 'next', 'created_at', 'user')


class BusinessSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    winning_rate = serializers.CharField(source='get_winning_rate_display', required=True)

    class Meta:
        model = Business
        fields = ('id', 'name', 'winning_rate', 'money', 'created_at', 'user')


class PreSupportSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = PreSupport
        fields = ('id', 'preplan', 'product', 'cycle', 'des', 'date', 'user')


class ImplementSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Implement
        fields = ('id', 'impplan', 'product', 'report', 'date', 'user')


class AfterSupportSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    status = serializers.CharField(source='get_status_display', required=True)

    class Meta:
        model = AfterSupport
        fields = ('id', 'aftersupport', 'status', 'des', 'date', 'user')


class ServiceSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d')

    class Meta:
        model = Service
        fields = ('id', 'problem', 'other', 'result', 'user', 'created_at')


class CustomerSerializer(serializers.ModelSerializer):
    """ 客户列表信息 """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    rank = serializers.CharField(source='get_rank_display', required=False)
    is_deal = serializers.CharField(source='get_is_deal_display', required=False)
    scale = serializers.CharField(source='get_scale_display', required=False)
    industry = serializers.CharField(source='get_industry_display', required=False)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'rank', 'is_deal', 'scale', 'industry', 'created_at', 'user')


class CustomerDetailSerializer(serializers.ModelSerializer):
    """ 客户详情信息 """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    liaison = LiaisonSerializer(many=True, read_only=True)
    record = RecordSerializer(many=True, read_only=True)
    business = BusinessSerializer(many=True, read_only=True)
    presupport = PreSupportSerializer(many=True, read_only=True)
    implement = ImplementSerializer(many=True, read_only=True)
    aftersupport = AfterSupportSerializer(many=True, read_only=True)
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class LinkCustomerSerializer(serializers.ModelSerializer):
    """后端使用 联系人 拜访记录 商机 外键依赖 """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Customer
        fields = ('id', 'name', 'user')


class LinkAllCustomerSerializer(serializers.ModelSerializer):
    """ 后端使用 售前 实施 售后 维修 外键依赖 """

    class Meta:
        model = Customer
        fields = ('id', 'name')


class LinkCustomerListSerializer(serializers.ModelSerializer):
    """ 前端使用，个人添加，返回个人的所有客户 """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    value = serializers.CharField(source='name')

    class Meta:
        model = Customer
        fields = ('id', 'value', 'user')


class LinkAllCustomerListSerializer(serializers.ModelSerializer):
    """ 前端使用，售后售前模块 返回所有的客户 """
    value = serializers.CharField(source='name')

    class Meta:
        model = Customer
        fields = ('id', 'value')


class AllCustomerSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    rank = serializers.CharField(source='get_rank_display', required=False)
    is_deal = serializers.CharField(source='get_is_deal_display', required=False)
    scale = serializers.CharField(source='get_scale_display', required=False)
    industry = serializers.CharField(source='get_industry_display', required=False)
    user = UserDetailSerializer()
    liaison = LiaisonSerializer(many=True, read_only=True)
    record = RecordSerializer(many=True, read_only=True)
    business = BusinessSerializer(many=True, read_only=True)
    presupport = PreSupportSerializer(many=True, read_only=True)
    implement = ImplementSerializer(many=True, read_only=True)
    aftersupport = AfterSupportSerializer(many=True, read_only=True)
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'rank', 'is_deal', 'scale', 'industry', 'created_at', 'user',
                  'liaison', 'record', 'business', 'presupport', 'implement', 'aftersupport', 'service')


class CustomerCreateSerializer(serializers.ModelSerializer):
    """ 后端人员创建客户序列化 """

    class Meta:
        model = Customer
        fields = '__all__'

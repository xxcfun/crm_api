from rest_framework import serializers

from account.serializers import UserDetailSerializer
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
        fields = ('id', 'theme', 'status', 'main', 'next', 'created_at', 'user')


class BusinessSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    winning_rate = serializers.CharField(source='get_winning_rate_display', required=True)

    class Meta:
        model = Business
        fields = ('id', 'name', 'winning_rate', 'money', 'created_at', 'user')


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

    class Meta:
        model = Customer
        fields = '__all__'


class LinkCustomerSerializer(serializers.ModelSerializer):
    """ 联系人 拜访记录 商机 外键依赖 """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Customer
        fields = ('id', 'name', 'user')


class LinkCustomerListSerializer(serializers.ModelSerializer):
    """ 关联客户，前端使用 """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    value = serializers.CharField(source='name')

    class Meta:
        model = Customer
        fields = ('id', 'value', 'user')


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

    class Meta:
        model = Customer
        fields = ('id', 'name', 'rank', 'is_deal', 'scale', 'industry', 'created_at', 'user', 'liaison', 'record', 'business')

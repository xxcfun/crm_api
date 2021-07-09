from rest_framework import serializers

from account.serializers import UserDetailSerializer
from business.models import Business
from customer.models import Customer
from customer.serializers import LinkCustomerSerializer
from data.models import Data
from liaison.models import Liaison
from record.models import Record


class DataSerializer(serializers.ModelSerializer):
    """ 数据汇总 """
    user = UserDetailSerializer()

    class Meta:
        model = Data
        fields = '__all__'


class DataCustomerSerializer(serializers.ModelSerializer):
    """ 一周用户 """
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    rank = serializers.CharField(source='get_rank_display', required=False)
    is_deal = serializers.CharField(source='get_is_deal_display', required=False)
    scale = serializers.CharField(source='get_scale_display', required=False)
    industry = serializers.CharField(source='get_industry_display', required=False)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'rank', 'is_deal', 'scale', 'industry', 'created_at', 'user')


class DataLiaisonSerializer(serializers.ModelSerializer):
    """ 一周联系人 """
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    job = serializers.CharField(source='get_job_display', required=True)
    injob = serializers.CharField(source='get_injob_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Liaison
        fields = ('id', 'name', 'customer', 'phone', 'job', 'injob', 'created_at', 'user')


class DataRecordSerializer(serializers.ModelSerializer):
    """ 一周拜访记录 """
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    status = serializers.CharField(source='get_status_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Record
        fields = ('id', 'theme', 'customer', 'status', 'main', 'next', 'created_at', 'user')


class DataBusinessSerializer(serializers.ModelSerializer):
    """ 一周商机 """
    user = UserDetailSerializer()
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    winning_rate = serializers.CharField(source='get_winning_rate_display', required=True)
    customer = LinkCustomerSerializer(read_only=True)

    class Meta:
        model = Business
        fields = ('id', 'name', 'customer', 'winning_rate', 'money', 'created_at', 'user')

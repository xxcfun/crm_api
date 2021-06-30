from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
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
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

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
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    value = serializers.CharField(source='name')

    class Meta:
        model = Customer
        fields = ('id', 'value', 'user')

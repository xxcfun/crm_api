from rest_framework import serializers

from customer.serializers import CustomerSerializer
from business.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = CustomerSerializer(many=False, read_only=False)

    class Meta:
        model = Business
        fields = '__all__'

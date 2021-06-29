from rest_framework import serializers

from customer.serializers import CustomerSerializer
from liaison.models import Liaison


class LiaisonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = CustomerSerializer(many=False, read_only=False)

    class Meta:
        model = Liaison
        fields = '__all__'

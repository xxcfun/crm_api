from rest_framework import serializers

from customer.serializers import CustomerSerializer
from record.models import Record


class RecordSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    updated_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    customer = CustomerSerializer(many=False, read_only=False)

    class Meta:
        model = Record
        fields = '__all__'

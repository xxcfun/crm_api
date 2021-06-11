from django.forms import ModelForm

from customer.models import Customer


class CustomerForm(ModelForm):
    """客户表单"""
    class Meta:
        model = Customer
        fields = ('name', 'rank', 'is_deal', 'website', 'scale', 'nature', 'industry', 'remarks', 'user')
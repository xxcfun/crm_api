from django import forms

from customer.models import Customer


class CustomerForm(forms.Form):
    """客户表单"""
    name = forms.CharField(label='客户名称', max_length=64, required=True, error_messages={
        'required': '请输入客户名称'
    })
    rank = forms.IntegerField(label='客户级别', required=True, error_messages={
        'required': '请选择客户级别'
    })
    is_deal = forms.BooleanField(label='是否成交', required=True, error_messages={
        'required': '请选择是否为成交客户'
    })
    # website = forms.CharField(label='网址', max_length=255)
    scale = forms.IntegerField(label='客户规模', required=True, error_messages={
        'required': '请选择客户规模'
    })
    nature = forms.IntegerField(label='客户性质', required=True, error_messages={
        'required': '请选择客户性质'
    })
    industry = forms.IntegerField(label='客户行业', required=True, error_messages={
        'required': '请选择客户行业'
    })
    # remarks = forms.CharField(label='客户名称', max_length=512)
    user = forms.CharField(label='创建人', max_length=16, required=True, error_messages={
        'required': '请填写创建人信息'
    })

    def clean_name(self):
        name = self.cleaned_data['name']
        if Customer.objects.filter(name=name).exists():
            raise forms.ValidationError('该客户已存在')
        return name

    def do_add(self, request):
        """ 执行添加 """
        data = self.cleaned_data
        user_id = request.user
        print(user_id)
        try:
            # 创建客户信息表
            customer = Customer.objects.create(
                name=data.get('name', None),
                rank=data.get('rank', None),
                is_deal=data.get('is_deal', None),
                website=data.get('website', None),
                scale=data.get('scale', None),
                nature=data.get('nature', None),
                industry=data.get('industry', None),
                remarks=data.get('remarks', None),
                user=user_id
            )
            return customer
        except Exception as e:
            print(e)
            return None

from django import forms
from django.contrib.auth import authenticate, login
from django.utils.timezone import now


class LoginForm(forms.Form):
    """ 登录表单 """
    username = forms.CharField(label='用户名', max_length=100, required=False, initial='admin')
    password = forms.CharField(label='密码', max_length=200, min_length=6, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = None

    def clean(self):
        data = super(LoginForm, self).clean()
        print(data)

        if self.errors:
            return
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或者是密码不正确')
        else:
            if not user.is_active:
                raise forms.ValidationError('该用户已被禁用')
        self.user = user
        return data

    def do_login(self, request):
        # 执行用户登录
        user = self.user
        login(request, user)
        user.last_login = now()
        user.save()
        return user

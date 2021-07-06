from django.contrib.auth.models import AbstractUser
from django.db import models

from account.choices import Role


class UserProfile(AbstractUser):
    """ 用户信息 """
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    name = models.CharField('姓名', max_length=30, null=True, blank=True)
    mobile = models.CharField('电话', max_length=11)
    gender = models.CharField('性别', max_length=6, choices=GENDER_CHOICES, default='male')
    email = models.EmailField('邮箱', max_length=100, null=True, blank=True)
    role = models.SmallIntegerField('角色', choices=Role.choices, default=None, null=True, blank=True)
    sub_user = models.ForeignKey('self', verbose_name='上级领导', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

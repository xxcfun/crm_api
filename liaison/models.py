from django.contrib.auth import get_user_model
from django.db import models

from customer.models import Customer
from liaison.choices import Job, Injob
from utils.models import CommonModel

User = get_user_model()


class Liaison(CommonModel):
    """联系人模型"""
    customer = models.ForeignKey(Customer, verbose_name='客户', related_name='liaison', on_delete=models.CASCADE)
    name = models.CharField('联系人姓名', max_length=64)
    phone = models.CharField('联系人电话', max_length=11)
    job = models.SmallIntegerField('职称', choices=Job.choices, default=Job.JOB_BUSINESS)
    injob = models.SmallIntegerField('是否在职', choices=Injob.choices, default=Injob.INJOB_YES)
    wx = models.CharField('微信', max_length=64, blank=True, null=True)
    qq = models.CharField('QQ', max_length=64, blank=True, null=True)
    email = models.EmailField('电子邮箱', max_length=64, blank=True, null=True)
    hobby = models.CharField('兴趣爱好', max_length=128, blank=True, null=True)
    birthday = models.CharField('生日', max_length=64, blank=True, null=True)
    remarks = models.TextField('联系人备注', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='创建人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'liaison'
        verbose_name = verbose_name_plural = "联系人"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

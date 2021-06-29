from django.contrib.auth import get_user_model
from django.db import models

from business.choices import WinRate
from customer.models import Customer
from utils.models import CommonModel

User = get_user_model()


class Business(CommonModel):
    """客户商机"""
    name = models.CharField('商机名称', max_length=64)
    customer = models.ForeignKey(Customer, verbose_name='商机客户', related_name='business', on_delete=models.CASCADE)
    winning_rate = models.SmallIntegerField('赢单率', choices=WinRate.choices, default=WinRate.WINNING_NONE)
    money = models.CharField('预估金额', max_length=16, blank=True, null=True)
    remarks = models.TextField('商机备注', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='创建人', related_name='business', on_delete=models.CASCADE)

    class Meta:
        db_table = 'business'
        verbose_name = verbose_name_plural = "客户商机"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

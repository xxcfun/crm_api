from django.contrib.auth import get_user_model
from django.db import models

from customer.models import Customer
from record.choices import STATUS
from utils.models import CommonModel

User = get_user_model()


class Record(CommonModel):
    """客户拜访记录模型"""
    theme = models.CharField('拜访主题', max_length=256)
    customer = models.ForeignKey(Customer, verbose_name='客户', related_name='record', on_delete=models.CASCADE)
    status = models.SmallIntegerField('客户拜访方式', choices=STATUS.choices, default=STATUS.STATUS_XS)
    main = models.TextField('主要事宜', max_length=1000, null=True, blank=True)
    next = models.TextField('后期规划', max_length=1000, null=True, blank=True)
    remarks = models.TextField('拜访备注', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='创建人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'record'
        verbose_name = verbose_name_plural = "客户拜访记录"
        ordering = ['-created_at']

    def __str__(self):
        return self.theme

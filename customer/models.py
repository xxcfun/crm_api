from django.contrib.auth import get_user_model
from django.db import models

from customer.choices import Rank, Scale, Nature, Industry, Deal
from utils.models import CommonModel

User = get_user_model()


class Customer(CommonModel):
    """ 客户信息 """
    name = models.CharField('客户名称', max_length=64, unique=True)
    rank = models.SmallIntegerField('客户级别', choices=Rank.choices, default=Rank.RANK_POTENTIAL)
    is_deal = models.SmallIntegerField('是否成交', choices=Deal.choices, default=Deal.DEAL_NO)
    website = models.CharField('客户网址', max_length=255, blank=True, null=True)
    scale = models.SmallIntegerField('客户规模', choices=Scale.choices, default=Scale.SCALE_TEN)
    nature = models.SmallIntegerField('客户性质', choices=Nature.choices, default=Nature.NATURE_YX)
    industry = models.SmallIntegerField('客户行业', choices=Industry.choices, default=Industry.INDUSTRY_JTSB)
    remarks = models.TextField('客户备注', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='创建人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer'
        verbose_name = verbose_name_plural = "客户信息"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

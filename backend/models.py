from django.contrib.auth import get_user_model
from django.db import models

from backend.choices import Status
from customer.models import Customer
from utils.models import CommonModel

User = get_user_model()


class PreSupport(CommonModel):
    """ 售前支持 """
    preplan = models.CharField('售前方案', max_length=256)
    customer = models.ForeignKey(Customer, verbose_name='客户名称', related_name='presupport', on_delete=models.CASCADE)
    product = models.CharField('产品名称', max_length=128)
    cycle = models.CharField('周期', max_length=128)
    des = models.TextField('详情', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='售前人员', related_name='presupport', on_delete=models.CASCADE)
    date = models.CharField('服务日期', max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'presupport'
        verbose_name = verbose_name_plural = '售前支持表'
        ordering = ['-created_at']

    def __str__(self):
        return self.preplan


class Implement(CommonModel):
    """ 实施 """
    testplan = models.CharField('测试方案', max_length=256)
    customer = models.ForeignKey(Customer, verbose_name='客户名称', related_name='implement', on_delete=models.CASCADE)
    report = models.TextField('测试报告', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='实施人员', related_name='implement', on_delete=models.CASCADE)
    date = models.CharField('实施日期', max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'implement'
        verbose_name = verbose_name_plural = '实施支持表'
        ordering = ['-created_at']

    def __str__(self):
        return self.testplan


class AfterSupport(CommonModel):
    """ 售后支持 """
    aftersupport = models.CharField('售后支持', max_length=500)
    customer = models.ForeignKey(Customer, verbose_name='客户名称', related_name='aftersupport', on_delete=models.CASCADE)
    status = models.SmallIntegerField('服务方式', choices=Status.choices, default=Status.STATUS_XS)
    des = models.TextField('详情', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='售后人员', related_name='aftersupport', on_delete=models.CASCADE)
    date = models.CharField('服务日期', max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'aftersupport'
        verbose_name = verbose_name_plural = '售后支持表'
        ordering = ['-created_at']

    def __str__(self):
        return self.aftersupport


class Service(CommonModel):
    """ 维修支持 """
    problem = models.TextField('故障现象', max_length=1000)
    customer = models.ForeignKey(Customer, verbose_name='客户名称', related_name='service', on_delete=models.CASCADE)
    other = models.TextField('其它事宜', max_length=1000, blank=True, null=True)
    result = models.TextField('维修结果', max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='维修人员', related_name='service', on_delete=models.CASCADE)

    class Meta:
        db_table = 'service'
        verbose_name = verbose_name_plural = '维修支持表'
        ordering = ['-created_at']

    def __str__(self):
        return self.problem


class ServiceProcess(models.Model):
    """ 维修过程 """
    date = models.CharField('日期', max_length=10)
    process = models.TextField('详情', max_length=1000)
    service = models.ForeignKey(Service, verbose_name='维修支持记录', related_name='serviceprocess', on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_process'
        verbose_name = verbose_name_plural = '维修过程表'

    def __str__(self):
        return self.service.problem

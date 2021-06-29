from django.db import models


class Injob(models.IntegerChoices):
    """联系人是否在职"""
    INJOB_YES = 1, '在职'
    INJOB_NO = 0, '离职'


class Job(models.IntegerChoices):
    """联系人职称"""
    JOB_BUSINESS = 1, '经理'
    JOB_MANAGER = 2, '采购'
    JOB_PURCHASE = 3, '技术'
    JOB_TECHNOLOGY = 4, '售后'
    JOB_AFTERSALE = 5, '业务'
    JOB_OTHER = 6, '其他'

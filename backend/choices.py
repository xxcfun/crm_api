from django.db import models


class Status(models.IntegerChoices):
    """客户拜访方式"""
    STATUS_XS = 1, '电话支持'
    STATUS_XX = 2, '现场支持'

from django.db import models


class STATUS(models.IntegerChoices):
    """客户拜访方式"""
    STATUS_XS = 1, '线上'
    STATUS_XX = 2, '线下'

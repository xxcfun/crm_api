from django.db import models


class Rank(models.IntegerChoices):
    """ 客户级别 """
    RANK_POTENTIAL = 1, '潜在客户'
    RANK_INTENTION = 2, '意向客户'
    RANK_IMPORTANT = 3, '重点客户'


class Deal(models.IntegerChoices):
    """ 是否成交 """
    DEAL_YES = 1, '成交'
    DEAL_NO = 0, '未成交'


class Scale(models.IntegerChoices):
    """ 客户规模 """
    SCALE_TEN = 1, '0~10人'
    SCALE_FIF = 2, '10~50人'
    SCALE_HUN = 3, '50~100人'
    SCALE_THO = 4, '100~1000人'
    SCALE_MORE = 5, '1000人及以上'


class Nature(models.IntegerChoices):
    """ 客户性质 """
    NATURE_GY = 1, '有限责任公司'
    NATURE_JT = 2, '股份有限公司'
    NATURE_SY = 3, '国有企业'
    NATURE_GT = 4, '集体企业'
    NATURE_HH = 5, '私营企业'
    NATURE_LY = 6, '个体工商户'
    NATURE_GFHZ = 7, '合伙企业'
    NATURE_YX = 8, '联营企业'
    NATURE_GF = 9, '股份合作制企业'


class Industry(models.IntegerChoices):
    """ 客户行业 """
    INDUSTRY_JTSB = 1, '机台设备制造商'
    INDUSTRY_SCZZ = 2, '生产制造型企业'
    INDUSTRY_XTJC = 3, '系统集成商'
    INDUSTRY_FX = 4, '分销商'
    INDUSTRY_QT = 5, '其它'

from django.db import models


class Role(models.IntegerChoices):
    """ 用户角色 """
    ROLE_JL = 1, '经理'
    ROLE_YW = 2, '业务'
    ROLE_ZG = 3, '主管'
    ROLE_SW = 4, '商务'
    ROLE_RS = 5, '人事'
    ROLE_SQ = 6, '售前'
    ROLE_JS = 7, '技术'

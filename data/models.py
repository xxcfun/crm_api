from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Data(models.Model):
    """ 用户数据统计 """
    user = models.ForeignKey(User, verbose_name='业务姓名', related_name='data', on_delete=models.CASCADE)
    yes_record = models.IntegerField('昨日拜访记录', default=0)
    yes_phone = models.IntegerField('昨日外呼数量', default=0)
    new_customer = models.IntegerField('新增客户', default=0)
    new_business = models.IntegerField('新增商机', default=0)

    week_record = models.IntegerField('本周拜访数量', default=0)
    week_phone = models.IntegerField('本周外呼数量', default=0)
    week_business = models.IntegerField('本周商机数量', default=0)

    mon_customer = models.IntegerField('本月客户数量', default=0)
    fol_business = models.IntegerField('跟进商机', default=0)
    fin_business = models.IntegerField('完成商机', default=0)

    class Meta:
        db_table = 'data'
        verbose_name = verbose_name_plural = "用户数据统计"

    def __str__(self):
        return self.user.name

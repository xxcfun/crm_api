import xadmin
from data.models import Data


class DataAdmin(object):
    list_display = ['user', 'yes_record', 'yes_phone', 'new_customer', 'new_business',
                    'week_record', 'week_phone', 'week_business',
                    'mon_customer', 'fol_business', 'fin_business']


xadmin.site.register(Data, DataAdmin)

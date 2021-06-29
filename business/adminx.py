import xadmin
from business.models import Business


class BusinessAdmin(object):
    list_display = ['name', 'customer', 'winning_rate', 'money', 'user']


xadmin.site.register(Business, BusinessAdmin)

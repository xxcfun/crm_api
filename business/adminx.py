import xadmin
from business.models import Business, BusinessProduct


class BusinessAdmin(object):
    list_display = ['id', 'name', 'customer', 'winning_rate', 'money', 'user']


class BusinessProductAdmin(object):
    list_display = ['id', 'name', 'business', 'number', 'price']


xadmin.site.register(Business, BusinessAdmin)
xadmin.site.register(BusinessProduct, BusinessProductAdmin)

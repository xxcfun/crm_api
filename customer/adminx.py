import xadmin
from customer.models import Customer


class CustomerAdmin(object):
    list_display = ['name', 'rank', 'is_deal', 'scale', 'industry', 'user']


xadmin.site.register(Customer, CustomerAdmin)

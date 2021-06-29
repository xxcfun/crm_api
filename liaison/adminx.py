import xadmin
from liaison.models import Liaison


class LiaisonAdmin(object):
    list_display = ['name', 'customer', 'phone', 'job', 'injob', 'user']


xadmin.site.register(Liaison, LiaisonAdmin)
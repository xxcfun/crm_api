import xadmin
from record.models import Record


class RecordAdmin(object):
    list_display = ['theme', 'customer', 'status', 'main', 'next', 'user']


xadmin.site.register(Record, RecordAdmin)

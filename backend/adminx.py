import xadmin
from backend.models import PreSupport, Implement, AfterSupport, Service, ServiceProcess


class PreSupportAdmin(object):
    list_display = ['id', 'preplan', 'customer', 'product', 'cycle', 'user', 'date']


class ImplementAdmin(object):
    list_display = ['id', 'impplan', 'customer', 'product', 'report', 'user', 'date']


class AfterSupportAdmin(object):
    list_display = ['id', 'aftersupport', 'customer', 'status', 'des', 'user', 'date']


class ServiceAdmin(object):
    list_display = ['id', 'problem', 'customer', 'other', 'result', 'user']


class ServiceProcessAdmin(object):
    list_display = ['id', 'date', 'process', 'service']


xadmin.site.register(PreSupport, PreSupportAdmin)
xadmin.site.register(Implement, ImplementAdmin)
xadmin.site.register(AfterSupport, AfterSupportAdmin)
xadmin.site.register(Service, ServiceAdmin)
xadmin.site.register(ServiceProcess, ServiceProcessAdmin)

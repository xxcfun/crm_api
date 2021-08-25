from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from backend import views

router = DefaultRouter()

# 售前支持
router.register(r'presupport', views.PreSupportViewset, basename='presupport')
# 实施支持
router.register(r'implement', views.ImplementViewset, basename='implement')
# 售后支持
router.register(r'aftersupport', views.AfterSupportViewset, basename='aftersupport')
# 维修支持
router.register(r'service', views.ServiceViewset, basename='service')
router.register(r'serviceprocess', views.ServiceProcessViewset, basename='serviceprocess')
# 所有支持列表
router.register(r'all/presupport', views.AllPreSupportViewset, basename='all_presupport')
router.register(r'all/implement', views.AllImplementViewset, basename='all_implement')
router.register(r'all/aftersupport', views.AllAfterSupportViewset, basename='all_aftersupport')
router.register(r'all/service', views.AllServiceViewset, basename='all_service')
router.register(r'files', views.FileViewset, basename='files')

urlpatterns = [
    re_path('^', include(router.urls))
]

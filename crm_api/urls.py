"""crm_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from crm_api.settings import MEDIA_ROOT

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path('docs', include_docs_urls(title='系统接口文档')),
    path('api-auth/',include('rest_framework.urls')),
    path('customer/', include('customer.urls')),
    path('account/', include('account.urls')),
    path('liaison/', include('liaison.urls')),
    path('record/', include('record.urls')),
    path('business/', include('business.urls')),
    path('data/', include('data.urls')),
    path('backend/', include('backend.urls'))
]

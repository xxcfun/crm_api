from django.urls import path

from customer import views

urlpatterns = [
    # 客户信息列表
    path('customer/list/', views.CustomerList.as_view(), name='customer_list'),
    # 客户详情（删改查）
    path('customer/detail/<int:pk>', views.CustomerDetail.as_view(), name='customer_detail'),
    # 客户添加
    path('customer/add/', views.CustomerAdd.as_view(), name='customer_add')
]
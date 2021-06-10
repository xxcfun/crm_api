from django.urls import path

from account import views

urlpatterns = [
    # 用户登入
    path('user/login/', views.user_login, name='user_login'),
    # 用户登出
    path('user/logout/', views.user_logout, name='user_logout')
]

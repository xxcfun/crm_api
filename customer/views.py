from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from customer.models import Customer
from customer.serializers import CustomerSerializer, CustomerDetailSerializer, LinkCustomerListSerializer, \
    AllCustomerSerializer
from utils.permissions import IsOwnerOrReadOnly


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class CustomerViewset(viewsets.ModelViewSet):
    """
    客户管理
    get list:
        获取客户
    post create:
        添加客户
    put update:
        更新客户
    delete destroy:
        删除客户
    """
    # permission是用来做权限判断的
    # IsAuthenticated：必须登录用户；IsOwnerOrReadOnly：必须是当前登录的用户
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == 'list':
            return CustomerSerializer
        else:
            return CustomerDetailSerializer

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)
        rank = self.request.GET.get('rank', None)
        if rank:
            query = query & Q(rank=rank)
        is_deal = self.request.GET.get('is_deal', None)
        if is_deal:
            query = query & Q(is_deal=is_deal)
        industry = self.request.GET.get('industry', None)
        if industry:
            query = query & Q(industry=industry)
        queryset = Customer.objects.filter(query)
        return queryset

    # 如果要进行逻辑删除，那么重写下面两个方法
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def perform_destroy(self, instance):
    #     print(instance)
    #     instance.is_valid = False
    #     instance.save()


class LinkCustomerViewset(viewsets.ModelViewSet):
    """ 外键关联客户 """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LinkCustomerListSerializer

    def get_queryset(self):
        return Customer.objects.filter(is_valid=True, user=self.request.user)


class AllCustomerViewset(viewsets.ModelViewSet):
    """ 所有客户信息 """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AllCustomerSerializer
    pagination_class = Pagination

    def get_queryset(self):
        query = Q(is_valid=True)
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)
        rank = self.request.GET.get('rank', None)
        if rank:
            query = query & Q(rank=rank)
        is_deal = self.request.GET.get('is_deal', None)
        if is_deal:
            query = query & Q(is_deal=is_deal)
        industry = self.request.GET.get('industry', None)
        if industry:
            query = query & Q(industry=industry)
        queryset = Customer.objects.filter(query)
        return queryset

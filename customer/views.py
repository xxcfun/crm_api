from django import http
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import BaseDetailView

from customer import serializers
from customer.forms import CustomerForm
from customer.models import Customer
from utils.response import NotFoundJsonResponse


class CustomerList(ListView):
    """ 客户列表 """
    paginate_by = 10

    def get_queryset(self):
        """ 重写查询方法 """
        user = self.request.user
        query = Q(is_valid=True, user=user)
        # query = Q(is_valid=True)
        # 客户名称查询
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)
        # 客户级别查询
        rank = self.request.GET.get('rank', None)
        if rank:
            query = query & Q(rank=rank)
        # 是否成交
        is_deal = self.request.GET.get('is_deal', None)
        if is_deal:
            query = query & Q(is_deal=is_deal)
        # 客户行业
        industry = self.request.GET.get('industry', None)
        if industry:
            query = query & Q(industry=industry)
        queryset = Customer.objects.filter(query)
        return queryset

    def get_paginate_by(self, queryset):
        """ 从前端控制每一页的分页大小 """
        page_size = self.request.GET.get('limit', None)
        return page_size or self.paginate_by

    def render_to_response(self, context, **response_kwargs):
        page_obj = context['page_obj']
        if page_obj is not None:
            data = serializers.CustomerListSerializer(page_obj).to_dict()
            return http.JsonResponse(data)
        else:
            return NotFoundJsonResponse()


class CustomerAdd(BaseDetailView):
    """ 添加客户 """
    def post(self, request, *args, **kwargs):
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponse('添加成功', status=201)
        return http.HttpResponse('添加失败', status=200)


class CustomerDetail(BaseDetailView):
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    def get_queryset(self):
        user = self.request.user
        return Customer.objects.filter(user=user, is_valid=True)

    def get(self, request, *args, **kwargs):
        """ GET：客户详情 """
        # 获取客户对象
        customer_obj = self.get_object()
        data = serializers.CustomerDetailSerializer(customer_obj).to_dict()
        return http.JsonResponse(data)

    def post(self, request, *args, **kwargs):
        """ POST：客户修改 """
        customer_obj = self.get_object()
        form = CustomerForm(data=request.POST, instance=customer_obj)
        if form.is_valid():
            form.save()
            return http.HttpResponse('修改成功', status=201)
        return http.HttpResponse('修改失败', status=200)

    def delete(self, request, *args, **kwargs):
        """ DELETE：客户删除 """
        customer_obj = self.get_object()
        if customer_obj.is_valid:
            customer_obj.is_valid = False
            customer_obj.save()
            return http.HttpResponse('删除成功', status=201)
        else:
            pass

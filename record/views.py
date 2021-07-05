from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from customer.views import Pagination
from record.models import Record
from record.serializers import RecordSerializer, RecordCreateSerializer, RecordDetailSerializer, AllRecordSerializer
from utils.permissions import IsOwnerOrReadOnly


class RecordViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == 'list':
            return RecordSerializer
        elif self.action == 'create':
            return RecordCreateSerializer
        else:
            return RecordDetailSerializer

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        theme = self.request.GET.get('theme', None)
        if theme:
            query = query & Q(theme__icontains=theme)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        queryset = Record.objects.filter(query)
        return queryset


class AllRecordViewset(viewsets.ModelViewSet):
    """ 所有拜访记录信息 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AllRecordSerializer
    pagination_class = Pagination

    def get_queryset(self):
        query = Q(is_valid=True)
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        theme = self.request.GET.get('theme', None)
        if theme:
            query = query & Q(theme__icontains=theme)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        queryset = Record.objects.filter(query)
        return queryset

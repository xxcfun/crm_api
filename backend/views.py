from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from backend.models import PreSupport, Implement, AfterSupport, Service, ServiceProcess
from backend.serializers import ServiceDetailSerializer, ServiceCreateSerializer, ServiceSerializer, \
    AfterSupportDetailSerializer, AfterSupportSerializer, AfterSupportCreateSerializer, ImplementSerializer, \
    ImplementCreateSerializer, ImplementDetailSerializer, PreSupportDetailSerializer, PreSupportCreateSerializer, \
    PreSupportSerializer, ServiceProcessSerializer
from customer.views import Pagination
from utils.permissions import IsOwnerOrReadOnly


class PreSupportViewset(viewsets.ModelViewSet):
    """ 售前支持 """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PreSupportSerializer
        elif self.action == 'create':
            return PreSupportCreateSerializer
        else:
            return PreSupportDetailSerializer

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        queryset = PreSupport.objects.filter(query)
        return queryset


class AllPreSupportViewset(viewsets.ModelViewSet):
    """ 所有售前支持 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination
    serializer_class = PreSupportSerializer

    def get_queryset(self):
        query = Q(is_valid=True)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        queryset = PreSupport.objects.filter(query)
        return queryset



class ImplementViewset(viewsets.ModelViewSet):
    """ 实施支持 """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == 'list':
            return ImplementSerializer
        elif self.action == 'create':
            return ImplementCreateSerializer
        else:
            return ImplementDetailSerializer

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        queryset = Implement.objects.filter(query)
        return queryset


class AllImplementViewset(viewsets.ModelViewSet):
    """ 所有实施支持 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination
    serializer_class = ImplementSerializer

    def get_queryset(self):
        query = Q(is_valid=True)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        queryset = Implement.objects.filter(query)
        return queryset


class AfterSupportViewset(viewsets.ModelViewSet):
    """ 售后支持 """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == 'list':
            return AfterSupportSerializer
        elif self.action == 'create':
            return AfterSupportCreateSerializer
        else:
            return AfterSupportDetailSerializer

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        queryset = AfterSupport.objects.filter(query)
        return queryset


class AllAfterSupportViewset(viewsets.ModelViewSet):
    """ 所有售后支持 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination
    serializer_class = AfterSupportSerializer

    def get_queryset(self):
        query = Q(is_valid=True)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        queryset = AfterSupport.objects.filter(query)
        return queryset


class ServiceViewset(viewsets.ModelViewSet):
    """ 维修支持 """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceSerializer
        elif self.action == 'create':
            return ServiceCreateSerializer
        else:
            return ServiceDetailSerializer

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        problem = self.request.GET.get('problem', None)
        if problem:
            query = query & Q(problem__icontains=problem)
        queryset = Service.objects.filter(query)
        return queryset


class AllServiceViewset(viewsets.ModelViewSet):
    """ 所有维修支持 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination
    serializer_class = ServiceSerializer

    def get_queryset(self):
        query = Q(is_valid=True)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        problem = self.request.GET.get('problem', None)
        if problem:
            query = query & Q(problem__icontains=problem)
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        queryset = Service.objects.filter(query)
        return queryset


class ServiceProcessViewset(viewsets.ModelViewSet):
    """ 维修过程 """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ServiceProcessSerializer

    def get_queryset(self):
        service = self.request.GET.get('service', None)
        if service:
            return ServiceProcess.objects.filter(service_id=service)

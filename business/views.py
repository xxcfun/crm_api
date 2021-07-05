from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from business.models import Business
from business.serializers import BusinessSerializer, BusinessCreateSerializer, BusinessDetailSerializer, \
    AllBusinessSerializer
from customer.views import Pagination
from utils.permissions import IsOwnerOrReadOnly


class BusinessViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = Pagination

    def get_serializer_class(self):
        if self.action == 'list':
            return BusinessSerializer
        elif self.action == 'create':
            return BusinessCreateSerializer
        else:
            return BusinessDetailSerializer

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        winning_rate = self.request.GET.get('winning_rate', None)
        if winning_rate:
            query = query & Q(winning_rate=winning_rate)
        queryset = Business.objects.filter(query)
        return queryset


class AllBusinessViewset(viewsets.ModelViewSet):
    """ 商机 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AllBusinessSerializer
    pagination_class = Pagination

    def get_queryset(self):
        query = Q(is_valid=True)
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        winning_rate = self.request.GET.get('winning_rate', None)
        if winning_rate:
            query = query & Q(winning_rate=winning_rate)
        queryset = Business.objects.filter(query)
        return queryset

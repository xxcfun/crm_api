from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from business.models import Business
from business.serializers import BusinessSerializer
from customer.views import Pagination
from utils.permissions import IsOwnerOrReadOnly


class BusinessViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # auth使用来做用户认证的
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = BusinessSerializer
    pagination_class = Pagination

    def get_queryset(self):
        query = Q(is_valid=True, user=self.request.user)
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)
        customer = self.request.GET.get('customer', None)
        if customer:
            query = query & Q(customer__name__icontains=customer)
        queryset = Business.objects.filter(query)
        return queryset

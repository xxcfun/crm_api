import datetime

from django.db.models import Q
from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from business.choices import WinRate
from business.models import Business
from customer.models import Customer
from data.models import Data
from data.serializers import DataSerializer, DataCustomerSerializer, DataLiaisonSerializer, DataRecordSerializer, \
    DataBusinessSerializer
from liaison.models import Liaison
from record.choices import STATUS
from record.models import Record
from utils.permissions import IsOwnerOrReadOnly

now = datetime.datetime.now()
day_num = now.isoweekday()
week_day = now - datetime.timedelta(days=day_num)


class DataViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 数据汇总 """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = DataSerializer

    def get_queryset(self):
        # 定义一些日期
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        yesterday = now - datetime.timedelta(days=1)
        yesterday_year = yesterday.year
        yesterday_month = yesterday.month
        yesterday_day = yesterday.day

        user = self.request.user
        customer = Customer.objects.filter(user=user)
        record = Record.objects.filter(user=user)
        business = Business.objects.filter(user=user)

        # 昨日拜访
        yes_record = record.filter(status=STATUS.STATUS_XX,
                                         created_at__year=yesterday_year, created_at__month=yesterday_month,
                                         created_at__day=yesterday_day).count()
        # 昨日外呼
        yes_phone = record.filter(status=STATUS.STATUS_XS,
                                        created_at__year=yesterday_year, created_at__month=yesterday_month,
                                        created_at__day=yesterday_day).count()
        # 新增客户
        new_customer = customer.filter(created_at__year=year, created_at__month=month, created_at__day=day).count()
        # 新增商机
        new_business = business.filter(created_at__year=year, created_at__month=month, created_at__day=day).count()

        # 本周拜访
        week_record = record.filter(created_at__range=(week_day, now), status=STATUS.STATUS_XX).count()
        # 本周外呼
        week_phone = record.filter(created_at__range=(week_day, now), status=STATUS.STATUS_XS).count()
        # 本周商机
        week_business = business.filter(created_at__range=(week_day, now)).count()

        # 本月新增客户数量
        mon_customer = customer.filter(created_at__year=year, created_at__month=month).count()
        # 跟进商机
        fol_business = business.exclude(winning_rate=WinRate.WINNING_DONE).count()
        # 完成商机
        fin_business = business.filter(winning_rate=WinRate.WINNING_DONE).count()

        # 更新数据
        Data.objects.filter(user=user).update(
            yes_record=yes_record, yes_phone=yes_phone,
            new_customer=new_customer, new_business=new_business,
            week_record=week_record, week_phone=week_phone, week_business=week_business,
            mon_customer=mon_customer, fol_business=fol_business, fin_business=fin_business
        )

        queryset = Data.objects.all()
        return queryset


class DataCustomerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 一周客户数据汇总 """
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = DataCustomerSerializer

    def get_queryset(self):
        query = Q(is_valid=True, created_at__range=(week_day, now))
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        else:
            query = query & Q(user=self.request.user)
        queryset = Customer.objects.filter(query)
        return queryset


class DataLiaisonViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 一周联系人数据汇总 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = DataLiaisonSerializer

    def get_queryset(self):
        query = Q(is_valid=True, created_at__range=(week_day, now))
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        else:
            query = query & Q(user=self.request.user)
        queryset = Liaison.objects.filter(query)
        return queryset


class DataRecordViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 一周拜访记录数据汇总 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = DataRecordSerializer

    def get_queryset(self):
        query = Q(is_valid=True, created_at__range=(week_day, now))
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        else:
            query = query & Q(user=self.request.user)
        queryset = Record.objects.filter(query)
        return queryset


class DataBusinessViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """ 一周商机数据汇总 """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = DataBusinessSerializer

    def get_queryset(self):
        query = Q(is_valid=True, created_at__range=(week_day, now))
        username = self.request.GET.get('username', None)
        if username:
            query = query & Q(user__username=username)
        else:
            query = query & Q(user=self.request.user)
        queryset = Business.objects.filter(query)
        return queryset

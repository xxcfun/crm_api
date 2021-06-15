from utils.serializers import BaseListPageSerializer, BaseSerializer


class CustomerListSerializer(BaseListPageSerializer):
    """ 客户列表 """
    def get_object(self, obj):
        user = obj.user
        return {
            'id': obj.id,
            'name': obj.name,
            'rank': obj.get_rank_display(),
            'is_deal': obj.get_is_deal_display(),
            'website': obj.website,
            'scale': obj.get_scale_display(),
            'nature': obj.get_nature_display(),
            'industry': obj.get_industry_display(),
            'remarks': obj.remarks,
            'user': {
                'pk': user.pk,
                'username': user.username
            },
            'created_at': obj.created_at
        }


class CustomerDetailSerializer(BaseSerializer):
    """ 客户详情信息 """
    def to_dict(self):
        obj = self.obj
        return {
            'id': obj.id,
            'name': obj.name,
            'rank': obj.get_rank_display(),
            'is_deal': obj.get_is_deal_display(),
            'website': obj.website,
            'scale': obj.get_scale_display(),
            'nature': obj.get_nature_display(),
            'industry': obj.get_industry_display(),
            'remarks': obj.remarks,
        }
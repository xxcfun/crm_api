from utils.serializers import BaseSerializer


class UserSerializers(BaseSerializer):
    """ 用户信息 """
    def to_dict(self):
        obj = self.obj
        return {
            'username': obj.username,
        }
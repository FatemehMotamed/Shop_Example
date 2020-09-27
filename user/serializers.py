from rest_framework import serializers

from user.models import User, UserRole


class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','tel','user_role_id']

class UserRoleserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserRole
        fields=['name','id']
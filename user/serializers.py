from rest_framework import serializers

from user.models import User


class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','tel']
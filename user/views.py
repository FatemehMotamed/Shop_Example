from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializers import UserSerilizer
from rest_framework import viewsets, status


def index(request):
    return render(request,'users.html')

class ApiUsers(viewsets.ViewSet):
    # queryset=User.objects.all()
    serializer_class = UserSerilizer
    def list(self,request):
        queryset=User.objects.all()
        serializer_class=UserSerilizer(queryset,many=True)
        return Response(serializer_class.data)

    def create(self,request):
        data=UserSerilizer(data=request.data)
        if not data.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'invalid data'})
        new_user=User()
        UserSerilizer(data=request.data)
        new_user.first_name=data['first_name'].value
        new_user.last_name=data['last_name'].value
        new_user.tel=data['tel'].value
        new_user.save()
        return Response(data={'data':request.data,'message':'valid data'},status=status.HTTP_201_CREATED)

from django.urls import path, include

from user.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'users', ApiUsers,basename='user')
urlpatterns = [

    path('',include(router.urls)),
]

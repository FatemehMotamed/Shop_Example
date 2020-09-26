

from django.db import models

# Create your models here.
class UserRole(models.Model):
    name=models.CharField(max_length=70)

class User(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    tel=models.CharField(max_length=25,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user_role=models.ForeignKey(UserRole,on_delete=models.CASCADE,null=True)




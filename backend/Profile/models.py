from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL        #auth.User

class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    first_name=models.CharField(max_length=30, null=True, blank=True)
    last_name =models.CharField(max_length=30, null=True, blank=True)
    birth_date=models.DateField(auto_now=False,auto_now_add=False, null=True, blank=True)
    address1=models.CharField(max_length=64, null=True, blank=True)
    address2=models.CharField(max_length=64, null=True, blank=True)
    city=models.CharField(max_length=32,null=True, blank=True)
    county=models.CharField(max_length=32,null=True, blank=True)
    state=models.CharField(max_length=32,null=True, blank=True)
    zipcode=models.CharField(max_length=5, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=10, null=True, blank=True)

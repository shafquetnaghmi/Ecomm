from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from colorfield.fields import ColorField

class User(AbstractUser):   #model for user so that we can add to custome field to UserCreationForm
    phone=models.TextField(max_length=20,blank=False)
    is_verified = models.BooleanField(default=False)

class Product(models.Model):            #model to add product and its specifications 
   name = models.CharField(max_length=200, db_index=True)
   slug = models.SlugField(max_length=200, db_index=True)
   image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
   color = ColorField(default='#FF0000')
   description = models.TextField(blank=True,null=True)
   performance=models.TextField(blank=True,null=True)
   Display=models.TextField(blank=True,null=True)
   Camera=models.TextField(blank=True,null=True)
   Battery=models.TextField(blank=True,null=True)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   available = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
 
   def __str__(self):
       return f'{self.name}'


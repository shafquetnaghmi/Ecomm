from rest_framework import generics
from ecommapp.models import Product
from ecommapp.api.serializer import ProductSerializers 

class ProductCreateAPIView(generics.CreateAPIView):     # using django rest framework to create api endpoints 
      queryset=Product.objects.all()
      serializer_class=ProductSerializers

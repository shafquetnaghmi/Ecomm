from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from ecommapp.api.views import ProductCreateAPIView

urlpatterns=[
        path('login/',auth_views.LoginView.as_view(template_name="ecommapp/login.html"),name="login"),
        path('logout/',auth_views.LogoutView.as_view(template_name="ecommapp/logout.html"),name="logout"),
        path('signup/',views.register,name="signup"),
        path('index/',views.index,name='index'),
        path('verify/', views.verify_code,name="verify"), 
        path('store/',views.product_list,name="store"),
        path('cart/<str:id>/',views.product_deatail,name="cart"),
        path('api/store/',ProductCreateAPIView.as_view(),name="store-api")    #api endpoints 

]


        
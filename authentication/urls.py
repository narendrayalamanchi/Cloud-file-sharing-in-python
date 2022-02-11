from django.urls import path,include
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('login',login,name="login" ),
    path('register',register,name="register" ),
]
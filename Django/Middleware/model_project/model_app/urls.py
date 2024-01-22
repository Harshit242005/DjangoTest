# myapp/urls.py
from django.urls import path
from .views import index, home

urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    
]

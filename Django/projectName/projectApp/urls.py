"""projectName URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# projectApp/urls.py
from django.urls import path
from projectApp.views import home_view, about_view
from .views import contact_view, hello_world
from .views import signup, login
urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('hello_world/', hello_world, name='hello_world'),
    # defining the endpoint for the signup & login
    path('signup/', signup, name='signup'),
    path('login/', login, name='login')
]
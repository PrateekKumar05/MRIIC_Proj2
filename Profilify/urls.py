from django.contrib import admin
from django.urls import path
from RPMS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('registration', views.registration, name='registration'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('profile', views.profile, name='profile'),
    path('contact',views.contact,name='contact'),
]
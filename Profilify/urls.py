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
    # path('create/', views.profile_create, name='profile_create'),
    # path('edit/', views.profile_edit, name='profile_edit'),
    # path('list/', views.profile_list, name='profile_list'),
    # path('<int:pk>/', views.profile_detail, name='profile_detail'),
]
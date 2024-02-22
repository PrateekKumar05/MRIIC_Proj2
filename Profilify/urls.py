from django.contrib import admin
from django.urls import path
from RPMS import views
from RPMS.views import upload_file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('registration', views.registration, name='registration'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact',views.contact,name='contact'),
    path('upload/', views.upload_file, name='upload_file'),
    path('profile', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

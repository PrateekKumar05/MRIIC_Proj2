from django.contrib import admin
from django.urls import path
from RPMS import views
from RPMS.views import upload_file
from django.conf import settings
from django.conf.urls.static import static
from RPMS.views import leaderboard
from RPMS.views import chart_data
from RPMS.views import logistics
from RPMS.views import download_contact_info

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
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('chart-data/', chart_data, name='chart_data'),
    path('logistics/', logistics, name='logistics'),
    path('download-contact-info/', download_contact_info, name='download_contact_info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from .models import contact_info
from .models import UserProfile

admin.site.register(contact_info)
admin.site.register(UserProfile)

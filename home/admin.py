from django.contrib import admin
from .models import Neighborhood,Business,UserProfile,EmergencyContacts,Post

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(UserProfile)
admin.site.register(EmergencyContacts)
admin.site.register(Post)

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from . models import UserProfile, Projects

# Register your models here.

class PrfileAdmin(admin.StackedInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
    inlines = [PrfileAdmin]
    fields = (
        'username','email','password','first_name','last_name','last_login','date_joined','is_active','is_superuser','is_staff'
    )
    
admin.site.unregister(User)
admin.site.register((User,), UserAdmin)
admin.site.register(Projects)
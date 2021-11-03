from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from . models import Contact, UserProfile, Projects, Resume

# Register your models here.

class ProfileAdmin(admin.StackedInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileAdmin]
    fields = (
        'username','email','password','first_name','last_name','last_login','date_joined','is_active','is_superuser','is_staff'
    )

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title','name','email',)
    
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title','place','description','section','year','date','active',)
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Projects)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Resume, ResumeAdmin)

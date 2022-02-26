from django.contrib import admin
from .models import UserAccount

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name','username']

admin.site.register(UserAccount , UserAccountAdmin)
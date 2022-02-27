from django.contrib import admin

from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ['id','card_number','expiry_month','expiry_year','cvv']

admin.site.register(Card , CardAdmin)
from django.contrib import admin
from .models import Currency,Price
# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display  = ('code','name','type','symbol','created_at')
    list_filter   = ('type',)
    search_fields = ('code','name','symbol')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display  = ("base_currency","quote_currency",'rate','timestamp','source')
    list_filter   = ('base_currency','quote_currency','source')
    search_fields = ('base_currency__code','quote_currency__code','source')
    ordering      = ['-timestamp']
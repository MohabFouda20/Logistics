from django.contrib import admin
from .models import order
# Register your models here.
class orderAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'shipper',
        'phone',
        'government',
        'order_status',
    ]
    search_fields = [
        'name',
        'shipper',
        'phone',
        'government',
        'order_status',
    ]




admin.site.register(order, orderAdmin)

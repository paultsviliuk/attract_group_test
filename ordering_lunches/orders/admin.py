from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created', 'paid']
    list_filter = ['customer', 'created']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
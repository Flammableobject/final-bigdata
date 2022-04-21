from django.contrib import admin
from myapp.models import Customer, Item, OrderItem, Invoice
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(OrderItem, OrderItemAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Invoice, InvoiceAdmin)
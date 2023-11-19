from django.contrib import admin

from .models import Product, Invoice,InvoiceItem

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name']
    search_fields = ['name']

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'price', 'get_item_total', 'invoice']
    list_filter = ['invoice' , 'product']
    search_fields = ['invoice__pk' , 'product__name']

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'date', 'customer', 'created_by', 'get_total']
    list_filter = ['date', 'customer']
    search_fields = ['date', 'customer']
    inlines = [InvoiceItemInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)

from django.contrib import admin
from api.models import Invoice,InvoiceDetail

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('Date','InvoiceNo','CustomerName')

class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('invoice','description','quantity','unit_price','price')

admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(InvoiceDetail,InvoiceDetailAdmin)
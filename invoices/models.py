from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.timezone import now


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Invoice(models.Model):
    date = models.DateTimeField(default=now)
    customer = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    @admin.display(description ="Total")
    def get_total(self):
        total = 0
        items = self.invoiceitem_set.all()
        for item in items:
            total +=item.get_item_total()
        return total
    
    def __str__(self) -> str:
        return f'{self.pk}'
    
class InvoiceItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    
    @admin.display(description ="Item Total")
    def get_item_total(self):
        return self.quantity * self.price
    
    def __str__(self) -> str:
        return f'{self.invoice.pk}-{self.product.name}'
    

    
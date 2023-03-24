from django.db import models

# Create your models here.
class Invoice(models.Model):
    Date = models.DateField()
    InvoiceNo = models.IntegerField()
    CustomerName = models.CharField(max_length=30)


class InvoiceDetail(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='sungby')
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    price = models.FloatField()



from django.db import models
from customer.models import *
from product.models import *
import datetime

class Buy(models.Model):
  dateTransaction = models.DateField(default=datetime.date.today)
  customerID = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE, related_name="Customer")
  productID = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, related_name="Product")
  quantity = models.IntegerField()
  class Meta:
    db_table = "Buy"

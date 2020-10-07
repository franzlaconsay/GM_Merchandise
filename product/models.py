from django.db import models
from datetime import datetime

class Product(models.Model):
	sku = models.CharField(primary_key = True, max_length = 5)
	dateregistered = models.DateField(auto_now = True, null = False, blank = False)
	category = models.CharField(max_length = 20, null = False, blank = False)
	name = models.CharField(max_length = 20, null = False, blank = False)
	brand = models.CharField(max_length = 20)
	color = models.CharField(max_length = 20)
	sizeDimension = models.CharField(max_length = 20)
	price = models.IntegerField()
	stocks = models.IntegerField() 

	class Meta:
		db_table = "Product"

class ProductImages(models.Model):
	product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
	image1 = models.ImageField()

	class Meta:
		db_table = "Prod_Images"
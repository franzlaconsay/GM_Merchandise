from django import forms
from .models import *

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('category','name', 'price', 'stocks')

class ProductImagesForm(forms.ModelForm):

	class Meta:
		model = ProductImages
		fields = ('image1',)
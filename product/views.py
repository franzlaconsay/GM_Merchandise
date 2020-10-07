from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import ProductForm
from .forms import ProductImagesForm
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
import uuid

class ProductIndexView(View):
	def get(self,request):
		qsproducts = Product.objects.all()
		qsprodimages = ProductImages.objects.all()

		context = {
			'products' : qsproducts,
			'prodimages' : qsprodimages
		}
		return render(request,'product/productSummary.html', context)

	def post(self, request):
		if request.method == 'POST':	
			if 'btnUpdate' in request.POST:	
				print('update profile button clicked')
				sku = request.POST.get("skuField")	
				category = request.POST.get("categoryField");
				brand = request.POST.get("brandField");
				name = request.POST.get("nameField")
				color = request.POST.get("colorField")
				length = request.POST.get("lengthField")
				width = request.POST.get("widthField")
				price = request.POST.get("priceField")
				stocks = request.POST.get("stocksField")

				update_product = Product.objects.filter(sku = sku).update(category = category, brand = brand, name = name, color = color, sizeDimension = ""+str(length or 0)+"x"+str(width or 0),  price = price, stocks = stocks)

				update_prodIMG = ProductImages.objects.filter(product_id = sku)
				
				if request.FILES.get('image1', False) != False:
					update_img = ProductImages.objects.get(id = update_prodIMG[0].id)
					update_img.image1 = request.FILES['image1']
					update_img.save()
				
				if request.FILES.get('image2', False) != False:
					update_img = ProductImages.objects.get(id = update_prodIMG[1].id)
					print(update_img)
					print(request.FILES['image2'])
					update_img.image1 = request.FILES['image2']
					update_img.save()
				
				if request.FILES.get('image3', False) != False:
					update_img = ProductImages.objects.get(id = update_prodIMG[2].id)
					print(update_img)
					print(request.FILES['image3'])
					update_img.image1 = request.FILES['image3']
					update_img.save()

				print(update_product)

			elif 'btnDelete' in request.POST:	
				print('delete button clicked')
				sku = request.POST.get("product-sku")	
				prod = Product.objects.filter(sku = sku).delete()
				prodImage = ProductImages.objects.filter(product_id = sku).delete()
				print('recorded deleted')
			return redirect('product:product_summary_view')

class ProductRegistrationView(View):
	def get(self, request):
		return render(request, 'product/productRegistration.html')

	def post(self, request):
		form = ProductForm(request.POST)
		form2 = ProductImagesForm(request.POST, request.FILES)

		if form.is_valid() and form2.is_valid():
			categoryp = request.POST.get("category")
			namep = request.POST.get("name")
			brandp = request.POST.get("brand")
			colorp = request.POST.get("color")
			lengthp = request.POST.get("size1")
			widthp = request.POST.get("size2")
			pricep = request.POST.get("price")
			stocksp = request.POST.get("stocks")

			form = Product(sku = uuid.uuid4().hex[:5].upper(), category = categoryp, name = namep, brand = brandp, 
				color = colorp, sizeDimension = ""+str(lengthp or 0)+"x"+str(widthp or 0), 
				price = pricep, stocks = stocksp)
			form.save()

			if request.FILES.get('image1', False) != False:
				image1p = request.FILES["image1"];
				form2 = ProductImages(product = form, image1 = image1p)
				form2.save()
			else:
				form2 = ProductImages(product = form, image1 = "none.jpg")
				form2.save()

			if request.FILES.get('image2', False) != False:
				image2p = request.FILES["image2"];
				form2 = ProductImages(product = form, image1 = image2p)
				form2.save()
			else:
				form2 = ProductImages(product = form, image1 = "none.jpg")
				form2.save()

			if request.FILES.get('image3', False) != False:
				image3p = request.FILES["image3"];
				form2 = ProductImages(product = form, image1 = image3p)
				form2.save()
			else:
				form2 = ProductImages(product = form, image1 = "none.jpg")
				form2.save()

			#instead of httpresponse, i made a message that will be displayed in the same page po
			messages.success(request, 'The product is successfully added.')
			return render(request, 'product/productRegistration.html')
		else:
			messages.success(request, 'ERROR. The product is not added in the database. It must include IMAGE/S.')
			return render(request, 'product/productRegistration.html')
# Create your views here.

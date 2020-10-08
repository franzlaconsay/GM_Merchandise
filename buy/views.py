from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from product.models import *
from .models import *
from landingpage.views import *

class CategoriesIndexView(View):
	def get(self,request):
		qsProducts = Product.objects.all()
		qsImages = []
		for product in qsProducts:
			image = ProductImages.objects.filter(product_id=product.sku)
			qsImages.append(image[0].image1)

		xlist = zip(qsProducts,qsImages)
		xlist2 = zip(qsProducts,qsImages)
		xlist3 = zip(qsProducts,qsImages)
		xlist4 = zip(qsProducts,qsImages)
		xlist5 = zip(qsProducts,qsImages)
		xlist6 = zip(qsProducts,qsImages)
		xlist7 = zip(qsProducts,qsImages)
		xlist8 = zip(qsProducts,qsImages)
		user = request.session['user']
		firstName = request.session['firstName']
		lastName = request.session['lastName']
		
		context = {
			'products' : xlist,
			'products2' : xlist2,
			'products3' : xlist3,
			'products4' : xlist4,
			'products5' : xlist5,
			'products6' : xlist6,
			'products7' : xlist7,
			'products8' : xlist8,
			'user' : user,
			'firstname' : firstName,
			'lastname' : lastName
		}
		return render(request,'buy/categories.html', context, )

	def post(self,request):
		if request.method == "POST":
			user = request.POST.get("user")
			sku = request.POST.get("sku")
			stocks = request.POST.get("stocks")
			quantity = request.POST.get("quantity")
			customer = Customer.objects.get(id=user)
			product = Product.objects.get(sku=sku)
			form = Buy(customerID = customer, productID = product, quantity=quantity)
			form.save()
			newStocks = int(stocks)-int(quantity)
			Product.objects.filter(sku=sku).update(stocks=newStocks)
			return HttpResponseRedirect('category')

class CartIndexView(View):
	def get(self,request):
		return render(request,'buy/cart.html')

class WhatsNewIndexView(View):
	def get(self,request):
		qsProducts = Product.objects.filter(dateregistered__range=["2020-10-01", "2020-10-30"])
		qsImages = []
		for product in qsProducts:
			image = ProductImages.objects.filter(product_id=product.sku)
			qsImages.append(image[0].image1)
		xlist = zip(qsProducts,qsImages)
		user = request.session['user']
		firstName = request.session['firstName']
		lastName = request.session['lastName']
		context = {
			'products' : xlist,
			'user' : user,
			'firstname' : firstName,
			'lastname' : lastName
		}
		return render(request,'buy/whatsnew.html', context)

class OrderedIndexView(View):
	def get(self,request):
		user = request.session['user']
		opordered = Buy.objects.filter(customerID_id=user)
		qsproducts = Product.objects.all()
		qsimages = []

		for product in opordered:
			image = ProductImages.objects.filter(product_id=product.productID_id)
			qsimages.append(image[0].image1)

		xlist = zip(opordered,qsimages)
		context = {
			'orderedprod' : xlist,
			'products': qsproducts,
			'user' : user,
		}

		return render(request,'buy/ordersummary.html', context)
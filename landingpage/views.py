from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from customer.models import *

class LandingPageIndexView(View):
	def get(self,request):
		args = {
			'user' : ""
		}
		return render(request,'landingpage/landingpage.html', args)

	def post(self,request):
		if request.method == "POST":
			email = request.POST.get("email")
			password = request.POST.get("password")
			auser = Customer.objects.filter(email = email)
			if not auser:
				return HttpResponse("Email not found.")
			else:
				if(auser[0].password == password):
					args = {
						'user' : auser[0].id,
						'firstname' : auser[0].firstName,
						'lastname' : auser[0].lastName
					}
					return render(request,'landingpage/landingpage.html',args)
				else:
					return HttpResponse("Incorrect password.")

class CategoriesIndexView(View):
	def get(self,request):
		return render(request,'landingpage/categories.html')
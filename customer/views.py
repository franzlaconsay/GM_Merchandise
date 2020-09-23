from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .forms import CustomerForm
from .models import *

class SummaryView(View):
  def get(self,request):
    qsCustomers = Customer.objects.all()
    context = {
      'customers' : qsCustomers
    }
    return render(request, 'customer/customerSummary.html', context)

class RegistrationView(View):
  def get(self,request):
    return render(request, 'customer/customerRegistration.html')

  def post(self,request):
    form = CustomerForm(request.POST, request.FILES)
    firstName = request.POST.get("firstName")
    middleName = request.POST.get("middleName")
    lastName = request.POST.get("lastName")
    street = request.POST.get("street")
    barangay = request.POST.get("barangay")
    city = request.POST.get("city")
    province = request.POST.get("province")
    zipCode = request.POST.get("zipCode")
    country = request.POST.get("country")
    birthdate = request.POST.get("birthdate")
    status = request.POST.get("status")
    gender = request.POST.get("gender")
    spouseName = request.POST.get("spouseName")
    spouseOccupation = request.POST.get("spouseOccupation")
    childrenNum = request.POST.get("childrenNum")
    motherName = request.POST.get("motherName")
    motherOccupation = request.POST.get("motherOccupation")
    fatherName = request.POST.get("fatherName")
    fatherOccupation = request.POST.get("fatherOccupation")
    height = request.POST.get("height")
    weight = request.POST.get("weight")
    religion = request.POST.get("religion")
    profilePic = request.FILES.get("profilePic")
    print(profilePic)
    form = Customer(firstName = firstName, middleName = middleName, lastName = lastName,
                    street = street, barangay = barangay, city = city,
                    province = province, zipCode = zipCode, country = country,
                    birthdate = birthdate, status = status, gender = gender,
                    spouseName = spouseName, spouseOccupation = spouseOccupation, childrenNum = childrenNum,
                    motherName = motherName, motherOccupation = motherOccupation,
                    fatherName  = fatherName, fatherOccupation = fatherOccupation,
                    height = height, weight = weight, religion = religion, profilePic = profilePic)
    form.save()
    return render(request, 'customer/customerSummary.html')
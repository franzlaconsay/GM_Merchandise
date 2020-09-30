from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CustomerForm
from .models import *
from django.conf import settings
from django.conf.urls.static import static
import os

class SummaryView(View):
  def get(self,request):
    qsCustomers = Customer.objects.all()
    context = {
      'customers' : qsCustomers
    }
    return render(request, 'customer/customerSummary.html', context)

  def post(self,request):
    if request.method == "POST":
      if 'btnUpdate' in request.POST:
        customerID = request.POST.get("customerID")
        oldProfile = request.POST.get("oldProfile")
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
        gender = request.POST.get("gender-"+customerID)
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
        Customer.objects.filter(person_ptr_id = customerID).update(firstName = firstName, middleName = middleName, lastName = lastName,
                    street = street, barangay = barangay, city = city,
                    province = province, zipCode = zipCode, country = country,
                    birthdate = birthdate, status = status, gender = gender,
                    spouseName = spouseName, spouseOccupation = spouseOccupation, childrenNum = childrenNum,
                    motherName = motherName, motherOccupation = motherOccupation,
                    fatherName  = fatherName, fatherOccupation = fatherOccupation,
                    height = height, weight = weight, religion = religion)
        if profilePic is not None:
          os.remove(settings.MEDIA_ROOT+"/"+oldProfile)
          update_customerPic = Customer.objects.get(person_ptr_id = customerID)
          update_customerPic.profilePic = profilePic
          update_customerPic.save()
      elif 'btnDelete' in request.POST:
        customerID = request.POST.get("customerID")
        oldProfile = request.POST.get("oldProfile")
        os.remove(settings.MEDIA_ROOT+"/"+oldProfile)
        Customer.objects.filter(person_ptr_id = customerID).delete()
        Person.objects.filter(id = customerID).delete()
      return HttpResponseRedirect('summary')

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
    if(profilePic is None):
      profilePic="avatar.png"
    form = Customer(firstName = firstName, middleName = middleName, lastName = lastName,
                    street = street, barangay = barangay, city = city,
                    province = province, zipCode = zipCode, country = country,
                    birthdate = birthdate, status = status, gender = gender,
                    spouseName = spouseName, spouseOccupation = spouseOccupation, childrenNum = childrenNum,
                    motherName = motherName, motherOccupation = motherOccupation,
                    fatherName  = fatherName, fatherOccupation = fatherOccupation,
                    height = height, weight = weight, religion = religion, profilePic = profilePic)
    form.save()
    #return render(request, 'customer/customerSummary.html')
    return HttpResponseRedirect('summary')
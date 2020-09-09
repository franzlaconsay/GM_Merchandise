from django.shortcuts import render
from django.views.generic import View, TemplateView

class CustomerSummaryView(View):
  def get(self,request):
    return render(request, 'customer/customerSummary.html')

class CustomerRegistrationView(View):
  def get(self,request):
    return render(request, 'customer/customerRegistration.html')
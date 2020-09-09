from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('customerSummary', views.CustomerSummaryView.as_view(), name = "customerSummary_view"),
    path('customerRegistration', views.CustomerRegistrationView.as_view(), name = "customerRegistration_view"),
]
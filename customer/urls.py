from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('summary', views.SummaryView.as_view(), name = "summary_view"),
    path('registration', views.RegistrationView.as_view(), name = "registration_view"),
]
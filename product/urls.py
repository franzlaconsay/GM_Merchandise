from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
	path('summary', views.ProductIndexView.as_view(), name="product_summary_view"),
	path('registration', views.ProductRegistrationView.as_view(), name="product_registration_view")
]
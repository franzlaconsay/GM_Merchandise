from django.urls import path
from . import views

app_name = 'landingpage'
urlpatterns = [
	path('index', views.LandingPageIndexView.as_view(), name="landingpage_index_view"),
	path('category', views.CategoriesIndexView.as_view(), name="categories_category_view"),
]
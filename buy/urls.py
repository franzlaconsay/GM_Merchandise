from django.urls import path
from . import views

app_name = 'buy'
urlpatterns = [
	path('category', views.CategoriesIndexView.as_view(), name="categories_category_view"),
	path('cart', views.CartIndexView.as_view(), name="cart_cart_view"),
	path('whatsnew', views.WhatsNewIndexView.as_view(), name="whatsnew_whatsnew_view"),
	path('ordersummary', views.OrderedIndexView.as_view(), name="ordered_ordersummary_view"),
]
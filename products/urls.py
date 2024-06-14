
from django.urls import path
from . import views
from .views import add_product, all_products, product_detail


urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
]
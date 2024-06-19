from django.urls import path
from . import views
from .views import add_product, all_products, product_detail, delete_product


urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:product_id>/', views.product_detail,
         name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/<int:pk>/delete/', views.delete_product,
         name='delete_product'),
    path('products/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('remove_from_bag/<int:product_id>/', views.remove_from_bag,
         name='remove_from_bag'),
]

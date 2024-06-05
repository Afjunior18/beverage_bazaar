from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/reviews/', views.product_review, name='product_review'),
]
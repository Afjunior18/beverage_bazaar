from django.urls import path
from .views import supplier_application_view, supplier_application_success_view

urlpatterns = [
    path('apply/', supplier_application_view, name='supplier_application'),
    path('apply/success/', supplier_application_success_view, name='supplier_application_success'),
]
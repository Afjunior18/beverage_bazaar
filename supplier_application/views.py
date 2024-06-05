from django.shortcuts import render, redirect
from .forms import SupplierApplicationForm

def supplier_application_view(request):
    if request.method == 'POST':
        form = SupplierApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_application_success')
    else:
        form = SupplierApplicationForm()
    
    return render(request, 'supplier_application/supplier_application_form.html', {'form': form})

def supplier_application_success_view(request):
    return render(request, 'supplier_application/supplier_application_success.html')
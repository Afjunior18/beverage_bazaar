from django.shortcuts import render, redirect
from .forms import SupplierApplicationForm


def supplier_application_view(request):
    """
    Handle the supplier application form submission.
    If the request method is POST, validate and save the form data.
    Redirect to the success page upon successful submission.
    Otherwise, render the empty supplier application form.
    """
    if request.method == 'POST':
        form = SupplierApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_application_success')
    else:
        form = SupplierApplicationForm()

    return render(request,
                  'supplier_application/supplier_application_form.html',
                  {'form': form})


def supplier_application_success_view(request):
    """
    Render the supplier application success page.
    """
    return render(request,
                  'supplier_application/supplier_application_success.html')

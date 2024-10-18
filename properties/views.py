from django.shortcuts import render, redirect, get_object_or_404
from .models import Owner, Tenant, Property, RentalContract, TenantDocument
from .forms import OwnerForm, TenantForm, PropertyForm, RentalContractForm, TenantDocumentForm
# Create your views here.

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})

def owner_creat(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm()
    return render(request, 'owner_creat.html', {'form': form})

def owner_update(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'owner_form.html', {'form': form})

def owner_delete(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        owner.delete()
        return redirect('owner_list')
    return render(request, 'owner_confirm_delete.html', {'owner': owner})

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

def tenant_create(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    return render(request, 'tenant_form.html', {'form': form})

def tenant_update(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenant_form.html', {'form': form})

def tenant_delete(request, pk):
    tenant = get_object_or_404(Tenant, pk=pk)
    if request.method == 'POST':
        tenant.delete()
        return redirect('tenant_list')
    return render(request, 'tenant_confirm_delete.html', {'tenant': tenant})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})

def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property_form.html', {'form': form})

def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('property_list')
    return render(request, 'property_confirm_delete.html', {'property': property})

def rental_contract_list(request):
    rental_contracts = RentalContract.objects.all()
    return render(request, 'rental_contract_list.html', {'rental_contracts': rental_contracts})

def rental_contract_create(request):
    if request.method == 'POST':
        form = RentalContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental_contract_list')
    else:
        form = RentalContractForm()
    return render(request, 'rental_contract_form.html', {'form': form})

def rental_contract_update(request, pk):
    rental_contract = get_object_or_404(RentalContract, pk=pk)
    if request.method == 'POST':
        form = RentalContractForm(request.POST, instance=rental_contract)
        if form.is_valid():
            form.save()
            return redirect('rental_contract_list')
    else:
        form = RentalContractForm(instance=rental_contract)
    return render(request, 'rental_contract_form.html', {'form': form})

def rental_contract_delete(request, pk):
    rental_contract = get_object_or_404(RentalContract, pk=pk)
    if request.method == 'POST':
        rental_contract.delete()
        return redirect('rental_contract_list')
    return render(request, 'rental_contract_confirm_delete.html', {'rental_contract': rental_contract})

def tenant_document_list(request):
    tenant_documents = TenantDocument.objects.all()
    return render(request, 'tenant_document_list.html', {'tenant_documents': tenant_documents})

def tenant_document_create(request):
    if request.method == 'POST':
        form = TenantDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_document_list')
    else:
        form = TenantDocumentForm()
    return render(request, 'tenant_document_form.html', {'form': form})

def tenant_document_update(request, pk):
    tenant_document = get_object_or_404(TenantDocument, pk=pk)
    if request.method == 'POST':
        form = TenantDocumentForm(request.POST, instance=tenant_document)
        if form.is_valid():
            form.save()
            return redirect('tenant_document_list')
    else:
        form = TenantDocumentForm(instance=tenant_document)
    return render(request, 'tenant_document_form.html', {'form': form})

def tenant_document_delete(request, pk):
    tenant_document = get_object_or_404(TenantDocument, pk=pk)
    if request.method == 'POST':
        tenant_document.delete()
        return redirect('tenant_document_list')
from django import forms
from .models import Owner, Tenant, Property, RentalContract, TenantDocument

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'address', 'phone', 'email']
        labels = {
             'name':'اسم المالك',
            'address':'العنوان',
            'phone':'رقم الهاتف',
            'email':'البريد الإلكتروني',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
        
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'document_type', 'document_number', 'address', 'phone', 'email', 'rental_start_date', 'rental_end_date']
        labels = {
            'name':'اسم المستأجر', 
            'document_type':'نوع الوثيقة', 
            'document_number':'رقم الوثيقة',
            'address': 'العنوان',
            'phone':'رقم الهاتف', 
            'email':'البريد الإلكتروني', 
            'rental_start_date':'تاريخ بدء الإيجار', 
            'rental_end_date':'تاريخ انتهاء الإيجار',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}), 
            'document_type': forms.Select(attrs={'class':'form-control'}),
            'document_number': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control', 'rows':3}), 
            'phone': forms.TextInput(attrs={'class':'form-control'}), 
            'email': forms.EmailInput(attrs={'class':'form-control'}), 
            'rental_start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}), 
            'rental_end_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_type', 'address', 'owner', 'price', 'rooms', 'floor', 'available', 'description']
        labels = {
            'property_type':'نوع العقار',
            'address':'العنوان',
            'owner':'المالك',
            'price':'السعر',
            'rooms':'عدد الغرف',
            'floor':'الطابق',
            'available':'هل العقار متاح؟',
            'description':'وصف العقار',
        }
        widgets = {
            'property_type': forms.Select(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'owner': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'rooms': forms.NumberInput(attrs={'class':'form-control'}),
            'floor': forms.NumberInput(attrs={'class':'form-control'}),
            'available': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':4}),
        }

class RentalContractForm(forms.ModelForm):
    class Meta:
        model = RentalContract
        fields = ['property', 'tenant', 'start_date', 'end_date']
        labels = {
            'property':'العقار',
            'tenant':'المستأجر',
            'start_date':'تاريخ بدء الإيجار',
            'end_date':'تاريخ انتهاء الإيجار'
        }
        widgets = {
            'property': forms.Select(attrs={'class':'form-control'}),
            'tenant': forms.Select(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

class TenantDocumentForm(forms.ModelForm):
    class Meta:
        model = TenantDocument
        fields = ['tenant', 'document_type', 'document_file']
        labels = {
            'tenant':'المستأجر',
            'document_type':'نوع الوثيقة',
            'document_number':'رقم الوثيقة',
            'document_file':'ملف الوثيقة',
        }
        widgets = {
            'tenant': forms.Select(attrs={'class':'form-control'}),
            'document_type': forms.TextInput(attrs={'class':'form-control'}),
            'document_file': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
        }
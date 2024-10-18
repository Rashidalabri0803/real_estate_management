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
            'email': forms.EmailField(attrs={'class':'form-control'}),
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
            'address': forms.Textarea(attrs={'class':'form-control', 'rows':3}) 
            'phone': forms.TextInput(attrs={'class':'form-control'}), 
            'email': forms.EmailField(attrs={'class':'form-control'}), 
            'rental_start_date': forms.DateInput(attrs={'class':'form-control', 'type', 'date'}), 
            'rental_end_date': forms.DateInput(attrs={'class':'form-control', 'type', 'date'}),
        }
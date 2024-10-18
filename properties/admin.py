from django.contrib import admin
from .models import Owner, Tenant, Property, RentalContract, TenantDocument
# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'document_type', 'document_number', 'phone', 'email')
    search_fields = ('name', 'document_number', 'phone', 'email')
    list_filter = ('document_type',)
    
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'address', 'owner', 'price', 'available')
    search_fields = ('address', 'owner__name')
    list_filter = ('property_type', 'available')
    
@admin.register(RentalContract)
class RentalContractAdmin(admin.ModelAdmin):
    list_display = ('property', 'tenant', 'start_date', 'end_date')
    search_fields = ('property__address', 'tenant__name')
    list_filter = ('start_date', 'end_date')
    
@admin.register(TenantDocument)
class TenantDocumentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'document_type', 'document_file')
    search_fields = ('tenant__name', 'document_type')
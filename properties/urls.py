from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/new/', views.owner_create, name='owner_create'),
    path('owners/<int:pk>/edit/', views.owner_update, name='owner_update')
    path('owners/<int:pk>/delete/', views.owner_delete, name='owner_delete'),

    path('tenants/', views.tenant_list, name='tenant_list'),
    path('tenants/new/', views.tenant_create, name='tenant_create'),
    path('tenants/<int:pk>/edit/', views.tenant_update, name='tenant_update')
    path('tenants/<int:pk>/delete/', views.tenant_delete, name='tenant_delete'),

    path('properties/', views.property_list, name='property_list'),
    path('properties/new/', views.property_create, name='property_create'),
    path('properties/<int:pk>/edit/', views.property_update, name='property_update')
    path('properties/<int:pk>/delete/', views.property_delete, name='property_delete'),

    path('contracts/', views.rental_contract_list, name='rental_contract_list'),
    path('contracts/new/', views.rental_contract_create, name='rental_contract_create'),
    path('contracts/<int:pk>/edit/', views.rental_contract_update, name='rental_contract_update'),
    path('contracts/<int:pk>/delete/', views.rental_contract_delete, name='rental_contract_delete'),

    path('documents/', views.tenant_document_list, name='tenant_document_list'),
    path('documents/new/', views.tenant_document_create, name='tenant_document_create'),
    path('documents/<int:pk>/edit/', views.tenant_document_update, name='tenant_document_update'),
    path('documents/<int:pk>/delete/', views.tenant_document_delete, name='tenant_document_delete'),
]
from django.urls import path
from .views import ServiceListView, ServiceDetailView, BillDetailView
from django.views.generic.base import RedirectView


app_name = 'bills'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='bills:services_index'), name='index'),
    path('services', ServiceListView.as_view(), name='services_index'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='services_view'),
    path('bills/<int:pk>/', BillDetailView.as_view(), name='bills_view'),
]
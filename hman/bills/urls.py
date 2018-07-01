from django.urls import path
from .views import ServiceListView, ServiceDetailView, BillDetailView
from django.views.generic.base import RedirectView


app_name = 'bills'

urlpatterns = [
    path('', ServiceListView.as_view(), name='services_index'),
    path('<uuid:pk>/', ServiceDetailView.as_view(), name='services_view'),
    path('bill/<uuid:pk>/', BillDetailView.as_view(), name='bills_view'),
]
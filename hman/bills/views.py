from hman.views import DetailView, ListView, UpdateView
from hman.mixins import PermissionRequiredMixin
from .models import Service, Bill


class ServiceListView(PermissionRequiredMixin, ListView):

    template_name = 'bills/services/index.html'
    permission_required = 'bills.can_view_services'

    def get_queryset(self):
        return Service.objects.all()


class ServiceDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'bills/services/view.html'
    permission_required = 'bills.can_view_services'
    model = Service


class BillDetailView(DetailView):
    template_name = 'bills/bills/view.html'
    model = Bill
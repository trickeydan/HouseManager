from django.views.generic import ListView, DetailView
from hman.mixins import PermissionRequiredMixin

from .models import Person


class PeopleListView(PermissionRequiredMixin, ListView):

    template_name = 'people/index.html'
    permission_required = 'people.can_list_others'

    def get_queryset(self):
        return Person.objects.all()


class PersonView(PermissionRequiredMixin, DetailView):
    template_name = 'people/view.html'
    permission_required = 'people.can_view_others'
    model = Person


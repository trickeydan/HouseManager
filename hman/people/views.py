from hman.views import DetailView, ListView, UpdateView
from hman.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView as DTemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class ProfileView(UpdateView):
    permission_required = 'people.can_edit_profile'
    template_name = 'people/profile.html'
    model = Person

    fields = ['display_name', 'phone_number', 'picture', 'gender', 'pronouns', 'bio']

    def get_object(self, queryset=None):
        return Person.get_from_user(self.request.user)


class SetupView(LoginRequiredMixin, DTemplateView):

    template_name = "people/setup.html"
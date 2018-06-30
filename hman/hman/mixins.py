from django.shortcuts import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin as DjangoPermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin as DjangoLoginRequiredMixin

from people.models import Person

class PermissionRequiredMixin(DjangoPermissionRequiredMixin):
    raise_exception = True
    permission_denied_message = 'You do not have permission to access that.'


class LoginRequiredMixin(DjangoLoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if Person.get_from_user(request.user) is None and request.user.is_authenticated:
            return redirect('people:setup')

        return response
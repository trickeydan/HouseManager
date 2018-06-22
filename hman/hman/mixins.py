from django.contrib.auth.mixins import PermissionRequiredMixin as DjangoPermissionRequiredMixin


class PermissionRequiredMixin(DjangoPermissionRequiredMixin):
    raise_exception = True
    permission_denied_message = 'You do not have permission to access that.'

from django.conf import settings
from people.models import Person


def house(request):
    return { 'house': settings.HOUSE}


def me(request):
    if request.user.is_authenticated:
        return {
            'me': Person.get_from_user(request.user)
        }
    return {}


from django.conf import settings


def house(request):
    return { 'house': settings.HOUSE}

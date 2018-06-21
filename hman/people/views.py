from django.views.generic import ListView
from .models import Person


class PeopleListView(ListView):

    template_name = 'people/list.html'

    def get_queryset(self):
        return Person.objects.all()

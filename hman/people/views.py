from django.views.generic import ListView, DetailView
from .models import Person


class PeopleListView(ListView):

    template_name = 'people/index.html'

    def get_queryset(self):
        return Person.objects.all()


class PersonView(DetailView):
    template_name = 'people/view.html'
    model = Person


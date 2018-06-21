from django.urls import path
from .views import PeopleListView


app_name = 'people'

urlpatterns = [
    path('', PeopleListView.as_view(), name='index'),
]
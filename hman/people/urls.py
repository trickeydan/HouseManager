from django.urls import path
from .views import PeopleListView, PersonView


app_name = 'people'

urlpatterns = [
    path('', PeopleListView.as_view(), name='index'),
    path('<int:pk>/', PersonView.as_view(), name='view')
]
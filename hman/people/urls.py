from django.urls import path
from .views import PeopleListView, PersonView, ProfileView


app_name = 'people'

urlpatterns = [
    path('', PeopleListView.as_view(), name='index'),
    path('profile', ProfileView.as_view(success_url=''), name='profile'),
    path('view/<int:pk>/', PersonView.as_view(), name='view')
]
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView as DjangoTemplateView
from django.views.generic import ListView as DjangoListView
from django.views.generic import DetailView as DjangoDetailView
from django.views.generic import UpdateView as DjangoUpdateView


class TemplateView(LoginRequiredMixin, DjangoTemplateView):
    pass


class ListView(LoginRequiredMixin, DjangoListView):
    pass


class DetailView(LoginRequiredMixin, DjangoDetailView):
    pass


class UpdateView(LoginRequiredMixin, DjangoUpdateView):
    pass

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Thing


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Thing
    context_object_name = "things"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Thing


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Thing
    fields = ["title", "description", "purchaser"]


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Thing
    success_url = reverse_lazy("snack_list")


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Thing
    fields = "__all__"

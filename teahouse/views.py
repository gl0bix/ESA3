from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from teahouse.models import Tea


class TeaList(ListView):
    model = Tea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Tees"

        return context
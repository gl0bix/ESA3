from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, UpdateView

from teahouse.models import Tea, Preperation


def home(request):
    context = {'page_title': 'Welcome to the teahouse'}
    return render(request, 'teahouse/teahouse.html', context)


class TeaList(ListView):
    model = Tea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Teas'
        return context


class TeaUpdate(UpdateView):
    model = Tea
    fields = [
        "name",
        "category",
        "cultivar",
        "origin",
        "harvested",
    ]
    success_url = "/"


def show_prep(request, pk_id):
    preperation = Preperation.objects.get(pk=pk_id)
    page_title = 'Preperation'
    context = {'preperation': preperation,
               'page_title': page_title}
    return render(request, 'teahouse/preperation_card.html', context)

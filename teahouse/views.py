from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from teahouse.models import Tea, Preperation


class TeaList(ListView):
    model = Tea

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Teas'
        return context


def show_prep(request, pk_id):
    preperation = Preperation.objects.get(pk=pk_id)
    page_title = 'Preperation'
    context = {'preperation': preperation,
               'page_title': page_title}
    return render(request, 'teahouse/preperation_card.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from bboard.forms import BbForm
from bboard.models import Bb, Rubric
from django.template import loader
from django.views.generic.edit import CreateView


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric
    }
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name= 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

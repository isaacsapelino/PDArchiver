from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Thesis

# Create your views here.

@method_decorator(login_required, name='dispatch')
class homePage(ListView):
    model = Thesis
    queryset = Thesis.objects.all()
    context_object_name = 'theses'
    template_name='home.html'

@method_decorator(login_required, name='dispatch')
class searchContextPage(DetailView):
    model = Thesis

    def get_queryset(self):
        return Thesis.objects.all()

    def get(self, request, *args, **kwargs):
        context={}
        return render(request, template_name='home.html', context=context)

@method_decorator(login_required, name='dispatch')
class uploadPage(DetailView):

    def get(self, request, *args, **kwargs):
        context={}
        return render(request, template_name='upload.html', context=context)
        


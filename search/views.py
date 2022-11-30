from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.utils import timezone
import math
import json
import datetime

from .form import searchForm

from .models import Thesis

# Create your views here.

@method_decorator(login_required, name='dispatch')
class homePage(ListView):
    model = Thesis
    queryset = Thesis.objects.all()
    
    form_class = searchForm

    def get(self, request, *args, **kwargs):
        context = {
            'form' : self.form_class,
            'theses' : Thesis.objects.all(),
        }

        return render(request, template_name='home.html', context=context)

    def post(self, request, *args, **kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form_field = request.POST
            thesis_query = Thesis.objects.filter(title__icontains=form_field['thesis'])

            if len(thesis_query) > 0 and len(form_field) > 0:
                data = []
                for pos in thesis_query:
                    item = {
                        'id' : pos.id,
                        'title' : pos.title,
                        'abstract' : pos.abstract,
                        'authors' : [res.as_dict() for res in pos.authors.all()],
                        'whenpublished' : pos.whenpublished(),
                    }
                    data.append(item)
                res = data
            else:
                res = 'No result found.'
            return JsonResponse({'data' : res}, status=200)
        return JsonResponse({}, status=400)

@method_decorator(login_required, name='dispatch')
class searchContextPage(ListView):
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
        


from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
import math
import json
import datetime

from .form import searchForm, uploadThesisForm

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
                        'tags' : [str(res) for res in pos.tags.all()],
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

    tag_list = []

    form = uploadThesisForm

    def get(self, request, *args, **kwargs):
        context={
            'form' : self.form,
        }
        return render(request, template_name='upload.html', context=context)

    def post(self,request,*args, **kwargs):
        form = uploadThesisForm(request.POST, request.FILES)
        
        if form.is_valid():            
            instance = form.save(commit=False)
            instance.uploader = request.user
            instance.save()
            authors = form.cleaned_data['authors']
            tags = form.cleaned_data['tags']          

            for author in authors:
                instance.authors.add(author)            

            instance.tags.clear()

            chars_to_remove = [',',':','[','{',']','}','value']

            temp_tags = ' '.join(tags)

            for i in chars_to_remove:
                temp_tags = temp_tags.replace(i, '')
            
            tags = temp_tags.split()

            print(tags)

            for value in tags:
                print(value)
                instance.tags.add(value)
                    
            instance.save()
            
        else:
            form = uploadThesisForm()
            print('Failed')
 
        context = {
            'form' : self.form,
        }
        return render(request, template_name='upload.html', context=context)

        


        


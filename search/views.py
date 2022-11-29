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
            print(request.POST['thesis'])
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
            

    """   def datetime_handler(self, date):
        if isinstance(date, datetime.datetime):
            now = timezone.now()
            diff = now - date
            if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
                seconds= diff.seconds
                
                if seconds == 1:
                    return str(seconds) +  "second ago"
                
                else:
                    return str(seconds) + " seconds ago"

            if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
                minutes= math.floor(diff.seconds/60)

                if minutes == 1:
                    return str(minutes) + " minute ago"
                
                else:
                    return str(minutes) + " minutes ago"



            if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
                hours= math.floor(diff.seconds/3600)

                if hours == 1:
                    return str(hours) + " hour ago"

                else:
                    return str(hours) + " hours ago"

            # 1 day to 30 days
            if diff.days >= 1 and diff.days < 30:
                days= diff.days
            
                if days == 1:
                    return str(days) + " day ago"

                else:
                    return str(days) + " days ago"

            if diff.days >= 30 and diff.days < 365:
                months= math.floor(diff.days/30)
                

                if months == 1:
                    return str(months) + " month ago"

                else:
                    return str(months) + " months ago"


            if diff.days >= 365:
                years= math.floor(diff.days/365)

                if years == 1:
                    return str(years) + " year ago"

                else:
                    return str(years) + " years ago"
            return date.__str__()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Thesis.objects.values()), default=self.datetime_handler)
        return context """


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
        


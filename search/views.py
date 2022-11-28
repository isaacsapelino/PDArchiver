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

from .models import Thesis

# Create your views here.

@method_decorator(login_required, name='dispatch')
class homePage(ListView):
    model = Thesis
    queryset = Thesis.objects.all()
    context_object_name = 'theses'
    
    template_name='home.html'

    def datetime_handler(self, date):
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
        return context

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
        


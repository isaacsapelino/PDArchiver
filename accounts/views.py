from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import PDFBaseUser
from .form import RegisterForm
# Create your views here.

class loginPage(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('search:home')
        else:
            context = {}
            return render(request, template_name='loginPage.html', context=context)

    def post(self, request, *args, **kwargs):
        userId = request.POST.get('userId')
        password = request.POST.get('password')
        studentNumber = request.POST.get('studentNumber')
        print(request.POST.get('studentNumber'))

        user = authenticate(request, userId=userId, password=password)
        if user is not None:
            login(request, user)
            return redirect('/search/home')
        else:
            print('User is incorrect')
        context={}
        return render(request, template_name='loginPage.html', context=context)


class registerPage(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        
        context = {
            'form' : form,
        }

        return render(request, template_name='registerPage.html', context=context)
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            studentNumber = form.cleaned_data['studentNumber']

            return redirect('login')

        context = {
            'form' : form
        }

        return render(request, template_name='registerPage.html', context=context)

@login_required(login_url='/')
def logoutUser(request):
    logout(request)
    return redirect('/')






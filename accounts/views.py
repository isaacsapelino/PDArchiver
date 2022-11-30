from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import PDFBaseUser
from .form import RegisterForm,LoginForm
# Create your views here.

class loginPage(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        if request.user.is_authenticated:
            return redirect('search:home')
        else:
            context = {
                'form' : form,
            }
            return render(request, template_name='loginPage.html', context=context)

    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST)

        if form.is_valid():
            userId = form.cleaned_data['userId']
            studentNumber = form.cleaned_data['studentNumber']
            password = form.cleaned_data['password']
            user = authenticate(request, username=userId, password=password)
        else:
            userId = form.cleaned_data['userId']
            password = form.cleaned_data['password']
            user = authenticate(request, username=userId, password=password)
            

        if user is not None:
            login(request, user)
            return redirect('/search/home')
        else:
            messages.error(request, "Incorrect User ID or Password, please try again.")
            print('User is incorrect')
        context={
            'form' : form,
        }
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
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            studentNumber = form.cleaned_data['studentNumber']

            try:
                user = form.save()
                messages.success(request, "Account has been created!")
                return redirect('login')
            except:
                messages.error(request, "User already exists")
                return redirect('login')
            
        context = {
            'form' : form
        }

        return render(request, template_name='registerPage.html', context=context)

class profilePage(View):

    def get(self, request, *args, **kwargs):

        context = {
            
        }

        return render (request,template_name='profilePage.html', context=context)


@login_required(login_url='/')
def logoutUser(request):
    logout(request)
    return redirect('/')






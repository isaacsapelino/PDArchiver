from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PDFBaseUser

class LoginForm(forms.Form):
     studentNumber = forms.CharField(label='Student Number', max_length=255, widget=forms.TextInput(attrs={
        'class' : 'validate',
        'placeholder' : 'Student Number',
     }))

     userId = forms.CharField(label='User ID', max_length=255, widget=forms.TextInput(attrs={
        'class' : 'validate',
        'placeholder' : 'User ID',
     }))
     
     password= forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={
        'class' : 'validate',
        'placeholder' : 'Enter your password',
     }))
        


class RegisterForm(UserCreationForm):
    class Meta:
        model = PDFBaseUser
        fields = ['userId', 'firstName', 'middleName', 'lastName', 'email', 'studentNumber', 'password1', 'password2']
        widgets = {
            'firstName' : forms.TextInput(attrs={
                'placeholder' : 'Your first name',
            }),
            'middleName' : forms.TextInput(attrs={
                'placeholder' : 'Your middle name',
            }),
            'lastName' : forms.TextInput(attrs={
                'placeholder' : 'Your last name',
            }),
            'userId' : forms.TextInput(attrs={
                'placeholder' : 'Create your own username',
            }),
            'email' : forms.TextInput(attrs={
                'placeholder' : 'Enter your TIP email address',
            }),
            'studentNumber' : forms.TextInput(attrs={
                'placeholder' : 'Enter your TIP student number',
            }),
        }


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your password'})


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PDFBaseUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = PDFBaseUser
        fields = ['userId', 'firstName', 'lastName', 'email', 'studentNumber']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)


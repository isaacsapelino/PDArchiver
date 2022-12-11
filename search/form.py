from django import forms
from django.forms import ModelForm
from .models import Thesis
from accounts.models import PDFBaseUser
import datetime

class searchForm(forms.Form):
    searchField = forms.CharField(label='', required=False, max_length=255, widget=forms.TextInput(attrs={
        'class' : 'form-control me-2',
        'aria-label' : 'Search',
        'placeholder' : 'Find a document that you are looking for..',
    }))

class uploadThesisForm(ModelForm):
    title = forms.CharField(label='Project Design Title', required=True, max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control me-2',
        }))
    abstract = forms.CharField(label='Abstract', required=True, max_length=255, widget=forms.Textarea(attrs={
        'class': 'form-control me-2', }))
    authors = forms.ModelMultipleChoiceField(queryset=PDFBaseUser.objects.all())
    tags = forms.CharField(label="Tags", max_length=100, widget=forms.TextInput(attrs={
        'class' : 'form-control me-2',
        'spellcheck' : 'false',
    }))
    year = forms.DateField(initial=datetime.date.today)    
    document = forms.FileField()

    class Meta:
        model = Thesis
        fields = ['title', 'abstract', 'authors', 'year', 'document']
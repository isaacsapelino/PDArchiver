from django import forms
from .models import Thesis

class searchForm(forms.Form):
    searchField = forms.CharField(label='', required=False, max_length=255, widget=forms.TextInput(attrs={
        'class' : 'form-control me-2',
        'aria-label' : 'Search',
    }))
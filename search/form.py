from django import forms
from .models import Thesis

class PostForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = [
            'title',
            'abstract',
            'date_submitted',
            'tags',
        ]
from django.db.models.fields import CharField
from django.forms import widgets
from django.forms.fields import ImageField
from .models import post
from django import forms

class blog_form(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','content']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }
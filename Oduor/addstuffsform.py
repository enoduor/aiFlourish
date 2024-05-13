from django import forms
from .models import stuffs

class addStuffs(forms.Form):
    name_of_tool = forms.CharField(widget = forms.Textarea)
    description =  forms.CharField(widget = forms.Textarea)
    sign_up =  forms.CharField(widget = forms.Textarea)
    #ad =  forms.CharField(widget = forms.Textarea)
    website_link = forms.URLField(widget=forms.Textarea)
    youtube_link =  forms.CharField(widget = forms.Textarea)

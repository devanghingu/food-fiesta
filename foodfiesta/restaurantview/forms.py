from django import forms
from .models import Restaurant

class ResturantRemoveForm(forms.Form):
    ''' Resturant Remove Request Form '''
    reason = forms.CharField(max_length=25,widget=forms.Textarea())
  
   
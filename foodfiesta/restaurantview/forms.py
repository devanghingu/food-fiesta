from django import forms
from .models import Restaurant,Delivery
from accounts.models import User
from django.contrib.auth.forms  import UserCreationForm

class ResturantRemoveForm(forms.Form):
    ''' Resturant Remove Request Form '''
    reason = forms.CharField(max_length=25,widget=forms.Textarea())
  

class DeliveryPersonForm(UserCreationForm):
    ''' Create user for delivery person by restaurant Request Form '''

    class Meta:
        model   = User
        fields  = ('first_name','last_name','username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(DeliveryPersonForm, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None 


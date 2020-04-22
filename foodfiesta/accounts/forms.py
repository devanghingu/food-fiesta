from django.contrib.auth import get_user_model
from django import forms

USER_TYPE=(
    (False,'Customer'),
    (True,'Restaurant')
)

class SignupForm(forms.ModelForm):
    is_staff=forms.ChoiceField(choices=USER_TYPE)
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name','is_staff']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'is_staff':forms.Select(attrs={'class':'form-control'})
        }

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff=self.cleaned_data['is_staff']
        user.save()
from django import forms
from .models import *

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Description'}),
            'pic' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image Of Category'}),
        }

class FoodItemCreateForm(forms.ModelForm):
    class Meta:
        model = Fooditem
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'FoodItem Name'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FoodItem name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FoodItem Description'}),
            'pic' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image Of Fooditem'}),
        }
        
class CityCreateForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City Description'}),
        }

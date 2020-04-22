from django.contrib import admin

# Register your models here.
from .models import City, Category, Fooditem

admin.site.register(City)
admin.site.register(Category)
admin.site.register(Fooditem)
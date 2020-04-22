from django.contrib import admin

# Register your models here.
from cardview.models import Order

from cardview.models import Orderitem

admin.site.register(Order)
admin.site.register(Orderitem)
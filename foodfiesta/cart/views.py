from django.shortcuts import render
from django.views import View
# Create your views here.
class cart(View):
    def get(self,request,*args, **kwargs):
        return render(request,'frontend/user_cart.html')
    def post(self,request,*args, **kwargs):
        pass
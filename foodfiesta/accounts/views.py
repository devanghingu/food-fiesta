from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from allauth.account.views import SignupView,LoginView
from allauth.account.forms import SignupForm
from django.contrib.auth import logout,login
from django.contrib.auth.models import Group
from restaurantview.models import Restaurant
from django.urls import reverse_lazy
from . import forms
from django.views.generic import View
from django.contrib import messages
from adminview.models import City
from accounts.models import User


# Create your views here.
class Index(TemplateView):
    '''template for display when user come'''
    template_name="frontend/index.html"

# class JointSignupView(SignupView):
    
#     def __init__(self, **kwargs):
#         super(JointSignupView, self).__init__(*kwargs)        
    
#     def post(self,request,*args,**kwargs):
#         response=super().post(request,*args,**kwargs)
#         # new_group, created = Group.objects.get_or_create(name ='user_group')
#         # new_group.user_set.add(self.request.user)
#         # self.request.user.groups.add(new_group)

#         # if self.request.user://gone to user profile set login redirect url
#         #     logout(request)
#         #     return redirect('account_login')
#         return response

#     def get_context_data(self, **kwargs):
#         ret = super(JointSignupView, self).get_context_data(**kwargs)
#         # ret['signupform'] = get_form_class(app_settings.FORMS, 'signup', self.signup_form)
#         return ret

class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def post(self,request,*args,**kwargs):
        response=super().post(request,*args,**kwargs)
        if self.request.user.is_superuser:
            print('Supeeeeeeeeeeeeeeeeerrrrrrrrrrrrrr')
            return redirect('admin')
        elif self.request.user.is_staff:
            print('stafffffffffff')
            return redirect('accounts:index')
        return response

    # def get_context_data(self, **kwargs):
    #     context = super(LoginView, self).get_context_data(**kwargs)
    #     context.update({'signup_form': SignupForm})

    #     return context

class CreateRestaurant(View):
    def get(self,request,*args, **kwargs):
        form=forms.createrestaurant()
        context={}
        context={ 'form':form }
        return render(request,'frontend/createrestaurant.html',context)

    def post(self,request,*args, **kwargs):
        form=forms.createrestaurant(request.POST)
        if form.is_valid():
            data=request.POST.copy()
            city=City.objects.get(id=data['city'])
            name=form.cleaned_data.get('name')
            address=form.cleaned_data.get('address')
            contact=form.cleaned_data.get('contact')
            if Restaurant.objects.filter(name=name).exists():
                messages.info(request, "Restaurant is already Exist")
                return render(request,'frontend/createrestaurant.html',context={'form':form})
            else:
                Restaurant.objects.create(user=request.user,city=city,name=name,address=address,contact=contact)
                # new_group, created = Group.objects.get_or_create(name ='staff_group')
                # alice_group=User.groups.through.objects.get(user=self.request.user)
                # print(alice_group)
                # alice_group.group=new_group
                # alice_group.save()
                messages.success(request, "New Restaurant Added")
                return redirect("accounts:index")
        else:
            return render(request,'frontend/createrestaurant.html',context={'form':form})



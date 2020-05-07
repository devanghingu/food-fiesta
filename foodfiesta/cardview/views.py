import json

from adminview.models import City
from cart.models import Orderitem, Order
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views import View
from restaurantview.models import Restaurant


class RestaurantList(View):
    def get(self, request, *args, **kwargs):
        try:
            ordr = get_object_or_404(Order, user=request.user, status=0)
        except:
            ordr = None
        cartitem = Orderitem.objects.filter(order=ordr).order_by('id')
        res_list = Restaurant.objects.all()
        paginator = Paginator(res_list, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count = res_list.count()
        return render(request, 'frontend/cardview/restaurantlist.html',
                      {'page_obj': page_obj, 'count': count,
                       'cartitem': cartitem})

    def post(self, request):
        searchcity = request.POST.get('inputcity')
        searchres = request.POST.get('inputres')
        check_res = Restaurant.objects.all()
        if check_res.count() > 1:
            if searchcity and not searchres:
                searchinput = "'" + searchcity + "'"
                res_list = Restaurant.objects.filter(
                    city__name__icontains=searchcity.strip())
            elif searchres and not searchcity:
                searchinput = "'" + searchres + "'"
                res_list = Restaurant.objects.filter(
                    name__icontains=searchres.strip())
            elif searchres and searchcity:
                searchinput = "'" + searchcity + "'" + ' ' + "'" + searchres + "'"
                res_list = Restaurant.objects.filter(
                    name__icontains=searchres.strip(),
                    city__name__icontains=searchcity.strip())
            elif not searchres and not searchcity:
                searchinput = ''
                res_list = Restaurant.objects.all()
                count = res_list.count()
            else:
                searchinput = ''
                res_list = ""
            paginator = Paginator(res_list, 3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            count = res_list.count()
        else:
            messages.warning(request, 'No Restaurant found')

        return render(request, 'frontend/cardview/restaurantlist.html',
                      {'page_obj': page_obj, 'count': count,
                       'searchinput': searchinput})


def autocompletecity(request):
    """searchbar autocomplete"""
    if request.is_ajax():
        q = request.GET.get('term')
        search_qs = City.objects.filter(name__istartswith=q)
        print(search_qs)
        results = []
        for r in search_qs:
            results.append(r.name)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'adminview'

urlpatterns = [
    path('index/', views.home,name='adminview_home'),
    #Category
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/update',views.CategoryUpdate.as_view(),name='category_update'),
    path('category/<int:pk>/delete',views.CategoryDelete.as_view(),name='category_delete'),
    path('categorylist/',views.CategoryList.as_view(),name='allcategory'),
    path('category/create/',views.CategoryCreate.as_view(),name='category_create'),
    #FoodItem
    path('fooditem/<int:pk>/', views.FoodItemDetail.as_view(), name='fooditem_detail'),
    path('fooditem/<int:pk>/update',views.FoodItemUpdate.as_view(),name='fooditem_update'),
    path('fooditem/<int:pk>/delete',views.FoodItemDelete.as_view(),name='fooditem_delete'),
    path('fooditemlist/',views.FoodItemList.as_view(),name='allfooditem'),
    path('fooditem/create/',views.FoodItemCreate.as_view(),name='fooditem_create'),
]

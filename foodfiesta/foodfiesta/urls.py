from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from accounts.views import CustomLoginView


urlpatterns = [
    path('restaurant/',include('restaurantview.urls')),
    path('cart/',include('cart.urls')),
    path('adminview/',include('adminview.urls')),
    path('admin/', admin.site.urls),
    path("accounts/login/",CustomLoginView.as_view(), name="account_login"),
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

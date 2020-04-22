from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from foodfiesta import settings

urlpatterns = [
    path('', include('cart.urls')),
    path('restaurant/', include('restaurantview.urls')),
    path('admin/', admin.site.urls),
    path('cardview/', include('cardview.urls')),
    path('adminview/', include('adminview.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from accounts.views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path

urlpatterns = [
    path("cart/", include("cart.urls")),
    path("admin/", admin.site.urls),
    path("accounts/login/", CustomLoginView.as_view(), name="account_login"),
    path("accounts/", include("allauth.urls")),
    path("", include("accounts.urls")),
    path("cardview/", include("cardview.urls")),
    path("adminview/", include("adminview.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

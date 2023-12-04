from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from network.views import custom_404 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("network.urls")),
]

urlpatterns += [re_path(r'^.*$', custom_404)]  # Catch-all pattern for 404 errors


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

handler404 = "web.views.handler404"
handler500 = "web.views.handler500"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

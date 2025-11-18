from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conference/', include('conferenceApp.urls')),
    path('user/', include('userApp.urls')),
    path('submission/', include('submissionApp.urls')),
    path('api/', include('sessionAppApi.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

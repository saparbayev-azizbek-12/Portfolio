"""
Root URL configuration for config.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secure/admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('core.urls', namespace='core')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

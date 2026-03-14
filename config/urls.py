"""
Root URL configuration for config.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secure/part/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', include('core.urls', namespace='core')),
]

# Custom 404 handler
handler404 = 'django.views.defaults.page_not_found'

# Serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from config import settings

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('apps.course.urls')),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

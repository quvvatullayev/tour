from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Tour API",
        default_version='1.0.0',
        description="Test description",
    ),
    public=True,
)

urlpatterns = [
    path('', include('tour.urls')),
    path('admin/', admin.site.urls),
    path('api/vi/', include([
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Swagger va Redoc uchun schema-view sozlamalari
schema_view = get_schema_view(
    openapi.Info(
        title="AvtoLitsenziya Pro API",
        default_version='v1',
        description="API for managing vehicle licenses, vouchers, and inspections",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Asosiy admin sahifasi
    path('admin/', admin.site.urls),

    # API hujjatlashtirish manzillari
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API endpointlari
    path('api/auth/', include('accounts.urls')),
    path('api/user/', include('user.urls')),
    path('api/admin/', include('accounts.urls')),
]

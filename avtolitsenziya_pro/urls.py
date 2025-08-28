from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

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

@api_view(['GET'])
def api_root_view(request, format=None):
    """
    Bu view barcha API endpointlari ro'yxatini ko'rsatadi.
    """
    return Response({
        'auth_register': reverse('accounts:register', request=request, format=format),
        'auth_login': reverse('accounts:login', request=request, format=format),
        'admin_employees': reverse('accounts:employee-list', request=request, format=format),
        'admin_vehicles': reverse('accounts:vehicle-list', request=request, format=format),
        'admin_putyovkas': reverse('accounts:putyovka-list', request=request, format=format),
        'admin_inspections': reverse('accounts:inspection-list', request=request, format=format),
        'admin_payments': reverse('accounts:payment-list', request=request, format=format),
        'admin_companies': reverse('accounts:company-list', request=request, format=format),
        # 'user' endpointlari uchun sizga views/urls kerak bo'ladi
        # 'user_profile': reverse('user:profile', request=request, format=format),
        # 'user_putyovkas': reverse('user:putyovkas', request=request, format=format),
    })

urlpatterns = [
    # Asosiy admin sahifasi
    path('admin/', admin.site.urls),

    # API hujjatlashtirish manzillari
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API endpointlari
    path('api/', api_root_view, name='api-root'),
    path('api/accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('api/user/', include(('user.urls', 'user'), namespace='user')),
]

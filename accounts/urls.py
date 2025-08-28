from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
    RegisterView,
    LoginView,
    EmployeeAdminView,
    VehicleAdminView,
    PutyovkaAdminView,
    InspectionAdminView,
    PaymentAdminView,
    CompanyAdminView,
)

# Ilova nomi
app_name = 'accounts'

urlpatterns = [
    # Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    # Admin
    path('employees/', EmployeeAdminView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeAdminView.as_view(), name='employee-detail'),
    path('vehicles/', VehicleAdminView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', VehicleAdminView.as_view(), name='vehicle-detail'),
    path('putyovkas/', PutyovkaAdminView.as_view(), name='putyovka-list'),
    path('putyovkas/<int:pk>/', PutyovkaAdminView.as_view(), name='putyovka-detail'),
    path('inspections/', InspectionAdminView.as_view(), name='inspection-list'),
    path('inspections/<int:pk>/', InspectionAdminView.as_view(), name='inspection-detail'),
    path('payments/', PaymentAdminView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentAdminView.as_view(), name='payment-detail'),
    path('companies/', CompanyAdminView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyAdminView.as_view(), name='company-detail'),
]

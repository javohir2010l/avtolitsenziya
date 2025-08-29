from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
    RegisterView,
    LoginView,
    EmployeeListCreateAPIView,
    EmployeeRetrieveUpdateDestroyAPIView,
    VehicleListCreateAPIView,
    VehicleRetrieveUpdateDestroyAPIView,
    PutyovkaListCreateAPIView,
    PutyovkaRetrieveUpdateDestroyAPIView,
    InspectionListCreateAPIView,
    InspectionRetrieveUpdateDestroyAPIView,
    PaymentListCreateAPIView,
    PaymentRetrieveUpdateDestroyAPIView,
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateDestroyAPIView
)

# Ilova nomi
app_name = 'accounts'

urlpatterns = [
    # Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # Admin
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),
    path('vehicles/', VehicleListCreateAPIView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', VehicleRetrieveUpdateDestroyAPIView.as_view(), name='vehicle-detail'),
    path('putyovkas/', PutyovkaListCreateAPIView.as_view(), name='putyovka-list'),
    path('putyovkas/<int:pk>/', PutyovkaRetrieveUpdateDestroyAPIView.as_view(), name='putyovka-detail'),
    path('inspections/', InspectionListCreateAPIView.as_view(), name='inspection-list'),
    path('inspections/<int:pk>/', InspectionRetrieveUpdateDestroyAPIView.as_view(), name='inspection-detail'),
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view(), name='company-detail'),
]

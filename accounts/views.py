from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from .serializers import (
    EmployeeSerializer,
    CompanySerializer,
    VehicleSerializer,
    PutyovkaSerializer,
    InspectionSerializer,
    PaymentSerializer
)
from .models import (
    Employee,
    Company,
    Vehicle,
    Putyovka,
    Inspection,
    Payment
)

# Autentifikatsiya view'lari
class RegisterView(APIView):
    """
    Yangi xodimni ro'yxatdan o'tkazish.
    Faqat adminlar uchun ruxsat berilgan.
    """
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Tizimga kirish va JWT tokenlarini olish.
    """
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        employee = Employee.objects.filter(login=login).first()

        if employee and employee.check_password(password):
            refresh = RefreshToken.for_user(employee)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Admin Paneli uchun View`lar
# Barcha View'lar uchun IsAdminUser ruxsati qo'shilgan
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]

class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]

class VehicleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAdminUser]

class VehicleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAdminUser]

class PutyovkaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Putyovka.objects.all()
    serializer_class = PutyovkaSerializer
    permission_classes = [permissions.IsAdminUser]

class PutyovkaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Putyovka.objects.all()
    serializer_class = PutyovkaSerializer
    permission_classes = [permissions.IsAdminUser]

class InspectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
    permission_classes = [permissions.IsAdminUser]

class InspectionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
    permission_classes = [permissions.IsAdminUser]

class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]

class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]

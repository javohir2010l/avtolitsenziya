# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.tokens import RefreshToken
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
    permission_classes = [IsAuthenticated, IsAdminUser]

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


# Admin Paneli - Xodimlar boshqaruvi
class EmployeeAdminView(APIView):
    """
    Xodimlarni ko'rish, o'zgartirish va o'chirish uchun API endpoint.
    GET: Barcha xodimlar ro'yxati yoki bitta xodim ma'lumoti.
    PUT/PATCH: Xodim ma'lumotlarini yangilash.
    DELETE: Xodimni o'chirish.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Admin Paneli - Avtomobillar boshqaruvi
class VehicleAdminView(APIView):
    """
    Avtomobillarni boshqarish uchun API endpoint.
    GET: Barcha avtomobillar yoki bitta avtomobil ma'lumoti.
    POST: Yangi avtomobil yaratish.
    PUT/PATCH: Avtomobil ma'lumotlarini yangilash.
    DELETE: Avtomobilni o'chirish.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            vehicle = get_object_or_404(Vehicle, pk=pk)
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)
        
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Admin Paneli - Putyovkalar boshqaruvi
class PutyovkaAdminView(APIView):
    """
    Putyovkalarni boshqarish uchun API endpoint.
    GET, POST, PUT, DELETE metodlari mavjud.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            putyovka = get_object_or_404(Putyovka, pk=pk)
            serializer = PutyovkaSerializer(putyovka)
            return Response(serializer.data)
        
        putyovkas = Putyovka.objects.all()
        serializer = PutyovkaSerializer(putyovkas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PutyovkaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        putyovka = get_object_or_404(Putyovka, pk=pk)
        serializer = PutyovkaSerializer(putyovka, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        putyovka = get_object_or_404(Putyovka, pk=pk)
        putyovka.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Admin Paneli - Tekshiruvlar boshqaruvi
class InspectionAdminView(APIView):
    """
    Tekshiruvlarni boshqarish uchun API endpoint.
    GET, POST, PUT, DELETE metodlari mavjud.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            inspection = get_object_or_404(Inspection, pk=pk)
            serializer = InspectionSerializer(inspection)
            return Response(serializer.data)
        
        inspections = Inspection.objects.all()
        serializer = InspectionSerializer(inspections, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InspectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        inspection = get_object_or_404(Inspection, pk=pk)
        serializer = InspectionSerializer(inspection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inspection = get_object_or_404(Inspection, pk=pk)
        inspection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Admin Paneli - To'lovlar boshqaruvi
class PaymentAdminView(APIView):
    """
    To'lovlarni boshqarish uchun API endpoint.
    GET, POST, PUT, DELETE metodlari mavjud.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            payment = get_object_or_404(Payment, pk=pk)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data)
        
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Admin Paneli - Kompaniyalar boshqaruvi
class CompanyAdminView(APIView):
    """
    Kompaniyalarni boshqarish uchun API endpoint.
    GET, POST, PUT, DELETE metodlari mavjud.
    """
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            company = get_object_or_404(Company, pk=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

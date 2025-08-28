# user/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    EmployeeProfileSerializer,
    PutyovkaSerializer,
    InspectionSerializer,
    PaymentSerializer
)

class UserProfileView(APIView):
    """
    GET: Foydalanuvchi profilini ko'rish.
    PATCH: Profil ma'lumotlarini qisman yangilash.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = EmployeeProfileSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = EmployeeProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPutyovkasView(APIView):
    """
    GET: Foydalanuvchining putyovkalar ro'yxatini ko'rish.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        putyovkas = request.user.putyovkas.all()
        serializer = PutyovkaSerializer(putyovkas, many=True)
        return Response(serializer.data)

class UserInspectionsView(APIView):
    """
    GET: Foydalanuvchining tekshiruvlar ro'yxatini ko'rish.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        inspections = request.user.inspections.all()
        serializer = InspectionSerializer(inspections, many=True)
        return Response(serializer.data)

class UserPaymentsView(APIView):
    """
    GET: Foydalanuvchining to'lovlar tarixini ko'rish.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payments = request.user.payments.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
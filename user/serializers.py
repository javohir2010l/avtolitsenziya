# user/serializers.py
from rest_framework import serializers
from accounts.models import Employee, Putyovka, Inspection, Payment, Vehicle

class EmployeeProfileSerializer(serializers.ModelSerializer):
    """
    Foydalanuvchi o'z profil ma'lumotlarini ko'rishi va yangilashi uchun.
    """
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'phone', 'passport', 'e_imzo_key', 'login', 'role']
        read_only_fields = ['id', 'role', 'login'] # Bu maydonlar faqat o'qish uchun

class VehiclePutyovkaSerializer(serializers.ModelSerializer):
    """
    Putyovkada avtomobil ma'lumotlarini ko'rsatish uchun ichki seriyalizator.
    """
    class Meta:
        model = Vehicle
        fields = ['number', 'model']
        
class PutyovkaSerializer(serializers.ModelSerializer):
    """
    Foydalanuvchi putyovkalar ro'yxatini ko'rishi uchun.
    """
    vehicle = VehiclePutyovkaSerializer(read_only=True) # Avtomobil ma'lumotlari
    
    class Meta:
        model = Putyovka
        fields = ['id', 'start_date', 'end_date', 'qr_code', 'vehicle']

class InspectionSerializer(serializers.ModelSerializer):
    """
    Foydalanuvchi tekshiruvlar ro'yxatini ko'rishi uchun.
    """
    vehicle = VehiclePutyovkaSerializer(read_only=True)
    
    class Meta:
        model = Inspection
        fields = ['id', 'inspection_type', 'status', 'notes', 'created_at', 'vehicle']

class PaymentSerializer(serializers.ModelSerializer):
    """
    Foydalanuvchi to'lovlar tarixini ko'rishi uchun.
    """
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_type', 'payment_date', 'is_confirmed']
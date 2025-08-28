from rest_framework import serializers
from .models import Company, Employee, Vehicle, Putyovka, Inspection, Payment

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'inn', 'account_number', 'name']

class EmployeeSerializer(serializers.Serializer):
    """
    Bu seriyalizator admin paneli uchun maxsus.
    U yangi xodim yaratishda va mavjud xodimni boshqarishda ishlatiladi.
    ModelSerializer o'rniga ishlatilishining sababi password'ni
    qo'lda hashlab saqlashni ta'minlashdir.
    """
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    full_name = serializers.CharField(max_length=255)
    login = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    e_imzo_key = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    passport = serializers.CharField(max_length=9)
    phone = serializers.CharField(max_length=15)
    role = serializers.CharField(max_length=50)
    is_admin = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
        """
        Yangi xodimni yaratishda parol maydonini hashlaydi.
        """
        password = validated_data.pop('password')
        employee = Employee.objects.create_user(password=password, **validated_data)
        return employee

    def update(self, instance, validated_data):
        """
        Mavjud xodim ma'lumotlarini yangilash.
        Agar yangi parol berilgan bo'lsa, uni hashlaydi.
        """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class PutyovkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Putyovka
        fields = '__all__'

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

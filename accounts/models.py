from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Company(models.Model):
    inn = models.CharField(max_length=9, unique=True)
    account_number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EmployeeManager(BaseUserManager):
    def create_user(self, login, password, **extra_fields):
        if not login:
            raise ValueError('Login manzili majburiy')

        extra_fields.setdefault('is_active', True)
        
        employee = self.model(login=login, **extra_fields)
        employee.set_password(password)
        employee.save(using=self._db)
        return employee

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bo‘lishi kerak.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is_superuser=True bo‘lishi kerak.')

        return self.create_user(login, password, **extra_fields)

class Employee(AbstractBaseUser, PermissionsMixin):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    e_imzo_key = models.CharField(max_length=255, null=True, blank=True)
    passport = models.CharField(max_length=9)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = EmployeeManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['company', 'full_name', 'phone', 'passport']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_groups',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='employee',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='employee_permission',
    )

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
class Vehicle(models.Model):
    number = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    # Sizning loyihangizdagi boshqa maydonlar:
    # general_info = models.JSONField(null=True, blank=True)
    # cargo_info = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return self.number

class Putyovka(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='putyovkas')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    qr_code = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Putyovka for {self.employee.full_name}"

class Inspection(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='inspections')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    inspection_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inspection for {self.employee.full_name} ({self.inspection_type})"

class Payment(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='payments')
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=50)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Payment of {self.amount} by {self.employee.full_name}"
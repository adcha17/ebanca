from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


class Client(models.Model):

    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )

    DOCUMENT_CHOICES = (
        ('DNI', 'DNI'),
        # ('RUC', 'RUC'),
    )

    lastname = models.CharField(max_length=50)
    mothers_lastname = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    membership_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    document_type = models.CharField(
        max_length=3, choices=DOCUMENT_CHOICES, default='DNI')

    doc_num_validator = RegexValidator(r'^[0-9]{8,8}$',
                                       'DNI require 8 digitos.', 'Invalid number')

    document_number = models.CharField(max_length=8, validators=[
                                       doc_num_validator], unique=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.lastname, self.document_number)


class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_superuser, is_staff, **extra_fields):
        if not username:
            raise ValueError('El número de tarjeta es requerido.')

        # if not is_superuser:
        #     if extra_fields.get('client') == None:
        #         raise ValueError('El cliente es requerido.')

        user = self.model(username=username, is_superuser=is_superuser, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True)
    # recordar validar client null, blank
    client = models.ForeignKey(Client, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username


class CreditCard(models.Model):
    # revisar todo null, blank tiene que generarse automaticamente
    num_card = models.IntegerField(unique=True, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    num_cvv = models.IntegerField(null=True, blank=True)
    validity_status = models.BooleanField(default=True)
    blocking_status = models.BooleanField(default=False)
    num_pin = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s' % (self.num_card)


class Account(models.Model):

    CURRENCY_CHOICES = (
        ('S', 'SOLES'),
        ('D', 'DOLARES'),
        ('E', 'EUROS'),
    )
    # revisar todo null, blank tiene que generarse automaticamente
    num_account = models.CharField(
        max_length=14, unique=True, null=True, blank=True)
    client = models.ForeignKey(Client)
    card = models.ForeignKey(CreditCard)
    associated_currency = models.CharField(
        max_length=1, choices=CURRENCY_CHOICES)
    current_balance = models.DecimalField(
        decimal_places=4, max_digits=7, default=0)
    maintenance_cost = models.DecimalField(
        decimal_places=4, max_digits=7, default=0)
    cancellation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s' % (self.num_account)

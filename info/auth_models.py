from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, phone, password, **extra_fields):
        user = self.model(
            phone=phone,
            password=password,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields['is_staff']= True
        extra_fields['is_superuser'] = True
        extra_fields['user_type'] = 1
        return self.create_user(phone=phone, password=password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    fullname = models.CharField(max_length=56)
    phone = models.CharField(max_length=15, unique=True)
    age = models.PositiveSmallIntegerField(default=16)
    gender = models.BooleanField(default=True)
    user_type = models.BooleanField(default=2, choices=[
        (1, "Admin"),
        (2, "User")
    ])

    #majburiy polyalar
    is_active = models.BooleanField(default=True) #ban bo'lgan userlarni olmaydi faqat aktivlarni oladi
    is_superuser = models.BooleanField(default=False) #agar saytdan ro'yhatdan o'tsa superuser=false holatda kiradi.
    is_staff = models.BooleanField(default=False) #user xodim emasligi uchun tekshiriladi

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['age', 'user_type']
    USERNAME_FIELD = "phone"


class Otp(models.Model):     #OTP -> One Time Password
    phone = models.CharField(max_length=15)
    token = models.CharField(max_length=256)



    extra = models.JSONField(default=dict)
    by = models.SmallIntegerField(default=1, choices=[
        (1, "login"),
        (2, "regis")
    ])








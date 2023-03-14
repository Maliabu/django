from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):
    def create_user(self, email:str,phone:int,password:str=None, is_staff=False,is_superuser=False) -> "User":
        if not email:
            raise ValueError("users must have an email")
        if not phone:
            raise ValueError("users must have a phone number")
        
        user = self.model(email=self.normalize_email(email))
        user.phone = phone
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
    
    def create_superuser(self, email:str,phone:int,password:str=None, is_staff=False,is_superuser=False) -> "User":
        user = self.create_user(
            phone=phone,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user

class User(auth_models.AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    phone = models.BigIntegerField(verbose_name="phone")
    password=models.CharField(max_length=200)
    username=None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"] # Email & Password are required by default.
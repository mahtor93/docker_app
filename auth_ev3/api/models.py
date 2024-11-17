from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Crea y retorna un usuario con email y contraseña."""
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Crea y retorna un superusuario"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Aunque se maneja con set_password


    objects = UsuarioManager()

    USERNAME_FIELD = 'email'  # Utilizamos el email como nombre de usuario
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """User model"""

    username = None

    email = models.EmailField(unique=True, verbose_name="email")
    phone_number = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    is_seller = models.BooleanField(default="False", verbose_name="Продавец")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

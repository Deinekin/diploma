from decimal import Decimal

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Price(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE,
    )
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Стартовая цена"
    )
    goods = models.CharField(max_length=100, verbose_name="Товар", **NULLABLE)

    taxes = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("0.06"),
        verbose_name="Общие налоги",
    )
    bank_taxes = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("0.02"),
        verbose_name="Отчисления банку",
    )
    seller_taxes = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=Decimal("0.12"),
        verbose_name="Отчисления продавцу",
    )
    self_profit = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=Decimal("0.2"),
        verbose_name="Отчисления магазину",
    )
    total_price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Итоговая цена", **NULLABLE
    )

    def __str__(self):
        return f"{self.goods} - {self.total_price}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

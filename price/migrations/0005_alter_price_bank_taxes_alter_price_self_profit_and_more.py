# Generated by Django 5.0.7 on 2024-07-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("price", "0004_alter_price_bank_taxes_alter_price_self_profit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="bank_taxes",
            field=models.DecimalField(
                decimal_places=2,
                default=0.02,
                max_digits=6,
                verbose_name="Отчисления банку",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="self_profit",
            field=models.DecimalField(
                decimal_places=2,
                default=0.2,
                max_digits=7,
                verbose_name="Отчисления магазину",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="seller_taxes",
            field=models.DecimalField(
                decimal_places=2,
                default=0.12,
                max_digits=7,
                verbose_name="Отчисления продавцу",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="taxes",
            field=models.DecimalField(
                decimal_places=2,
                default=0.06,
                max_digits=6,
                verbose_name="Общие налоги",
            ),
        ),
    ]

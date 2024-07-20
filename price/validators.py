from rest_framework.exceptions import ValidationError


class PositivePriceValidator:
    """positive price validator"""

    def __init__(self, price):
        self.price = price

    def __call__(self, value):
        checked_price = dict(value).get(self.price)
        if float(checked_price) <= 0.0:
            raise ValidationError("Цена должна быть больше 0.0")

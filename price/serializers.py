from rest_framework.serializers import ModelSerializer

from price.models import Price
from price.validators import PositivePriceValidator


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = [
            "id",
            "user",
            "goods",
            "taxes",
            "bank_taxes",
            "seller_taxes",
            "self_profit",
            "price",
            "total_price",
        ]
        validators = [PositivePriceValidator(price="price")]

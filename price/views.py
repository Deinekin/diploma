from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from price.models import Price
from price.serializers import PriceSerializer
from users.permissions import IsOwner, IsSeller


class PriceCreateAPIView(CreateAPIView):
    """creating price and setting total_price"""

    serializer_class = PriceSerializer
    permission_classes = [IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        price_data = serializer.save(user=self.request.user)

        taxes = float(price_data.taxes)
        price = float(price_data.price)
        seller_taxes = float(price_data.seller_taxes)
        bank_taxes = float(price_data.bank_taxes)
        self_profit = float(price_data.self_profit)

        total_price = price + price * (taxes + seller_taxes + bank_taxes + self_profit)
        price_data.total_price = total_price

        price_data.save()


class PriceListAPIView(ListAPIView):
    """list of prices"""

    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsSeller]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Price.objects.all()
        return Price.objects.filter(user=user)


class PriceDetailAPIView(RetrieveAPIView):
    """detail of price"""

    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsSeller, IsOwner]


class PriceUpdateAPIView(UpdateAPIView):
    """update price"""

    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsSeller, IsOwner]


class PriceDestroyAPIView(DestroyAPIView):
    """delete price"""

    queryset = Price.objects.all()
    permission_classes = [IsAuthenticated, IsSeller, IsOwner]

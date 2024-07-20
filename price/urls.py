from django.urls import path

from price.apps import PriceConfig
from price.views import (
    PriceCreateAPIView,
    PriceDestroyAPIView,
    PriceDetailAPIView,
    PriceListAPIView,
    PriceUpdateAPIView,
)

app_name = PriceConfig.name

urlpatterns = [
    path("", PriceListAPIView.as_view(), name="prices"),
    path("create/", PriceCreateAPIView.as_view(), name="price_create"),
    path("detail/<int:pk>/", PriceDetailAPIView.as_view(), name="price_detail"),
    path("update/<int:pk>/", PriceUpdateAPIView.as_view(), name="price_update"),
    path("destroy/<int:pk>/", PriceDestroyAPIView.as_view(), name="price_delete"),
]

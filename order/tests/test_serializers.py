import pytest

from order.serializers import OrderSerializer
from order.factories import OrderFactory
from product.factories import ProductFactory


@pytest.mark.django_db
def test_order_serializer():
    product = ProductFactory(price=100)
    order = OrderFactory(product=[product])

    serializer = OrderSerializer(order)
    data = serializer.data

    assert data["total"] == 100
    assert len(data["product"]) == 1
    assert data["product"][0]["title"] == product.title
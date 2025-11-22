import pytest

from product.factories import ProductFactory
from order.factories import OrderFactory


@pytest.mark.django_db
def test_order_factory():
    product = ProductFactory()
    order = OrderFactory(product=[product])

    assert order.pk is not None
    assert order.product.count() == 1
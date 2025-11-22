import pytest

from django.contrib.auth.models import User

from order.models import Order
from product.factories import ProductFactory


@pytest.mark.django_db
def test_order_model():
    user = User.objects.create_user(username="Victor", password="123")
    product = ProductFactory()

    order = Order.objects.create(user=user)
    order.product.add(product)

    assert order.user.username == "Victor"
    assert order.product.count() == 1
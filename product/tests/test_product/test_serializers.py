import pytest

from product.factories import ProductFactory
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer():
    product = ProductFactory()
    serializer = ProductSerializer(product)
    data = serializer.data

    assert data["title"] == product.title
    assert data["price"] == product.price
    assert len(data["category"]) == product.category.count()
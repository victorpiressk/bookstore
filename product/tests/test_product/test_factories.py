import pytest

from product.factories import ProductFactory


@pytest.mark.django_db
def test_product_factory():
    product = ProductFactory()

    assert product.pk is not None
    assert isinstance(product.title, str)
    assert product.category.count() == 1
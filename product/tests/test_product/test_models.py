import pytest

from product.models import Product
from product.factories import CategoryFactory


@pytest.mark.django_db
def test_product_model():
    category = CategoryFactory()
    product = Product.objects.create(
        title="Notebook",
        description="Alta performance",
        price=3500,
        active=True,
    )
    product.category.add(category)

    assert product.title == "Notebook"
    assert product.price == 3500
    assert product.category.count() == 1
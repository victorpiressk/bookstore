import pytest

from product.models import Category


@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(
        title="Eletrônicos",
        slug="eletronicos",
        description="Itens digitais"
    )

    assert category.title == "Eletrônicos"
    assert category.slug == "eletronicos"
    assert category.description == "Itens digitais"
    assert category.active is True
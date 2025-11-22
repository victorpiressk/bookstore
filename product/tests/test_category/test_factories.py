import pytest

from product.factories import CategoryFactory


@pytest.mark.django_db
def test_category_factory():
    category = CategoryFactory()

    assert category.pk is not None
    assert isinstance(category.title, str)
    assert isinstance(category.slug, str)
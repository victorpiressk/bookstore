import pytest

from product.serializers import CategorySerializer
from product.factories import CategoryFactory


@pytest.mark.django_db
def test_category_serializer():
    category = CategoryFactory()

    serializer = CategorySerializer(category)
    data = serializer.data

    assert data["title"] == category.title
    assert data["slug"] == category.slug
    assert data["description"] == category.description
    assert data["active"] == category.active
import json

import factory
import pytest
from pytest_factoryboy import register

from main.models import Author


@register
class AuthorFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Sequence(lambda x: "login%s@mail.ru" % x)

    class Meta:
        model = Author


@pytest.mark.django_db
def test_200(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_model_fixture(client):
    AuthorFactory.create()
    AuthorFactory.create()
    AuthorFactory.create()

    response = client.get('/')
    assert response.status_code == 200

    data = json.loads(response.content)
    assert len(data['authors']) == 3

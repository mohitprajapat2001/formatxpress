from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.conf import settings
from utils.auth_service import AuthService

MODEL_NOT_FOUND = "Please set model attribute"
FACTORY_CLASS_NONE = "Please set factory_class attribute"
LIST_URL_NONE = "Please set list_url attribute"
DETAIL_URL_NONE = "Please set detail_url attribute"
SERIALIZER_CLASS_NONE = "Please set serializer_class attribute"


class BaseTest(TestCase):
    BASE_DIR = str(settings.BASE_DIR)


class TestModel(BaseTest):
    model = None
    factory_class = None

    def setUp(self):
        super().setUp()
        if self.model is None:
            raise ValueError(MODEL_NOT_FOUND)
        if self.factory_class is None:
            raise ValueError(FACTORY_CLASS_NONE)

    def factory_create(self, **kwargs):
        return self.factory_class.create(**kwargs)

    def factory_create_many(self, how_many: int = 10, **kwargs):
        return self.factory_class.create_batch(how_many, **kwargs)


class TestClientCRUD(TestModel):
    def setUp(self):
        if self.list_url is None:
            raise ValueError(LIST_URL_NONE)
        if self.detail_url is None:
            raise ValueError(DETAIL_URL_NONE)
        if self.serializer_class is None:
            raise ValueError(SERIALIZER_CLASS_NONE)
        self.client = APIClient()
        self.user = self.create_superuser()
        self.get_client_jwt()
        super().setUp()

    def create_superuser(self):
        return get_user_model().objects.create_superuser(
            username="testuser", password="password", email="testuser@testuser.com"
        )

    def get_client_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.get_jwt_token()}")

    def get_jwt_token(self):
        response = AuthService().get_auth_tokens_for_user(self.user)
        return response["access"]

    def get_serialized_data(self, instance):
        return self.serializer_class(instance).data

    def serializer_validation(self, response, instance):
        self.assertEqual(response.data, self.get_serialized_data(instance=instance))

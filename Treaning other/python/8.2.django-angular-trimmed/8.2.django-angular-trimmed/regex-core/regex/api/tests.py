from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import (
    APIClient,
    APITestCase,
)


class EntryTests(APITestCase):
    client = APIClient()
    username = 'admin'
    password = User.objects.make_random_password()
    token_key = None

    def setUp(self):
        user = User.objects.create_superuser(
            email='admin@admin.com',
            password=self.password,
            username=self.username,
        )
        self.token_key = Token.objects.create(user=user).key

    def test_read_all_entries(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(self.token_key),
        )
        response = self.client.get(reverse('api:entry-list'))
        response_obj = response.json()

        # TODO - Can also add in more relevant/functional asserts around updates
        # made against the DB, or JSON responses too.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_obj), 0)

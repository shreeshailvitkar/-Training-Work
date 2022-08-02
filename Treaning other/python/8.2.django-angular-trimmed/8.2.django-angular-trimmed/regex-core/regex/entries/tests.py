from django.contrib.auth.models import User
from django.test import (
    Client,
    TestCase,
)
from django.urls import reverse
from rest_framework import status


from entries.models import TestString


class TestStringModelTests(TestCase):
    def test_is_stringified_test_string_legible(self):
        test_string, is_test_string_created = TestString.objects.get_or_create(
            string='sample string'
        )

        self.assertEqual(str(test_string), test_string.string)


class TestStringAdminViewTests(TestCase):
    client = Client()
    username = 'admin'
    password = User.objects.make_random_password()

    def setUp(self):
        User.objects.create_superuser(
            email='admin@admin.com',
            password=self.password,
            username=self.username,
        )

        test_string, is_test_string_created = TestString.objects.get_or_create(
            string='sample string'
        )
        self.test_string_id = test_string.id

    def test_test_string_change_view_renders(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.get(reverse(
            'admin:entries_teststring_change',
            args=(self.test_string_id,),
        ))
        response_content = str(response.content)

        # TODO - Can also add in more relevant/functional asserts around updates
        # made against the DB, or HTML responses too.
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HomeViewTests(TestCase):
    client = Client()
    username = 'admin'
    password = User.objects.make_random_password()

    def setUp(self):
        User.objects.create_superuser(
            email='admin@admin.com',
            password=self.password,
            username=self.username,
        )

    def test_home_view_renders(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.get(reverse('entries:home'))
        response_content = str(response.content)

        # TODO - Can also add in more relevant/functional asserts around updates
        # made against the DB, or HTML responses too.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

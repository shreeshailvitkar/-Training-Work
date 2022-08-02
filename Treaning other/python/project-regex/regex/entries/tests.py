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



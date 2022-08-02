from django.contrib.auth.models import User
from rest_framework import serializers

from entries.models import (
    Entry,
    TestString,
)


class EntrySerializer(serializers.ModelSerializer):
    test_strings = serializers.SlugRelatedField(
        queryset=TestString.objects.all(),
        many=True,
        slug_field='string',
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = Entry
        fields = [
            'date_added',
            'id',
            'pattern',
            'test_strings',
            'user',
        ]

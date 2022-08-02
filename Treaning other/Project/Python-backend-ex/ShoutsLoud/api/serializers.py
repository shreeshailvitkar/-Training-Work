from rest_framework import serializers

from entries.models import UserData


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            'first_name',
            'id'
        ]

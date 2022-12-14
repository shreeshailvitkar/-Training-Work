from rest_framework import viewsets

from api.serializers import EntrySerializer
from entries.models import Entry


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('-date_added')
    serializer_class = EntrySerializer

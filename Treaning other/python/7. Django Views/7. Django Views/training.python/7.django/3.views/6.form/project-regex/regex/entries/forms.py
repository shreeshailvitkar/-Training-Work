from django.forms import ModelForm

from entries.models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = [
            'id',
            'pattern',
            'date_added',
        ]

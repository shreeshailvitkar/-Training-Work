from django.contrib import admin
from entries.models import (
    Entry,
    TestString,
    UserProfile,
)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        'test_strings',
        'user',
    ]
    list_display = [
        'pattern',
        'user',
    ]
    list_filter = ['user']
    search_fields = ['pattern']

@admin.register(TestString)
class TestStringAdmin(admin.ModelAdmin):
    list_display = ['string']
    search_fields = ['string']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname']
    list_filter = ['nickname']
    search_fields = ['nickname']

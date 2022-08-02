from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TestString(models.Model):
    string = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.string


class Entry(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    pattern = models.CharField(max_length=255)
    test_strings = models.ManyToManyField(TestString)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return str(self.id)


class UserProfile(models.Model):
    nickname = models.CharField(max_length=255)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{}-{}'.format(
            self.user.username,
            self.nickname,
        )

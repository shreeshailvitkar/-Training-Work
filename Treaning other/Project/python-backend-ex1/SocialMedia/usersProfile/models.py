from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user')
    name = models.CharField(max_length=255, null=True)
    lname = models.CharField(max_length=255, null=True)
    mobile = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    isactive = models.BooleanField(default=False)
    otp =  models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)


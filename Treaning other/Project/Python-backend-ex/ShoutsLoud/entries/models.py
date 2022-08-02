from django.db import models

# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.IntegerField()
    password = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    active_status = models.BooleanField()
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    
    def __str__(self):
        return str(self.id)
# authapi/models.py
from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.email

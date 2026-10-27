from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    years_of_experience = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

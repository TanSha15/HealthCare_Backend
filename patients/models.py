from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    medical_history = models.TextField(blank=True, default='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

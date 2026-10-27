from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    created_by_email = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Patient
        fields = [
            'id',
            'name',
            'age',
            'gender',
            'contact_number',
            'address',
            'medical_history',
            'created_by',
            'created_by_email',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_by_email', 'created_at', 'updated_at']

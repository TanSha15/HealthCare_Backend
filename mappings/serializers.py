from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_date']
        read_only_fields = ['id', 'assigned_date']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['patient_name'] = instance.patient.name
        data['doctor_name'] = instance.doctor.name
        data['doctor_details'] = DoctorSerializer(instance.doctor).data
        data['patient_details'] = PatientSerializer(instance.patient).data
        return data

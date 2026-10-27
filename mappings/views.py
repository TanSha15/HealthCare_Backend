from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from patients.models import Patient
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer

class MappingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if not Patient.objects.filter(pk=pk).exists():
            return Response({'detail': 'Patient not found.'}, status=status.HTTP_404_NOT_FOUND)
        mappings = PatientDoctorMapping.objects.filter(patient_id=pk)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        mapping = PatientDoctorMapping.objects.filter(pk=pk).first()
        if not mapping:
            return Response({'detail': 'Mapping not found.'}, status=status.HTTP_404_NOT_FOUND)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

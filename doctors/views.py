from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

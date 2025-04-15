from rest_framework import viewsets
from .models import AboutUs, VisionMission, Gallery
from .serializers import AboutUsSerializer, VisionMissionSerializer, GallerySerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class VisionMissionViewSet(viewsets.ModelViewSet):
    queryset = VisionMission.objects.all()
    serializer_class = VisionMissionSerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

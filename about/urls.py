from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutUsViewSet, VisionMissionViewSet, GalleryViewSet

router = DefaultRouter()
router.register(r'about-us', AboutUsViewSet)
router.register(r'vision-mission', VisionMissionViewSet)
router.register(r'gallery', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

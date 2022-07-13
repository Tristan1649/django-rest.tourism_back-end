from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, TurViewSet, GalleryViewSet, EventViewSet
router = DefaultRouter()
router.register('location', LocationViewSet)
router.register('tur', TurViewSet)
router.register('gallery', GalleryViewSet)
router.register('event', EventViewSet)

urlpatterns = router.urls
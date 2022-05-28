from rest_framework.routers import DefaultRouter
from .views import LibraryViewSet, RackViewSet

router = DefaultRouter()
router.register("library", LibraryViewSet)
router.register("racks", RackViewSet)

urlpatterns = router.urls
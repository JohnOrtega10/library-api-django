from .views import MemberAccountViewSet, LibrarianAccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("members", MemberAccountViewSet)
router.register("librarians", LibrarianAccountViewSet)

urlpatterns = router.urls
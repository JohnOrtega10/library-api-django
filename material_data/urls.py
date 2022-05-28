from rest_framework.routers import DefaultRouter
from .views import  EditorialViewSet, AuthorViewSet

router = DefaultRouter()
router.register("editorials", EditorialViewSet)
router.register("authors", AuthorViewSet)

urlpatterns = router.urls
from rest_framework.routers import DefaultRouter
from .views import BookItemViewSet, BookViewSet

router = DefaultRouter()
router.register("books", BookViewSet)
router.register("books_library", BookItemViewSet)
urlpatterns = router.urls

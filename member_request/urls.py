from rest_framework.routers import DefaultRouter
from .views import BookLendingViewSet, BookReservationViewSet 

router = DefaultRouter()
router.register("rents", BookLendingViewSet)
router.register("reservations", BookReservationViewSet)

urlpatterns = router.urls
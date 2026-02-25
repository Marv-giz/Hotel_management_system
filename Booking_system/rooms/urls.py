from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, RoomCategoryViewSet

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('categories', RoomCategoryViewSet)

urlpatterns = router.urls
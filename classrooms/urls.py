from rest_framework.routers import DefaultRouter

from .views import ClassroomViewSet

router = DefaultRouter()
router.register("classrooms", ClassroomViewSet)
urlpatterns = router.urls

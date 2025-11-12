from rest_framework.routers import DefaultRouter
from .views import GoalsViewSets

router = DefaultRouter()
router.register('', GoalsViewSets, basename='goals')

urlpatterns = router.urls
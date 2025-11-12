from rest_framework.routers import DefaultRouter
from .views import AccountViewSets

router = DefaultRouter()
router.register('', AccountViewSets, basename='accounts')

urlpatterns = router.urls
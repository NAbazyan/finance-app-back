from rest_framework.routers import DefaultRouter
from .views import TransactionViewSets

router = DefaultRouter()
router.register(r'', TransactionViewSets, basename='transactions')

urlpatterns = router.urls
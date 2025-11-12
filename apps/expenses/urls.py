from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSets

router = DefaultRouter()
router.register('', ExpenseViewSets, basename='expense')

urlpatterns = router.urls
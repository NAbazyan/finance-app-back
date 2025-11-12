from rest_framework.routers import DefaultRouter
from .views import BillViewSets, ProductViewSets

router = DefaultRouter()
router.register('bills', BillViewSets, basename='bills')
router.register('products', ProductViewSets, basename='products')

urlpatterns = router.urls
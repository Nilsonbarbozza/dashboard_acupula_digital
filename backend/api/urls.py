from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardMetricsViewSet, SaldosMetricsViewSet

router = DefaultRouter()
router.register(r'metrics', DashboardMetricsViewSet)
router.register(r'saldos', SaldosMetricsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

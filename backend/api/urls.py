from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardMetricsViewSet, SaldosMetricsViewSet, TransacoesMetricsViewSet

router = DefaultRouter()
router.register(r'metrics', DashboardMetricsViewSet)
router.register(r'saldos', SaldosMetricsViewSet)
router.register(r'transacoes', TransacoesMetricsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

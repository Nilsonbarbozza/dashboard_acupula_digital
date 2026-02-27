from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardMetricsViewSet, SaldosMetricsViewSet, TransacoesMetricsViewSet, ClientesMetricsViewSet, CatalogoMetricsViewSet, MetricasGeralViewSet

router = DefaultRouter()
router.register(r'metrics', DashboardMetricsViewSet, basename='metrics')
router.register(r'saldos', SaldosMetricsViewSet, basename='saldos')
router.register(r'transacoes', TransacoesMetricsViewSet, basename='transacoes')
router.register(r'clientes', ClientesMetricsViewSet, basename='clientes')
router.register(r'catalogo', CatalogoMetricsViewSet, basename='catalogo')
router.register(r'metricas-geral', MetricasGeralViewSet, basename='metricas-geral')

urlpatterns = [
    path('', include(router.urls)),
]

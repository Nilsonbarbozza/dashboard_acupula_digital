from rest_framework import viewsets
from rest_framework.response import Response
from .models import DashboardMetrics, SaldosMetrics, TransacoesMetrics, ClientesMetrics, CatalogoMetrics, MetricasGeral
from .serializers import DashboardMetricsSerializer, SaldosMetricsSerializer, TransacoesMetricsSerializer, ClientesMetricsSerializer, CatalogoMetricsSerializer, MetricasGeralSerializer

class DashboardMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para obter os sumários do painel.
    O ReadOnlyModelViewSet garante que só haja métodos GET.
    """
    queryset = DashboardMetrics.objects.all()
    serializer_class = DashboardMetricsSerializer

    def list(self, request, *args, **kwargs):
        # Sempre retorna o primeiro e único registro, criando se não existir
        instance = self.queryset.first()
        if not instance:
            instance = DashboardMetrics.objects.create()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class SaldosMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SaldosMetrics.objects.all()
    serializer_class = SaldosMetricsSerializer

    def list(self, request, *args, **kwargs):
        instance = self.queryset.first()
        if not instance:
            instance = SaldosMetrics.objects.create()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class TransacoesMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TransacoesMetrics.objects.all()
    serializer_class = TransacoesMetricsSerializer

    def list(self, request, *args, **kwargs):
        instance = self.queryset.first()
        if not instance:
            instance = TransacoesMetrics.objects.create()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ClientesMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClientesMetrics.objects.all()
    serializer_class = ClientesMetricsSerializer

    def list(self, request, *args, **kwargs):
        instance = self.queryset.first()
        if not instance:
            instance = ClientesMetrics.objects.create()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CatalogoMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CatalogoMetrics.objects.all()
    serializer_class = CatalogoMetricsSerializer

    def list(self, request, *args, **kwargs):
        instance = self.queryset.first()
        if not instance:
            instance = CatalogoMetrics.objects.create()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class MetricasGeralViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MetricasGeral.objects.all()
    serializer_class = MetricasGeralSerializer

    def list(self, request, *args, **kwargs):
        # Automatically populate initial standard periods if empty
        if not self.queryset.exists():
            default_data = {
                'hoje': {
                    'valor_bruto': 10449.55, 'volume_bruto_anterior': 13034.88,
                    'volume_liquido': 9749.21, 'volume_liquido_anterior': 9187.34,
                    'clientes': 81, 'clientes_anterior': 51
                },
                'ultimos7dias': {
                    'valor_bruto': 224583.83, 'volume_bruto_anterior': 181421.83,
                    'volume_liquido': 183630.12, 'volume_liquido_anterior': 112234.56,
                    'clientes': 209, 'clientes_anterior': 154
                },
                'ultimas4semanas': {
                    'valor_bruto': 492071.00, 'volume_bruto_anterior': 321341.09,
                    'volume_liquido': 382754.66, 'volume_liquido_anterior': 281901.45,
                    'clientes': 412, 'clientes_anterior': 356
                },
                'ultimos6meses': {
                    'valor_bruto': 553420.50, 'volume_bruto_anterior': 446353.23,
                    'volume_liquido': 451280.30, 'volume_liquido_anterior': 391876.12,
                    'clientes': 524, 'clientes_anterior': 478
                },
                'ultimos12meses': {
                    'valor_bruto': 8010340.25, 'volume_bruto_anterior': 892901.01,
                    'volume_liquido': 701960.55, 'volume_liquido_anterior': 720345.67,
                    'clientes': 723, 'clientes_anterior': 612
                },
                'mesatedata': {
                    'valor_bruto': 2451680.75, 'volume_bruto_anterior': 134121.83,
                    'volume_liquido': 2238540.20, 'volume_liquido_anterior': 1121340.56,
                    'clientes': 842, 'clientes_anterior': 754
                },
                'trimesteateadata': {
                    'valor_bruto': 3206450.60, 'volume_bruto_anterior': 1645321.45,
                    'volume_liquido': 2862780.90, 'volume_liquido_anterior': 1431210.34,
                    'clientes': 912, 'clientes_anterior': 834
                },
                'anoateadata': {
                    'valor_bruto': 4007890.80, 'volume_bruto_anterior': 2045321.67,
                    'volume_liquido': 3663780.75, 'volume_liquido_anterior': 1831450.89,
                    'clientes': 978, 'clientes_anterior': 876
                },
                'desdoinicio': {
                    'valor_bruto': 4859920.90, 'volume_bruto_anterior': 2431421.93,
                    'volume_liquido': 4264780.45, 'volume_liquido_anterior': 2234450.78,
                    'clientes': 1024, 'clientes_anterior': 934
                }
            }
            for key, data in default_data.items():
                MetricasGeral.objects.get_or_create(periodo=key, defaults=data)

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

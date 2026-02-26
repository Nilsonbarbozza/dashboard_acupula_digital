from rest_framework import viewsets
from rest_framework.response import Response
from .models import DashboardMetrics, SaldosMetrics, TransacoesMetrics, ClientesMetrics, CatalogoMetrics
from .serializers import DashboardMetricsSerializer, SaldosMetricsSerializer, TransacoesMetricsSerializer, ClientesMetricsSerializer, CatalogoMetricsSerializer

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

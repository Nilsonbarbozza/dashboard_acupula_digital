from rest_framework import viewsets
from rest_framework.response import Response
from .models import DashboardMetrics, SaldosMetrics
from .serializers import DashboardMetricsSerializer, SaldosMetricsSerializer

class DashboardMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows metrics to be viewed.
    We only expect one record to exist, so we override get_queryset to ensure it only returns the first/active one if needed.
    """
    queryset = DashboardMetrics.objects.all()
    serializer_class = DashboardMetricsSerializer

    def list(self, request, *args, **kwargs):
        # Always return a single object object instead of an array
        instance = self.queryset.first()
        if not instance:
            instance = DashboardMetrics.objects.create() # Create default if none exists
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

from rest_framework import viewsets
from rest_framework.response import Response
from .models import DashboardMetrics
from .serializers import DashboardMetricsSerializer

class DashboardMetricsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DashboardMetrics.objects.all()
    serializer_class = DashboardMetricsSerializer

    def list(self, request, *args, **kwargs):
        # Always return a single object object instead of an array
        instance = self.queryset.first()
        if not instance:
            instance = DashboardMetrics.objects.create() # Create default if none exists
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

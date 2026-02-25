from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardMetricsViewSet

router = DefaultRouter()
router.register(r'metrics', DashboardMetricsViewSet, basename='metrics')

urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib import admin
from .models import DashboardMetrics, SaldosMetrics, TransacoesMetrics

@admin.register(DashboardMetrics)
class DashboardMetricsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if DashboardMetrics.objects.exists():
            return False
        return True

@admin.register(SaldosMetrics)
class SaldosMetricsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SaldosMetrics.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(TransacoesMetrics)
class TransacoesMetricsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if TransacoesMetrics.objects.exists():
            return False
        return True

from django.contrib import admin
from .models import DashboardMetrics, SaldosMetrics, TransacoesMetrics, ClientesMetrics, CatalogoMetrics, MetricasGeral

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

@admin.register(ClientesMetrics)
class ClientesMetricsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if ClientesMetrics.objects.exists():
            return False
        return True

@admin.register(CatalogoMetrics)
class CatalogoMetricsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if CatalogoMetrics.objects.exists():
            return False
        return True

@admin.register(MetricasGeral)
class MetricasGeralAdmin(admin.ModelAdmin):
    list_display = ('get_periodo_display', 'valor_bruto', 'volume_liquido', 'clientes', 'updated_at')
    
    def has_add_permission(self, request):
        # We only want the 9 explicitly defined periods
        if MetricasGeral.objects.count() >= 9:
            return False
        return True

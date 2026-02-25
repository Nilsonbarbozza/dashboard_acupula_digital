from django.contrib import admin
from .models import DashboardMetrics

@admin.register(DashboardMetrics)
class DashboardMetricsAdmin(admin.ModelAdmin):
    list_display = ('id', 'volume_bruto', 'novos_clientes', 'pagamentos_realizados', 'volume_liquido')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

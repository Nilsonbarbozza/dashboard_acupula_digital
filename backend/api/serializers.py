from rest_framework import serializers
from .models import DashboardMetrics, SaldosMetrics

class DashboardMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardMetrics
        fields = [
            'id', 
            'volume_bruto', 'volume_bruto_ontem', 
            'novos_clientes', 'novos_clientes_ontem', 
            'pagamentos_realizados', 'pagamentos_realizados_ontem', 
            'volume_liquido', 'volume_liquido_ontem',
            'saldo_usd', 'repasses'
        ]

class SaldosMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaldosMetrics
        fields = ['id', 'saldo_total', 'entrada', 'disponivel']

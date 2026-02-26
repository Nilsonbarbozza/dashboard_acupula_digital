from rest_framework import serializers
from .models import DashboardMetrics, SaldosMetrics, TransacoesMetrics

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
        fields = [
            'id', 'saldo_total', 'entrada', 'disponivel',
            'atividade_1_valor', 'atividade_1_data',
            'atividade_2_valor', 'atividade_2_data',
            'atividade_3_valor', 'atividade_3_data'
        ]
class TransacoesMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransacoesMetrics
        fields = [
            'id', 'tudo', 'ok', 'reembolsados',
            'contestados', 'malsucedidos', 'nao_capturados',
            'valor1', 'valor2', 'valor3', 'valor4', 'valor5', 'valor6',
            'valor7', 'valor8', 'valor9', 'valor10', 'valor11'
        ]

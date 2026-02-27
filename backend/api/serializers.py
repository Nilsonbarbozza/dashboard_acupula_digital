from rest_framework import serializers
from .models import DashboardMetrics, SaldosMetrics, TransacoesMetrics, ClientesMetrics, CatalogoMetrics, MetricasGeral

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

class ClientesMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesMetrics
        fields = [
            'id', 
            'nome1', 'nome2', 'nome3', 'nome4', 'nome5', 'nome6',
            'nome7', 'nome8', 'nome9', 'nome10', 'nome11', 'nome12',
            'email1', 'email2', 'email3', 'email4', 'email5', 'email6',
            'email7', 'email8', 'email9', 'email10', 'email11', 'email12'
        ]

class CatalogoMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoMetrics
        fields = '__all__'

class MetricasGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricasGeral
        fields = '__all__'

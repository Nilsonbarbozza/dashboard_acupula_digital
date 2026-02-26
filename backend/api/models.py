from django.db import models

class DashboardMetrics(models.Model):
    volume_bruto = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    volume_bruto_ontem = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    novos_clientes = models.IntegerField(default=0)
    novos_clientes_ontem = models.IntegerField(default=0)
    
    pagamentos_realizados = models.IntegerField(default=0)
    pagamentos_realizados_ontem = models.IntegerField(default=0)
    
    volume_liquido = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    volume_liquido_ontem = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    saldo_usd = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    repasses = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Métrica do Dropdown"
        verbose_name_plural = "Métricas do Dropdown"

    def __str__(self):
        return f"Dashboard Metrics (Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

class SaldosMetrics(models.Model):
    saldo_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    entrada = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    disponivel = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    # Atividades Recentes
    atividade_1_valor = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    atividade_1_data = models.CharField(max_length=50, blank=True, null=True, default='')
    atividade_2_valor = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    atividade_2_data = models.CharField(max_length=50, blank=True, null=True, default='')
    atividade_3_valor = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    atividade_3_data = models.CharField(max_length=50, blank=True, null=True, default='')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Métrica de Saldos"
        verbose_name_plural = "Métricas de Saldos"

    def __str__(self):
        return f"Saldos Metrics (Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

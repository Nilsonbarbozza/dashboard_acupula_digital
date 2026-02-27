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

class TransacoesMetrics(models.Model):
    tudo = models.IntegerField(default=0)
    ok = models.IntegerField(default=0)
    reembolsados = models.IntegerField(default=0)
    contestados = models.IntegerField(default=0)
    malsucedidos = models.IntegerField(default=0)
    nao_capturados = models.IntegerField(default=0)
    
    # Valores dinâmicos da tabela 1 ao 11
    valor1 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor2 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor3 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor4 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor5 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor6 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor7 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor8 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor9 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor10 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor11 = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Métrica de Transações"
        verbose_name_plural = "Métricas de Transações"

    def __str__(self):
        return f"Transações Metrics (Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

class ClientesMetrics(models.Model):
    # Nomes
    nome1 = models.CharField(max_length=255, default="Minneapolis Mental Health")
    nome2 = models.CharField(max_length=255, default="San Diego Fertility Center")
    nome3 = models.CharField(max_length=255, default="Milwaukee Urology Specialists")
    nome4 = models.CharField(max_length=255, default="Virginia Rheumatology Clinic")
    nome5 = models.CharField(max_length=255, default="Radiology Partners")
    nome6 = models.CharField(max_length=255, default="Boston Heart Center")
    nome7 = models.CharField(max_length=255, default="Houston Methodist")
    nome8 = models.CharField(max_length=255, default="Mayo Clinic")
    nome9 = models.CharField(max_length=255, default="Cleveland Clinic")
    nome10 = models.CharField(max_length=255, default="New York Presbyterian")
    nome11 = models.CharField(max_length=255, default="UCLA Health")
    nome12 = models.CharField(max_length=255, default="Johns Hopkins Medicine")

    # Emails
    email1 = models.EmailField(default="support@minneapolismentalhealth.com")
    email2 = models.EmailField(default="info@sdfertility.com")
    email3 = models.EmailField(default="info@milwaukeeurology.com")
    email4 = models.EmailField(default="care@varheum.com")
    email5 = models.EmailField(default="scheduling@radpartnersnv.com")
    email6 = models.EmailField(default="finance@bostonheart.com")
    email7 = models.EmailField(default="support@houstonmethodist.org")
    email8 = models.EmailField(default="accounts@mayo.com")
    email9 = models.EmailField(default="contact@clevelandclinic.org")
    email10 = models.EmailField(default="info@nyp.org")
    email11 = models.EmailField(default="support@uclahealth.org")
    email12 = models.EmailField(default="patientcare@jhmi.edu")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Métrica de Clientes"
        verbose_name_plural = "Métricas de Clientes"

    def __str__(self):
        return f"Clientes Metrics (Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

class CatalogoMetrics(models.Model):
    total = models.IntegerField(default=1)
    ativos = models.IntegerField(default=1)
    arquivados = models.IntegerField(default=0)
    
    # Produto
    produto_nome = models.CharField(max_length=255, default="Á CUPULA DIGITAL")
    produto_preco = models.DecimalField(max_digits=12, decimal_places=2, default=1890.79)
    produto_data = models.CharField(max_length=50, default="10 de ago.")
    produto_data_atualizado = models.CharField(max_length=50, default="5 de jan.")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Métrica de Catálogo"
        verbose_name_plural = "Métricas de Catálogo"

    def __str__(self):
        return f"Catálogo Metrics (Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M')})"

class MetricasGeral(models.Model):
    PERIOD_CHOICES = [
        ('hoje', 'Hoje'),
        ('ultimos7dias', 'Últimos 7 dias'),
        ('ultimas4semanas', 'Últimas 4 semanas'),
        ('ultimos6meses', 'Últimos 6 meses'),
        ('ultimos12meses', 'Últimos 12 meses'),
        ('mesatedata', 'Meses até a data'),
        ('trimesteateadata', 'Trimestre até a data'),
        ('anoateadata', 'Ano até a data'),
        ('desdoinicio', 'Desde o início'),
    ]

    periodo = models.CharField(max_length=20, choices=PERIOD_CHOICES, unique=True, verbose_name="Período")
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Valor Bruto")
    volume_bruto_anterior = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Volume Bruto Anterior")
    volume_liquido = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Volume Líquido")
    volume_liquido_anterior = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Volume Líquido Anterior")
    clientes = models.IntegerField(default=0, verbose_name="Clientes")
    clientes_anterior = models.IntegerField(default=0, verbose_name="Clientes Anterior")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Métrica Geral (Dashboard)"
        verbose_name_plural = "Métricas Gerais (Dashboard)"

    def __str__(self):
        return dict(self.PERIOD_CHOICES).get(self.periodo, self.periodo)

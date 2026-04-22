// Configuração de URL da API para Produção ou Local
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
      ? 'http://localhost:8000'
      : 'https://dashboard-acupula-digital.onrender.com'

// Estado Global de Métricas (com fallback de segurança)
let globalMetrics = {
      volumebruto: 0,
      volumebruto_ontem: 0,
      novosclientes: 0,
      novosclientes_ontem: 0,
      pagamentos: 0,
      pagamentos_ontem: 0,
      volumeliquido: 0,
      volumeliquido_ontem: 0
};

// Inicia a busca o mais rápido possível
let snapshotPromise = fetchSnapshot();

document.addEventListener("DOMContentLoaded", async () => {
      // 1. Tenta carregar do cache para exibição INSTANTÂNEA
      loadFromCache();
      
      // 2. Configura a UI (Dropdowns, etc)
      setupDropdown();
      
      // 3. Aguarda a resposta real do servidor (Snapshot Consolidado)
      const data = await snapshotPromise;
      if (data) {
            applySnapshot(data);
            saveToCache(data);
            console.log("Dashboard atualizado com dados reais via Snapshot.");
      }
});

async function fetchSnapshot() {
      try {
            const response = await fetch(`${API_BASE_URL}/api/snapshot/`);
            if (!response.ok) throw new Error(`Snapshot error! status: ${response.status}`);
            return await response.json();
      } catch (err) {
            console.error("Falha ao buscar snapshot:", err);
            return null;
      }
}

function loadFromCache() {
      const cached = localStorage.getItem('dashboard_snapshot');
      if (cached) {
            try {
                  const data = JSON.parse(cached);
                  applySnapshot(data, true); // true = carregamento silencioso de cache
                  console.log("Dados carregados do cache local.");
            } catch (e) {
                  console.error("Erro ao ler cache:", e);
            }
      }
}

function saveToCache(data) {
      localStorage.setItem('dashboard_snapshot', JSON.stringify(data));
}

function applySnapshot(data, isCache = false) {
      if (!data) return;

      // 1. Dashboard Metrics (Volume Bruto, etc)
      if (data.metrics) {
            const metrics = data.metrics;
            globalMetrics.volumebruto = metrics.volume_bruto;
            globalMetrics.volumebruto_ontem = metrics.volume_bruto_ontem;
            globalMetrics.novosclientes = metrics.novos_clientes;
            globalMetrics.novosclientes_ontem = metrics.novos_clientes_ontem;
            globalMetrics.pagamentos = metrics.pagamentos_realizados;
            globalMetrics.pagamentos_ontem = metrics.pagamentos_realizados_ontem;
            globalMetrics.volumeliquido = metrics.volume_liquido;
            globalMetrics.volumeliquido_ontem = metrics.volume_liquido_ontem;

            // Independente (USD/Repasses)
            const saldoUSDEl = document.getElementById("saldoUSD");
            if (saldoUSDEl) {
                  const spanInner = saldoUSDEl.querySelector("span");
                  if (spanInner) spanInner.innerText = formatMoney(metrics.saldo_usd);
            }
            const repassesEl = document.getElementById("repassesValor");
            if (repassesEl) {
                  const spanInner = repassesEl.querySelector("span");
                  if (spanInner) spanInner.innerText = formatMoney(metrics.repasses);
            }

            updateDisplayValue();
      }

      // 2. Saldos
      if (data.saldos) {
            const s = data.saldos;
            updateElementText("saldoTotal", formatMoney(s.saldo_total));
            updateElementText("saldoEntrada", formatMoney(s.entrada));
            updateElementText("saldoDisponivel", formatMoney(s.disponivel));
            
            updateElementText("atividade1Valor", formatMoney(s.atividade_1_valor));
            updateElementText("atividade1Data", s.atividade_1_data || "");
            updateElementText("atividade2Valor", formatMoney(s.atividade_2_valor));
            updateElementText("atividade2Data", s.atividade_2_data || "");
            updateElementText("atividade3Valor", formatMoney(s.atividade_3_valor));
            updateElementText("atividade3Data", s.atividade_3_data || "");
      }

      // 3. Transações
      if (data.transacoes) {
            const t = data.transacoes;
            updateElementText("transacoesTudo", t.tudo);
            updateElementText("transacoesTudoFooter", t.tudo);
            updateElementText("transacoesOk", t.ok);
            updateElementText("transacoesReembolsados", t.reembolsados);
            updateElementText("transacoesContestados", t.contestados);
            updateElementText("transacoesMalsucedidos", t.malsucedidos);
            updateElementText("transacoesNaoCapturados", t.nao_capturados);

            for (let i = 1; i <= 11; i++) {
                  updateElementText(`valor${i}`, formatMoney(t[`valor${i}`]));
                  updateElementHTML(`nome${i}`, `&nbsp; ${t[`nome${i}`] || ''}`);
                  updateElementText(`data${i}`, t[`data${i}`] || "");
            }
      }

      // 4. Clientes
      if (data.clientes) {
            const c = data.clientes;
            for (let i = 1; i <= 12; i++) {
                  updateElementHTML(`clientName${i}`, `&nbsp; ${c[`nome${i}`] || ''}`);
                  updateElementText(`clientEmail${i}`, c[`email${i}`] || "");
            }
      }

      // 5. Catálogo
      if (data.catalogo) {
            const cat = data.catalogo;
            updateElementText("produtos-total", cat.total);
            updateElementText("produtos-ativos", cat.ativos);
            updateElementText("produtos-arquivados", cat.arquivados);
            updateElementHTML("nome-produto", `&nbsp; ${cat.produto_nome || ''}`);
            updateElementText("preco-produto", formatMoney(cat.produto_preco));
            updateElementText("data-produto", cat.produto_data);
            updateElementText("data-atualizado", cat.produto_data_atualizado);
      }

      // 6. Métricas Geral (Chart data)
      if (data.metricas_geral && typeof dadosMockados !== 'undefined') {
            data.metricas_geral.forEach(metric => {
                  const p = metric.periodo;
                  if (dadosMockados[p]) {
                        dadosMockados[p].valorBruto = parseFloat(metric.valor_bruto);
                        dadosMockados[p].volumeBrutoAnterior = parseFloat(metric.volume_bruto_anterior);
                        dadosMockados[p].volumeLiquido = parseFloat(metric.volume_liquido);
                        dadosMockados[p].volumeLiquidoAnterior = parseFloat(metric.volume_liquido_anterior);
                        dadosMockados[p].clientes = parseInt(metric.clientes);
                        dadosMockados[p].clientesAnterior = parseInt(metric.clientes_anterior);
                  }
            });
            if (typeof atualizarDashboard === 'function') {
                  const filtro = typeof filtroAtual !== 'undefined' ? filtroAtual : '7dias';
                  atualizarDashboard(filtro);
            }
      }
}

// Helpers Utilitários
function updateElementText(id, text) {
      const el = document.getElementById(id);
      if (el) el.innerText = text;
}

function updateElementHTML(id, html) {
      const el = document.getElementById(id);
      if (el) el.innerHTML = html;
}

function formatMoney(value) {
      if (!value && value !== 0) return "$ 0.00";
      return "$ " + parseFloat(value).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function updateDisplayValue() {
      const valorAtualEl = document.getElementById("valorAtual");
      const valorOntemEl = document.getElementById("valorOntem");
      if (!valorAtualEl) return;

      const metricType = valorAtualEl.getAttribute("data-metric");

      switch(metricType) {
            case "volumebruto":
                  valorAtualEl.innerText = formatMoney(globalMetrics.volumebruto);
                  if (valorOntemEl) valorOntemEl.innerText = formatMoney(globalMetrics.volumebruto_ontem);
                  break;
            case "novosclientes":
                  valorAtualEl.innerText = globalMetrics.novosclientes;
                  if (valorOntemEl) valorOntemEl.innerText = globalMetrics.novosclientes_ontem;
                  break;
            case "pagamentos":
                  valorAtualEl.innerText = globalMetrics.pagamentos;
                  if (valorOntemEl) valorOntemEl.innerText = globalMetrics.pagamentos_ontem;
                  break;
            case "volumeliquido":
                  valorAtualEl.innerText = formatMoney(globalMetrics.volumeliquido);
                  if (valorOntemEl) valorOntemEl.innerText = formatMoney(globalMetrics.volumeliquido_ontem);
                  break;
      }
}

function setupDropdown() {
      const menuButton = document.getElementById("menu2-button");
      const dropdownMenu = document.getElementById("select-valorbruto");

      if (!menuButton || !dropdownMenu) return;

      document.body.appendChild(dropdownMenu);

      menuButton.addEventListener("click", function (e) {
            e.stopPropagation();
            const rect = menuButton.getBoundingClientRect();
            dropdownMenu.style.position = 'absolute';
            dropdownMenu.style.top = `${rect.bottom + window.scrollY + 8}px`;
            dropdownMenu.style.left = `${rect.left + window.scrollX}px`;
            dropdownMenu.classList.toggle("hidden");
      });

      document.addEventListener("click", function (e) {
            if (!menuButton.contains(e.target) && !dropdownMenu.contains(e.target)) {
                  dropdownMenu.classList.add("hidden");
            }
      });

      const options = dropdownMenu.querySelectorAll(".option-item");
      const labelSpan = document.getElementById("metricaSelecionadaLabel");
      const valorAtualSpan = document.getElementById("valorAtual");

      options.forEach(option => {
            option.addEventListener("click", function (e) {
                  e.stopPropagation();
                  const metricName = this.querySelector("span").innerText;
                  if (labelSpan) labelSpan.innerText = metricName;

                  options.forEach(opt => {
                        opt.classList.remove("selected");
                        const _svg = opt.querySelector("svg");
                        if (_svg) _svg.classList.replace("text-blue-500", "text-gray-300");
                        if (_svg) _svg.classList.add("opacity-0");
                  });

                  this.classList.add("selected");
                  const activeSvg = this.querySelector("svg");
                  if (activeSvg) {
                        activeSvg.classList.replace("text-gray-300", "text-blue-500");
                        activeSvg.classList.remove("opacity-0");
                  }

                  const newMetric = this.getAttribute("data-metric");
                  if (valorAtualSpan) valorAtualSpan.setAttribute("data-metric", newMetric);
                  updateDisplayValue();
                  dropdownMenu.classList.add("hidden");
            });
      });
}

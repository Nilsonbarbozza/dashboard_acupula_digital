document.addEventListener("DOMContentLoaded", () => {
      fetchMetrics();
      setupDropdown();
      fetchSaldosMetrics(); // Will safely ignore if elements aren't present
      fetchTransacoesMetrics(); // Will safely ignore if elements aren't present
      fetchClientesMetrics(); // Will safely ignore if elements aren't present
      fetchCatalogoMetrics(); // Will safely ignore if elements aren't present
});

async function fetchTransacoesMetrics() {
      const transTudoEl = document.getElementById("transacoesTudo");
      const transOkEl = document.getElementById("transacoesOk");
      const transReembolsadosEl = document.getElementById("transacoesReembolsados");
      const transContestadosEl = document.getElementById("transacoesContestados");
      const transMalsucedidosEl = document.getElementById("transacoesMalsucedidos");
      const transNaoCapturadosEl = document.getElementById("transacoesNaoCapturados");

      let hasAnyValorEl = false;
      for (let i = 1; i <= 11; i++) {
            if (document.getElementById(`valor${i}`)) {
                  hasAnyValorEl = true;
                  break;
            }
      }

      if (!transTudoEl && !transOkEl && !transReembolsadosEl &&
            !transContestadosEl && !transMalsucedidosEl && !transNaoCapturadosEl && !hasAnyValorEl) {
            return;
      }

      try {
            const response = await fetch('http://localhost:8000/api/transacoes/');
            if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            const metrics = Array.isArray(data) ? data[0] : data;

            if (metrics) {
                  if (transTudoEl) transTudoEl.innerText = metrics.tudo;
                  if (transOkEl) transOkEl.innerText = metrics.ok;
                  if (transReembolsadosEl) transReembolsadosEl.innerText = metrics.reembolsados;
                  if (transContestadosEl) transContestadosEl.innerText = metrics.contestados;
                  if (transMalsucedidosEl) transMalsucedidosEl.innerText = metrics.malsucedidos;
                  if (transNaoCapturadosEl) transNaoCapturadosEl.innerText = metrics.nao_capturados;

                  for (let i = 1; i <= 11; i++) {
                        const valorEl = document.getElementById(`valor${i}`);
                        if (valorEl) {
                              const valorKey = `valor${i}`;
                              if (metrics[valorKey] !== undefined) {
                                    valorEl.innerText = formatMoney(metrics[valorKey]);
                              }
                        }
                  }
            }
      } catch (err) {
            console.error("Error fetching Transacoes metrics:", err);
      }
}

async function fetchSaldosMetrics() {
      // Check if we are on the Saldos page by looking for the IDs
      const saldoTotalEl = document.getElementById("saldoTotal");
      const saldoEntradaEl = document.getElementById("saldoEntrada");
      const saldoDisponivelEl = document.getElementById("saldoDisponivel");

      if (!saldoTotalEl && !saldoEntradaEl && !saldoDisponivelEl) return;

      try {
            const response = await fetch('http://localhost:8000/api/saldos/');
            if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();

            // The API returns an array, so we get the first record
            const metrics = Array.isArray(data) ? data[0] : data;

            if (metrics) {
                  if (saldoTotalEl) saldoTotalEl.innerText = formatMoney(metrics.saldo_total);
                  if (saldoEntradaEl) saldoEntradaEl.innerText = formatMoney(metrics.entrada);
                  if (saldoDisponivelEl) saldoDisponivelEl.innerText = formatMoney(metrics.disponivel);

                  // Atividades Recentes
                  const ativ1Val = document.getElementById("atividade1Valor");
                  const ativ1Dat = document.getElementById("atividade1Data");
                  const ativ2Val = document.getElementById("atividade2Valor");
                  const ativ2Dat = document.getElementById("atividade2Data");
                  const ativ3Val = document.getElementById("atividade3Valor");
                  const ativ3Dat = document.getElementById("atividade3Data");

                  if (ativ1Val) ativ1Val.innerText = formatMoney(metrics.atividade_1_valor);
                  if (ativ1Dat) ativ1Dat.innerText = metrics.atividade_1_data || "";

                  if (ativ2Val) ativ2Val.innerText = formatMoney(metrics.atividade_2_valor);
                  if (ativ2Dat) ativ2Dat.innerText = metrics.atividade_2_data || "";

                  if (ativ3Val) ativ3Val.innerText = formatMoney(metrics.atividade_3_valor);
                  if (ativ3Dat) ativ3Dat.innerText = metrics.atividade_3_data || "";
            }
      } catch (err) {
            console.error("Error fetching Saldos metrics:", err);
      }
}

async function fetchClientesMetrics() {
      // Check if we are on the Clientes page by looking for the ID
      const clientName1El = document.getElementById("clientName1");
      if (!clientName1El) return;

      try {
            const response = await fetch('http://localhost:8000/api/clientes/');
            if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            const metrics = Array.isArray(data) ? data[0] : data;

            if (metrics) {
                  for (let i = 1; i <= 12; i++) {
                        const nameEl = document.getElementById(`clientName${i}`);
                        const emailEl = document.getElementById(`clientEmail${i}`);

                        if (nameEl && metrics[`nome${i}`]) {
                              nameEl.innerHTML = `&nbsp; ${metrics["nome" + i]}`;
                        }
                        if (emailEl && metrics[`email${i}`]) {
                              emailEl.innerText = metrics[`email${i}`];
                        }
                  }
            }
      } catch (err) {
            console.error("Error fetching Clientes metrics:", err);
      }
}

async function fetchCatalogoMetrics() {
      // Check Se está na página de catalogo
      const totalEl = document.getElementById("produtos-total");
      const ativosEl = document.getElementById("produtos-ativos");
      const arquivadosEl = document.getElementById("produtos-arquivados");

      // Table elements
      const nomeProdutoEl = document.getElementById("nome-produto");
      const precoProdutoEl = document.getElementById("preco-produto");
      const dataProdutoEl = document.getElementById("data-produto");
      const dataAtualizadoEl = document.getElementById("data-atualizado");

      if (!totalEl && !ativosEl && !arquivadosEl && !nomeProdutoEl) return;

      try {
            const response = await fetch('http://localhost:8000/api/catalogo/');
            if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            const metrics = Array.isArray(data) ? data[0] : data;

            if (metrics) {
                  // Top KPIs
                  if (totalEl) totalEl.innerText = metrics.total;
                  if (ativosEl) ativosEl.innerText = metrics.ativos;
                  if (arquivadosEl) arquivadosEl.innerText = metrics.arquivados;

                  // Table Row
                  if (nomeProdutoEl) nomeProdutoEl.innerHTML = `&nbsp; ${metrics.produto_nome}`;
                  if (precoProdutoEl) precoProdutoEl.innerText = formatMoney(metrics.produto_preco);
                  if (dataProdutoEl) dataProdutoEl.innerText = metrics.produto_data;
                  if (dataAtualizadoEl) dataAtualizadoEl.innerText = metrics.produto_data_atualizado;
            }
      } catch (err) {
            console.error("Error fetching Catalogo metrics:", err);
      }
}

let globalMetrics = {
      volumebruto: 13812.00,
      volumebruto_ontem: 9758.00,
      novosclientes: 45,
      novosclientes_ontem: 40,
      pagamentos: 120,
      pagamentos_ontem: 110,
      volumeliquido: 9000.00,
      volumeliquido_ontem: 8500.00
};

async function fetchMetrics() {
      try {
            const response = await fetch("http://localhost:8000/api/metrics/");
            const data = await response.json();
            const metrics = Array.isArray(data) ? data[0] : data;

            if (metrics) {
                  globalMetrics.volumebruto = metrics.volume_bruto;
                  globalMetrics.volumebruto_ontem = metrics.volume_bruto_ontem;

                  globalMetrics.novosclientes = metrics.novos_clientes;
                  globalMetrics.novosclientes_ontem = metrics.novos_clientes_ontem;

                  globalMetrics.pagamentos = metrics.pagamentos_realizados;
                  globalMetrics.pagamentos_ontem = metrics.pagamentos_realizados_ontem;

                  globalMetrics.volumeliquido = metrics.volume_liquido;
                  globalMetrics.volumeliquido_ontem = metrics.volume_liquido_ontem;

                  // Update Independent Static Metrics
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

                  // Update the currently selected exact metric UI immediately
                  updateDisplayValue();
            }
      } catch (err) {
            console.error("Error fetching metrics:", err);
      }
}

function formatMoney(value) {
      if (!value) return "$ 0.00";
      return "$ " + parseFloat(value).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function updateDisplayValue() {
      const valorAtualEl = document.getElementById("valorAtual");
      const valorOntemEl = document.getElementById("valorOntem");

      if (!valorAtualEl) return;

      const metricType = valorAtualEl.getAttribute("data-metric");

      if (metricType === "volumebruto") {
            valorAtualEl.innerText = formatMoney(globalMetrics.volumebruto);
            if (valorOntemEl) valorOntemEl.innerText = formatMoney(globalMetrics.volumebruto_ontem);
      } else if (metricType === "novosclientes") {
            valorAtualEl.innerText = globalMetrics.novosclientes;
            if (valorOntemEl) valorOntemEl.innerText = globalMetrics.novosclientes_ontem;
      } else if (metricType === "pagamentos") {
            valorAtualEl.innerText = globalMetrics.pagamentos;
            if (valorOntemEl) valorOntemEl.innerText = globalMetrics.pagamentos_ontem;
      } else if (metricType === "volumeliquido") {
            valorAtualEl.innerText = formatMoney(globalMetrics.volumeliquido);
            if (valorOntemEl) valorOntemEl.innerText = formatMoney(globalMetrics.volumeliquido_ontem);
      }
}

function setupDropdown() {
      const menuButton = document.getElementById("menu2-button");
      const dropdownMenu = document.getElementById("select-valorbruto");

      if (!menuButton || !dropdownMenu) return;

      // Move dropdown to body to bypass overflow: hidden limits
      document.body.appendChild(dropdownMenu);

      // Toggle dropdown
      menuButton.addEventListener("click", function (e) {
            e.stopPropagation();

            // Position the dropdown dynamically right below the button
            const rect = menuButton.getBoundingClientRect();
            dropdownMenu.style.position = 'absolute';
            dropdownMenu.style.top = `${rect.bottom + window.scrollY + 8}px`;
            dropdownMenu.style.left = `${rect.left + window.scrollX}px`;

            dropdownMenu.classList.toggle("hidden");
      });

      // Hide dropdown when clicking outside
      document.addEventListener("click", function (e) {
            if (!menuButton.contains(e.target) && !dropdownMenu.contains(e.target)) {
                  dropdownMenu.classList.add("hidden");
            }
      });

      // Handle option selection
      const options = dropdownMenu.querySelectorAll(".option-item");
      const labelSpan = document.getElementById("metricaSelecionadaLabel");
      const valorAtualSpan = document.getElementById("valorAtual");

      options.forEach(option => {
            option.addEventListener("click", function (e) {
                  e.stopPropagation();

                  // 1. Update text label
                  const metricName = this.querySelector("span").innerText;
                  if (labelSpan) {
                        labelSpan.innerText = metricName;
                  }

                  // 2. Visual indicator (check mark)
                  options.forEach(opt => {
                        opt.classList.remove("selected");
                        const svg = opt.querySelector("svg");
                        if (svg) {
                              svg.classList.remove("text-blue-500");
                              svg.classList.add("text-gray-300", "opacity-0");
                        }
                  });

                  this.classList.add("selected");
                  const activeSvg = this.querySelector("svg");
                  if (activeSvg) {
                        activeSvg.classList.remove("text-gray-300", "opacity-0");
                        activeSvg.classList.add("text-blue-500");
                  }

                  // 3. Update data-metric attribute
                  const newMetric = this.getAttribute("data-metric");
                  if (valorAtualSpan) {
                        valorAtualSpan.setAttribute("data-metric", newMetric);
                  }

                  // 4. Update the displayed value based on globally stored metrics
                  updateDisplayValue();

                  // 5. Close dropdown
                  dropdownMenu.classList.add("hidden");
            });
      });
}

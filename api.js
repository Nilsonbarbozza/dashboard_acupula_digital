document.addEventListener("DOMContentLoaded", () => {
      fetchMetrics();
      setupDropdown();
});

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

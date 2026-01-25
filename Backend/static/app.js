let riskChart = null;

document.addEventListener("DOMContentLoaded", () => {

    const runBtn = document.getElementById("runScanBtn");
    const resultsContainer = document.getElementById("resultsContainer");
    const scoreBox = document.getElementById("score");

    runBtn.addEventListener("click", () => {
        const target = document.getElementById("target").value.trim();
        const scanType = document.getElementById("scanType").value;

        if (!target) {
            alert("Enter a target");
            return;
        }

        resultsContainer.innerHTML = `<p class="placeholder">⏳ Scanning...</p>`;
        scoreBox.textContent = "—";

        fetch("/run-scan", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ type: scanType, target })
        })
        .then(res => res.json())
        .then(data => renderResults(data))
        .catch(err => {
            console.error(err);
            resultsContainer.innerHTML =
                `<p class="placeholder">❌ Scan Failed</p>`;
        });
    });
});

function renderResults(data) {
    const container = document.getElementById("resultsContainer");
    const scoreBox = document.getElementById("score");

    container.innerHTML = "";

    if (data.error) {
        container.innerHTML = `<p class="placeholder">❌ ${data.error}</p>`;
        return;
    }

    if (!data.results || data.results.length === 0) {
        container.innerHTML = `<p class="placeholder">✅ No issues found</p>`;
    } else {
        data.results.forEach((item, i) => {
            const box = document.createElement("div");
            box.className = `result-box risk-${item.risk}`;

            box.innerHTML = `
                <h3>#${i + 1} ${item.service || item.check || "Finding"}</h3>
                ${item.port ? `<p><b>Port:</b> ${item.port}</p>` : ""}
                <p><b>Status:</b> ${item.status}</p>
                <p><b>Risk:</b> ${item.risk.toUpperCase()}</p>
                <p><b>Recommendation:</b> ${item.recommendation}</p>
            `;

            container.appendChild(box);
        });
    }

    // ✅ Score
    scoreBox.textContent =
        `${data.risk.security_score} / 100 (${data.risk.grade})`;

    // ✅ Donut chart
    renderRiskChart(data.risk.risk_breakdown);
}

function renderRiskChart(breakdown) {
    const ctx = document.getElementById("riskChart");

    if (riskChart) {
        riskChart.destroy();
    }

    riskChart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["Low", "Medium", "High", "Critical"],
            datasets: [{
                data: [
                    breakdown.low,
                    breakdown.medium,
                    breakdown.high,
                    breakdown.critical
                ]
            }]
        },
        options: {
            plugins: {
                legend: { position: "bottom" }
            }
        }
    });
}

document.getElementById("runScanBtn").addEventListener("click", () => {
    const target = document.getElementById("target").value.trim();
    const scanType = document.getElementById("scanType").value;

    if (!target) {
        alert("Enter a target");
        return;
    }

    document.getElementById("output").textContent = "⏳ Scanning...";
    document.getElementById("score").textContent = "—";

    fetch("/run-scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            type: scanType,
            target: target
        })
    })
    .then(res => res.json())
    .then(data => renderResults(data))
    .catch(err => {
        console.error(err);
        document.getElementById("output").textContent =
            "❌ Scan Failed: " + err.message;
    });
});


function renderResults(data) {
    const output = document.getElementById("output");
    const scoreBox = document.getElementById("score");

    if (data.error) {
        output.textContent = "❌ Error: " + data.error;
        scoreBox.textContent = "—";
        return;
    }

    /* --------- RESULTS --------- */
    if (!data.results || data.results.length === 0) {
        output.textContent = "✅ No issues found.";
    } else {
        let text = "";

        data.results.forEach((item, i) => {
            text += `#${i + 1}\n`;
            for (const key in item) {
                text += `${key}: ${item[key]}\n`;
            }
            text += "\n-----------------\n\n";
        });

        output.textContent = text;
    }
    
    if (data.risk) {
        scoreBox.textContent = data.risk.security_score + " / 100";
    }
}
   

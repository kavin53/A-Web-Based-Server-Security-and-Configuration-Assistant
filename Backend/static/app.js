document.getElementById("runScanBtn").addEventListener("click", async () => {
    const target = document.getElementById("target").value.trim();
    const scanType = document.getElementById("scanType").value;
    const output = document.getElementById("output");
    const score = document.getElementById("score");

    output.textContent = "⏳ Scanning...";
    score.textContent = "—";

    if (!target) {
        output.textContent = "❌ Error: Target is required";
        return;
    }

    try {
        const response = await fetch("/run-scan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                type: scanType,
                target: target
            })
        });

        const data = await response.json();

        if (!response.ok) {
            // Backend error message
            throw new Error(data.error || "Scan failed");
        }

        renderResults(data);

    } catch (err) {
        console.error(err);
        output.textContent = `❌ Scan Failed: ${err.message}`;
    }
});

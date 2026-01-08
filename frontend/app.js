async function runScan() {
    const target = document.getElementById("target").value;
    const scanType = document.getElementById("scanType").value;

    const response = await fetch("http://127.0.0.1:5000/run-scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            type: scanType,
            target: target
        })
    });

    const data = await response.json();
    document.getElementById("output").textContent =
        JSON.stringify(data, null, 2);
}

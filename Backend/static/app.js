document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("runScanBtn").addEventListener("click", () => {
        const target = document.getElementById("target").value.trim();
        const scanType = document.getElementById("scanType").value;

        if (!target) {
            alert("Enter a target");
            return;
        }

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
            alert("Scan failed");
        });
    });

});

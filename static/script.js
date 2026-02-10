const textarea = document.getElementById("textInput");
const charCount = document.getElementById("charCount");

/* Character counter */
textarea.addEventListener("input", () => {
    charCount.textContent = `${textarea.value.length} characters`;
});

function analyzeText() {
    const text = textarea.value.trim();
    const resultBox = document.getElementById("result");
    const loader = document.getElementById("loader");
    const button = document.getElementById("analyzeBtn");

    if (text.length === 0) {
        resultBox.innerHTML =
            "<div class='error'>⚠ Please enter some text.</div>";
        return;
    }

    /* UI loading state */
    loader.classList.remove("hidden");
    resultBox.innerHTML = "";
    button.disabled = true;
    button.innerText = "Analyzing...";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => {
        if (!response.ok) throw new Error("Server error");
        return response.json();
    })
    .then(data => {
        const type = data.prediction === 1 ? "threat" : "safe";
        const icon = data.prediction === 1 ? "⚠" : "✔";

        resultBox.innerHTML = `
            <div class="result-card ${type}">
                <h3>${icon} ${data.meaning}</h3>
                <p><strong>Prediction:</strong> ${data.prediction}</p>
            </div>
        `;
    })
    .catch(() => {
        resultBox.innerHTML =
            "<div class='error'>❌ Unable to analyze. Try again.</div>";
    })
    .finally(() => {
        loader.classList.add("hidden");
        button.disabled = false;
        button.innerText = "Analyze Threat";
    });
}

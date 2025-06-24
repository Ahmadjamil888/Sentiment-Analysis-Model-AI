async function getSentiment() {
    const text = document.getElementById("inputText").value;
    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    const data = await response.json();
    document.getElementById("result").innerText = "Sentiment: " + data.sentiment;
}

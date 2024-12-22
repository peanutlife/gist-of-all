document.getElementById('summarize-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const url = document.getElementById('url').value;
    const keywords = document.getElementById('keywords').value.split(',').map(k => k.trim());

    const response = await fetch('http://127.0.0.1:5000/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url, keywords })
    });

    const result = await response.json();
    document.getElementById('summary-result').textContent = result.summary || 'No summary available';
});

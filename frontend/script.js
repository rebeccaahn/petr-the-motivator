// Update with proper ngrok link before running the website
fetch("https://api.codetabs.com/v1/proxy?quest=https://paste-your-ngrok-link-here.ngrok.io/compliment/random")
    .then(res => res.json())
    .then(data => {
        document.getElementById('comp').innerHTML = data.compliment
    });
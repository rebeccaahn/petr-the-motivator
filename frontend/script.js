// Example: https://api.codetabs.com/v1/proxy?quest=https://c76b-128-195-97-145.ngrok.io/compliment/random
fetch("https://api.codetabs.com/v1/proxy?quest=https://paste-your-ngrok-link-here.ngrok.io/compliment/random")
    .then(res => res.json())
    .then(data => {
        document.getElementById('display').innerHTML = data.compliment
    });
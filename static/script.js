function generatePrompt() {
  const task = document.getElementById('task').value;
  const category = document.getElementById('category').value;
  const tone = document.getElementById('tone').value;

  fetch('/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: `task=${encodeURIComponent(task)}&category=${encodeURIComponent(category)}&tone=${encodeURIComponent(tone)}`
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('output').value = data.prompt;
  });
}

function copyPrompt() {
  const output = document.getElementById('output');
  output.select();
  document.execCommand('copy');
  alert("Prompt Copied to Clipboard! 🔥");
}

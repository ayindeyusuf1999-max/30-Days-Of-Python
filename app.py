from flask import Flask, request, jsonify
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>AI Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; background: #f5f5f5; }
        h1 { color: #333; }
        #chat-box { background: white; border-radius: 10px; padding: 20px; height: 400px; overflow-y: auto; margin-bottom: 20px; border: 1px solid #ddd; }
        .user-msg { background: #007bff; color: white; padding: 10px; border-radius: 10px; margin: 5px 0; text-align: right; }
        .bot-msg { background: #e9e9e9; color: #333; padding: 10px; border-radius: 10px; margin: 5px 0; }
        #input-area { display: flex; gap: 10px; }
        #message { flex: 1; padding: 10px; border-radius: 5px; border: 1px solid #ddd; font-size: 16px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>🤖 AI Chatbot</h1>
    <div id="chat-box"></div>
    <div id="input-area">
        <input type="text" id="message" placeholder="Type your message..." onkeypress="if(event.key==='Enter') sendMessage()">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        function sendMessage() {
            const input = document.getElementById('message');
            const chatBox = document.getElementById('chat-box');
            const message = input.value.trim();
            if (!message) return;
            chatBox.innerHTML += '<div class="user-msg">' + message + '</div>';
            input.value = '';
            fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: message})
            })
            .then(r => r.json())
            .then(data => {
                chatBox.innerHTML += '<div class="bot-msg">🤖 ' + data.response + '</div>';
                chatBox.scrollTop = chatBox.scrollHeight;
            });
        }
    </script>
</body>
</html>
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_input}]
    )
    return jsonify({"response": message.content[0].text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

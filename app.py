from flask import Flask, request, jsonify
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/")
def home():
    return "<h1>AI Chatbot</h1><p>POST to /chat with JSON: {message: your message}</p>"

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
    app.run(host="0.0.0.0", port=5000)

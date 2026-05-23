import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

print("AI Chatbot - type 'quit' to exit")
print("----------------------------------")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot: " + message.content[0].text)
    print()

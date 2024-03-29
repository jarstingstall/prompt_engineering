import os

from dotenv import load_dotenv
import promptlayer

load_dotenv()

promptlayer.api_key = os.getenv("PROMPTLAYER_API_KEY")
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    user_input = input("User: ")
    messages.append({"role": "user", "content": user_input})
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    assistant_msg = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_msg})
    print(f"\nAssistant: {assistant_msg}")

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

with open("code_example.py", "r") as f:
    code = f.read()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a code review assistant. Provide detailed suggestions to improve the give python code.",
        },
        {"role": "user", "content": code},
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)

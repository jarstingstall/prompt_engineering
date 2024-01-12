from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

user_input = input("What can I help you with today? ")
chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': user_input},
    ],
    model="gpt-3.5-turbo",
    temperature=0.5,
    max_tokens=1024,
)

print(chat_completion.choices[0].message.content)

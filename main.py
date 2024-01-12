from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Which NFL team plays in Cincinnati?'},
    ],
    model="gpt-3.5-turbo",
    temperature=0.5,
    max_tokens=1024,
)

print(chat_completion.choices[0].message.content)

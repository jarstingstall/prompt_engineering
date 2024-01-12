import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather for a location."""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


def run():
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather for a location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, for example San Francisco, CA",
                        },
                        "unit": {
                            "type": "string",
                            "description": "The unit of temperature to return, e.g. fahrenheit or celsius",
                            "enum": ["fahrenheit", "celsius"],
                        },
                    },
                    "required": ["location"],
                },
            },
        },
    ]

    messages = [{"role": "user", "content": "What's the weather like in Boston?"}]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        tools=tools,
        tool_choice="auto",
    )
    first_response_msg = chat_completion.choices[0].message
    messages.append(first_response_msg)

    if first_response_msg.tool_calls:
        tool_call = first_response_msg.tool_calls[0]
        functions = {"get_current_weather": get_current_weather}
        function_name = tool_call.function.name
        function_arguments = json.loads(tool_call.function.arguments)
        function = functions[function_name]
        response = function(**function_arguments)

        messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": response,
            }
        )

        second_response = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )
        print(second_response.choices[0].message.content)


if __name__ == "__main__":
    run()

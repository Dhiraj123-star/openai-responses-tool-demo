import json
from config import client 
from tools import get_weather
tools =[
    {
        "type":"function",
        "name":"get_weather",
        "description":"Get the current weather in a given city",
        "parameters": {
            "type":"object",
            "properties":{
                "city":{"type":"string"}
            },
            "required":["city"],
            "additionalProperties":False
        },
    }
]
user_input = input("Ask something...  \n")
response = client.responses.create(
    model="gpt-4.1-mini",
    input=user_input,
    tools=tools
)


# Check if model called a tool
tool_call= response.output[0]

if tool_call.type=="function_call":
    arguments = json.loads(tool_call.arguments)
    city= arguments['city']

    # Execute the tool
    result = get_weather(city)

    # Send tool result back to OpenAI
    final_response = client.responses.create(
        model="gpt-4.1-mini",
        previous_response_id=response.id,
        input =[
            {
                "type":"function_call_output",
                "call_id":tool_call.call_id,
                "output":result
            }
        ]
    )
    print("\nFinal Answer")
    print(final_response.output_text)
import json
from app.config import client
from app.tools import get_weather

tools = [
    {
        "type":"function",
        "name":"get_weather",
        "description":"Get the current weather in a city",
        "parameters":{
            "type":"object",
            "properties":{
                "city":{"type":"string"}
            },
            "required":["city"],
            "additionalProperties":False
        } 
    }
]

def ask_ai(question:str):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question,
        tools=tools
    )
    tool_call= response.output[0]
    if tool_call.type=="function_call":
        args = json.loads(tool_call.arguments)
        result = get_weather(args["city"])

        final_response = client.responses.create(
            model="gpt-4.1-mini",
            previous_response_id = response.id,
            input = [
                {
                    "type":"function_call_output",
                    "call_id":tool_call.call_id,
                    "output":result
                }
            ]
        )

        return final_response.output_text
    
    return response.output_text
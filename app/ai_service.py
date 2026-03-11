import json
from app.config import client
from app.tools import get_weather,calculate,get_time
from app.tool_registry import tools

TOOL_MAP={
    "get_weather":get_weather,
    "calculate":calculate,
    "get_time":get_time
}

def ask_ai(question:str):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question,
        tools=tools
    )
    tool_call= response.output[0]
    if tool_call.type=="function_call":
        tool_name = tool_call.name
        args = json.loads(tool_call.arguments)
        tool_function= TOOL_MAP[tool_name]
        tool_result = tool_function(**args)

        final_response = client.responses.create(
            model="gpt-4.1-mini",
            previous_response_id = response.id,
            input = [
                {
                    "type":"function_call_output",
                    "call_id":tool_call.call_id,
                    "output":tool_result
                }
            ]
        )

        return final_response.output_text
    
    return response.output_text
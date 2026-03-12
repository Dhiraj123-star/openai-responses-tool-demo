import json
from app.config import client
from app.tools import get_weather,calculate,get_time
from app.tool_registry import tools

# Tool mapping
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
    while True:
        # if the model produced final text response
        if response.output_text:
            return response.output_text
        
        tool_outputs =[]

        for item in response.output:
            if item.type=="function_call":
                tool_name = item.name
                args= json.loads(item.arguments)

                tool_function = TOOL_MAP.get(tool_name)

                if tool_function is None:
                    continue
                result = tool_function(**args)

                tool_outputs.append(
                    {
                        "type":"function_call_output",
                        "call_id": item.call_id,
                        "output":result
                    }
                )
        # send tool results back to the model
        response = client.responses.create(
            model="gpt-4.1-mini",
            previous_response_id=response.id,
            input=tool_outputs
        )
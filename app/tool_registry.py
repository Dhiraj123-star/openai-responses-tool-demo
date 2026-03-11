tools = [
    {
        "type":"function",
        "name":"get_weather",
        "description":"Get the weather for ac city",
        "parameters":{
            "type":"object",
            "properties":{
                "city":{"type":"string"}
            },
            "required": ["city"],
            "additionalProperties":False
        }
    },
    {
        "type":"function",
        "name":"calculate",
        "description":"Evaluate a math expression",
        "parameters":{
            "type":"object",
            "properties":{
                "expression":{"type":"string"}
            },
            "required":["expression"],
            "additionalProperties":False
        }
    },
    {
        "type":"function",
        "name":"get_time",
        "description":"Get current time",
        "parameters":{
            "type":"object",
            "properties":{
                "city":{"type":"string"}
            },
            "required":["city"],
            "additionalProperties": False
        }
    }
]
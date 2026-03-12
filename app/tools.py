from datetime import datetime,timezone

def get_weather(city:str):
    """
    Dummy weather tool.
    """
    return f"The weather in {city} is 30°C and sunny."

def calculate(expression: str):
    """ 
    Simple calculator 
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid Calculation!!"

def get_time(city: str):
    """ 
    Dummy time tool. 
    """
    now = datetime.now(timezone.utc).strftime("%H:%M:%S")
    return f"The current UTC time is {now} "
def get_weather(city):
    return {
        "city": city,
        "temp": 23
    }

weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string"
            }
        },
        "required": ["city"]
    },
    "handler": get_weather
}
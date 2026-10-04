def get_time(city):
    return {
        "city": city,
        "time": "14:25"
    }

time_tool = {
    "name": "get_time",
    "description": "Get the current time for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string"
            }
        },
        "required": ["city"]
    },
    "handler": get_time
}
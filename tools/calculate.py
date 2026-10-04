def calculate(expression):
    return {
        "expression": expression
    }

calculate_tool = {
    "name": "calculate",
    "description": "calculate an expression.",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string"
            }
        },
        "required": ["expression"]
    },
    "handler": calculate
}
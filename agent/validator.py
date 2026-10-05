type_mapping = {
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "object": dict,
    "array": list,
}


def validate_tool_call(tool, arguments):
    required_parameters = tool["parameters"]["required"]
    properties = tool["parameters"]["properties"]

    for parameter in required_parameters:
        if parameter not in arguments:
            return {
                "success": False,
                "error": f"Missing required parameter: {parameter}"
            }

    for argument in arguments:
        if argument not in properties:
            return {
                "success": False,
                "error": f"Unknown parameter: {argument}"
            }

    for argument, value in arguments.items():
        expected_type = properties[argument]["type"]
        expected_python_type = type_mapping[expected_type]

        if expected_type in ("integer", "number") and isinstance(value, bool):
            return {
                "success": False,
                "error": f"Invalid type for parameter: {argument}"
            }

        if not isinstance(value, expected_python_type):
            return {
                "success": False,
                "error": f"Invalid type for parameter: {argument}"
            }

    return {
        "success": True
    }
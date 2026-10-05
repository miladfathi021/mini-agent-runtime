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


    return {
        "success": True
    }
def build_tool_definition(tool):
    new_tool = tool.copy()
    new_tool.pop("handler", None)
    return {
        "type": "function",
        "function": new_tool
    }


def build_tool_definitions(tools):
    return [build_tool_definition(tool) for tool in tools]
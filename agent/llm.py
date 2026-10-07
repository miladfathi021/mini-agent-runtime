def build_tool_definition(tool):
    new_tool = tool.copy()
    new_tool.pop("handler", None)
    return {
        "type": "function",
        "function": new_tool
    }

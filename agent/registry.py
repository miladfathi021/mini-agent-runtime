class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, tool):
        self._tools[tool["name"]] = tool
    
    def has(self, tool_name):
        return tool_name in self._tools

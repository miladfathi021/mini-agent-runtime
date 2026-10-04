class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, tool):
        self._tools[tool["name"]] = tool
    
    def has(self, tool_name):
        return tool_name in self._tools

    def get(self, tool_name):
        return self._tools.get(tool_name)

    def get_lists(self):
        return list(self._tools.keys())
class AgentRuntime:
    def __init__(self, registry):
        self.registry = registry

    def execute_tool(self, tool_call):
        if not self.registry.has(tool_call["name"]):
            return {
                "success": False,
                "error": f"Tool '{tool_call['name']}' not found."
            }


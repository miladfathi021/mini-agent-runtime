from agent.validator import validate_tool_call

class AgentRuntime:
    def __init__(self, registry):
        self.registry = registry

    def execute_tool(self, tool_call):
        if not self.registry.has(tool_call["name"]):
            return {
                "success": False,
                "error": f"Tool '{tool_call['name']}' not found."
            }

        tool = self.registry.get(tool_call["name"])
        arguments = tool_call.get("arguments", {})

        validation = validate_tool_call(tool, arguments)

        if not validation["success"]:
            return validation


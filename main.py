from agent.registry import ToolRegistry
from tools.weather import weather_tool
from tools.time import time_tool
from tools.calculate import calculate_tool
from agent.llm import build_tool_definitions
from agent.runtime import AgentRuntime

registry = ToolRegistry()

registry.register(weather_tool)
registry.register(time_tool)
registry.register(calculate_tool)

runtime = AgentRuntime(registry)

# print(build_tool_definitions([weather_tool, time_tool, calculate_tool]))
# print('----------')

tool_call = {
    "name": "get_weather",
    "arguments": {
        "city": "Berlin"
    }
}

is_valid = runtime.execute_tool(tool_call)

print(is_valid)
from agent.registry import ToolRegistry
from agent.runtime import AgentRuntime

def test_execute_tool():
    registry = ToolRegistry()

    def fake_weather(city):
        return {
            "city": city,
            "temp": 29
        }

    tool = {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                }
            },
            "required": ["city"]
        },
        "handler": fake_weather
    }

    registry.register(tool)
    runtime = AgentRuntime(registry)

    tool_call = {
        "name": "get_weather",
        "arguments": {
            "city": "Tehran"
        }
    }

    result = runtime.execute_tool(tool_call)

    assert result["success"] is True
    assert result["result"]["city"] == "Tehran"

def test_unknown_tool():
    registry = ToolRegistry()

    runtime = AgentRuntime(registry)

    tool_call = {
        "name": "unknown_tool",
        "arguments": {
            "city": "Tehran"
        }
    }

    result = runtime.execute_tool(tool_call)

    assert result["success"] is False
    assert result["error"] == "Tool 'unknown_tool' not found."

def test_missing_required_argument():
    registry = ToolRegistry()

    def fake_weather(city):
        return {
            "city": city,
            "temp": 23
        }

    tool = {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string"
                }
            },
            "required": ["city"]
        },
        "handler": fake_weather
    }

    registry.register(tool)
    runtime = AgentRuntime(registry)

    tool_call = {
        "name": "get_weather",
        "arguments": {}
    }

    result = runtime.execute_tool(tool_call)

    assert result["success"] is False
    assert result["error"] == "Missing required parameter: city"


def test_unknown_argument():
    registry = ToolRegistry()

    def fake_weather(city):
        return {
            "city": city,
            "temp": 23
        }

    tool = {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string"
                }
            },
            "required": ["city"]
        },
        "handler": fake_weather
    }

    registry.register(tool)
    runtime = AgentRuntime(registry)

    tool_call = {
        "name": "get_weather",
        "arguments": {
            "city": "Tehran",
            "country": "Iran"
        }
    }

    result = runtime.execute_tool(tool_call)

    assert result["success"] is False
    assert result["error"] == "Unknown parameter: country"


from agent.loop import AgentLoop
from agent.state import AgentState
from agent.checkpoint import Checkpoint

class FakeLLM:
    def __init__(self):
        self.count = 0

    def generate(self, messages):
        self.count += 1

        if messages[0]["content"] == "final":
            return {
                "type": "final",
                "content": "Hello"
            }

        if self.count == 1:
            return {
                "type": "tool_call",
                "tool_call": {
                    "id": "call_223",
                    "name": "get_weather",
                    "arguments": {
                        "city": "Tehran"
                    }
                }
            }
        
        return {
                "type": "final",
                "content": "Weather in Tehran is 23 degrees."
            }

class FakeRuntime:
    def execute_tool(self, tool_call):
        return {
            "city": "Tehran",
            "temp": 23
        }

class InfiniteToolCallLLM:
    def generate(self, messages):
        return {
            "type": "tool_call",
            "tool_call": {
                "id": "call_999",
                "name": "get_weather",
                "arguments": {
                    "city": "Tehran"
                }
            }
        }


def test_final_response(tmp_path):
    llm = FakeLLM()
    runtime = FakeRuntime()
    checkpoint = Checkpoint(tmp_path / "checkpoint.json")

    loop = AgentLoop(llm, runtime, checkpoint)

    messages = [{
        "role": "user",
        "content": "final"
    }]

    state = AgentState(messages)

    result = loop.run(state)

    assert result == "Hello"


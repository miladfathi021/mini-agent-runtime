class AgentLoop:
    max_iterations = 10

    def __init__(self, llm, runtime):
        self.llm = llm
        self.runtime = runtime

    def run(self, state):
        while state.current_iteration < self.max_iterations:

            state.increment_current_iteration()

            response = self.llm.generate(state.messages)

            if response["type"] == "final":
                state.add_message({
                    "role": "assistant",
                    "content": response["content"]
                })
                return response["content"]

            if response["type"] == "tool_call" and response["tool_call"]:
                tool_call = response["tool_call"]

                state.add_message({
                    "role": "assistant",
                    "tool_call": tool_call
                })

                runtime_result = self.runtime.execute_tool(tool_call)

                state.add_message({
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": runtime_result
                })

        return {
            "success": False,
            "error": "Max iterations exceeded."
        }
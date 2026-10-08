import json
from agent.state import AgentState

class Checkpoint:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, state):
        state_dict = state.to_dict()

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(state_dict, file, ensure_ascii=False)


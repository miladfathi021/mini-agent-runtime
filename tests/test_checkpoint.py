from agent.state import AgentState
from agent.checkpoint import Checkpoint
from pathlib import Path
import json


def test_checkpoint_creates_snapshot(tmp_path):
    state = AgentState([
        {
            "role": "user",
            "content": "Hello"
        }
    ])

    state.increment_current_iteration()

    checkpoint = Checkpoint(tmp_path / "checkpoint.json")
    checkpoint.save(state)

    state.increment_current_iteration()

    restored_state = checkpoint.load()

    assert restored_state.current_iteration == 1
    assert state.current_iteration == 2

def test_checkpoint_saves_state_to_file(tmp_path):
    state = AgentState([
        {
            "role": "user",
            "content": "Hello"
        }
    ])

    state.increment_current_iteration()
    state.increment_current_iteration()

    temp_path = tmp_path / "snapshot.json"

    checkpoint = Checkpoint(temp_path)
    checkpoint.save(state)

    assert temp_path.is_file()

def test_checkpoint_saves_correct_state_to_file(tmp_path):
    state = AgentState([
        {
            "role": "user",
            "content": "What is the weather of Tehran?"
        }
    ])

    state.increment_current_iteration()

    temp_path = tmp_path / "snapshot.json"

    checkpoint = Checkpoint(temp_path)
    checkpoint.save(state)

    state.increment_current_iteration()
    state.add_message({
        "role": "assistant",
        "tool_call": {
            "name": "get_weather",
            "parameters": {
                "city": "Tehran"
            }
        }
    })
    
    with open(temp_path, "r") as file:
        data = json.load(file)

    assert data["messages"] == [
        {
            "role": "user",
            "content": "What is the weather of Tehran?"
        }
    ]
    assert data["current_iteration"] == 1

def test_checkpoint_load_returns_none_when_file_does_not_exist(tmp_path):
    temp_path = tmp_path / "snapshot.json"
    checkpoint = Checkpoint(temp_path)
    checkpoint_load = checkpoint.load()

    assert checkpoint_load is None

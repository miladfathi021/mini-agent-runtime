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

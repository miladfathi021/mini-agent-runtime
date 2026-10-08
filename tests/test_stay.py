from agent.state import AgentState

def test_state_to_dict():

    message = [{
        "role": "user",
        "content": "what is the weather of Tehran?"
    }]

    state = AgentState(message)

    new_message = {
        "role": "assistant",
        "content": "the weather of Tehran is 23"
    }

    state.add_message(new_message)
    state.increment_current_iteration()

    state_dict = state.to_dict()

    assert state_dict["current_iteration"] == 1
    assert state_dict["messages"][0] == {
        "role": "user",
        "content": "what is the weather of Tehran?"
    }
    assert state_dict["messages"][1] == {
        "role": "assistant",
        "content": "the weather of Tehran is 23"
    }

def test_state_from_dict():
    state_dict = {
        "messages": [
            {
                "role": "user",
                "content": "what is the weather of Tehran?"
            },
            {
                "role": "assistant",
                "content": "the weather of Tehran is 23"
            }
        ],
        "current_iteration": 2
    }

    state = AgentState.from_dict(state_dict)

    assert state.current_iteration == 2
    assert state.messages == state_dict["messages"]

    
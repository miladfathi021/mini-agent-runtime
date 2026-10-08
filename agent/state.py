class AgentState:
    def __init__(self, messages):
        self.messages = messages
        self.current_iteration = 0


    def add_message(self, message):
        self.messages.append(message)

    def increment_current_iteration(self):
        self.current_iteration += 1

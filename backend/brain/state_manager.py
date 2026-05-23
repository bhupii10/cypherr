from datetime import datetime


class StateManager:
    def __init__(self):
        self.conversation_history = []
        self.current_state = "IDLE"

    def set_state(self, state):
        self.current_state = state

    def get_state(self):
        return self.current_state

    def add_message(self, role, content):
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })

    def get_history(self):
        return self.conversation_history

    def clear_history(self):
        self.conversation_history = []
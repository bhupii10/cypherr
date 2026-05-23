class Router:
    def __init__(self):
        pass

    def route(self, text):
        """
        Temporary routing logic.

        Later this will become:
        - LLM tool routing
        - intent classification
        - multi-step planning
        """

        text = text.lower()

        command_keywords = [
            "open",
            "close",
            "launch",
            "start",
            "run"
        ]

        for keyword in command_keywords:
            if keyword in text:
                return "COMMAND"

        return "CONVERSATION"
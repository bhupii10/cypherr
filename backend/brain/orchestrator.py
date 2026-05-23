from brain.router import Router
from brain.state_manager import StateManager

from tools.tool_executor import ToolExecutor


class Orchestrator:

    def __init__(self):

        self.router = Router()

        self.state_manager = StateManager()

        self.tool_executor = ToolExecutor()

    def handle_input(self, text):

        self.state_manager.add_message(
            "user",
            text
        )

        route = self.router.route(text)

        if route == "COMMAND":

            return self.handle_tool_request(text)

        return self.handle_conversation(text)

    def handle_tool_request(self, text):

        self.state_manager.set_state("EXECUTING")

        tool_name = self.determine_tool(text)

        if not tool_name:

            self.state_manager.set_state("IDLE")

            return {
                "type": "tool",
                "success": False,
                "error": "No matching tool found."
            }

        result = self.tool_executor.execute(
            tool_name,
            text
        )

        self.state_manager.add_message(
            "assistant",
            str(result)
        )

        self.state_manager.set_state("IDLE")

        return {
            "type": "tool",
            "data": result
        }

    def determine_tool(self, text):

        text = text.lower()

        if "notepad" in text:
            return "open_notepad"

        return None

    def handle_conversation(self, text):

        self.state_manager.set_state("PROCESSING")

        response_text = (
            "Conversational intelligence layer "
            "will be connected soon."
        )

        self.state_manager.add_message(
            "assistant",
            response_text
        )

        self.state_manager.set_state("IDLE")

        return {
            "type": "conversation",
            "response": response_text
        }
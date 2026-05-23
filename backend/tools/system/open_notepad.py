import os

from tools.base_tool import BaseTool


class OpenNotepadTool(BaseTool):

    name = "open_notepad"

    description = "Opens Windows Notepad"

    def run(self, input_text):

        os.system("start notepad")

        return "Notepad opened successfully."
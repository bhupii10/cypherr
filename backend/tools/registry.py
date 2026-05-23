from tools.system.open_notepad import OpenNotepadTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "open_notepad": OpenNotepadTool()
        }

    def get_tool(self, tool_name):

        return self.tools.get(tool_name)

    def list_tools(self):

        return list(self.tools.keys())
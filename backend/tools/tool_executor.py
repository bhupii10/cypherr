from tools.registry import ToolRegistry


class ToolExecutor:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, tool_name, input_text):

        tool = self.registry.get_tool(tool_name)

        if not tool:

            return {
                "success": False,
                "error": f"Tool '{tool_name}' not found."
            }

        try:

            result = tool.run(input_text)

            return {
                "success": True,
                "tool": tool_name,
                "result": result
            }

        except Exception as e:

            return {
                "success": False,
                "tool": tool_name,
                "error": str(e)
            }
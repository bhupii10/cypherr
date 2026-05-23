class BaseTool:
    name = ""
    description = ""

    def run(self, input_text):
        raise NotImplementedError
import webbrowser
import subprocess
import os


def execute_command(command: str):

    command = command.lower().strip()

    if "open chrome" in command:

        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        for path in chrome_paths:

            if os.path.exists(path):

                subprocess.Popen([path])

                return "Opening Chrome"

        return "Chrome not found"

    elif "open notepad" in command:

        subprocess.Popen("notepad")

        return "Opening Notepad"

    elif "open youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    elif command.startswith("search google for"):

        query = command.replace(
            "search google for",
            ""
        ).strip()

        if not query:
            return "Empty search query"

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        return f"Searching Google for {query}"

    return "Unknown command"
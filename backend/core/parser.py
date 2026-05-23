def normalize_text(text: str):

    text = text.lower().strip()

    replacements = {
        "note pad": "notepad",
        "youtube.com": "youtube",
        "google chrome": "chrome",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def parse_command(text: str):

    text = normalize_text(text)

    if "open chrome" in text:
        return "open chrome"

    elif "open notepad" in text:
        return "open notepad"

    elif "open youtube" in text:
        return "open youtube"

    elif "search google for" in text:
        return text

    return None 
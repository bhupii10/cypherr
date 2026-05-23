import json
import sys

from audio.recorder import record_audio
from stt.transcriber import transcribe_audio

from brain.orchestrator import Orchestrator


orchestrator = Orchestrator()


def send_event(event_type, data=None):

    payload = {
        "type": event_type,
        "data": data
    }

    print(json.dumps(payload))

    sys.stdout.flush()


def main():

    try:

        send_event("state", "LISTENING")

        audio_path = record_audio("output.wav")

        send_event("state", "PROCESSING")

        transcription = transcribe_audio(audio_path)

        send_event("transcription", transcription)

        response = orchestrator.handle_input(transcription)

        send_event("assistant_response", response)

        send_event(
            "conversation_history",
            orchestrator.state_manager.get_history()
        )

        send_event(
            "state",
            orchestrator.state_manager.get_state()
        )

    except Exception as e:

        send_event("error", str(e))


if __name__ == "__main__":
    main()
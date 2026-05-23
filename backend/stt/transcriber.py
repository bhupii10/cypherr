from faster_whisper import WhisperModel


class Transcriber:

    def __init__(self):

        print("Loading Whisper large-v3 model...")

        self.model = WhisperModel(
            "large-v3",
            device="cuda",
            compute_type="float16"
        )

        print("Whisper model loaded successfully.")

    def transcribe_audio(self, audio_path):

        segments, info = self.model.transcribe(
            audio_path,
            beam_size=5
        )

        transcription = ""

        for segment in segments:

            transcription += segment.text + " "

        return transcription.strip()


transcriber = Transcriber()


def transcribe_audio(audio_path):

    return transcriber.transcribe_audio(audio_path)
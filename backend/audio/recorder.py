import sounddevice as sd

from scipy.io.wavfile import write

import numpy as np


SAMPLE_RATE = 16000

DURATION = 5


def record_audio(output_path="output.wav"):

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype=np.int16
    )

    sd.wait()

    write(output_path, SAMPLE_RATE, recording)

    return output_path
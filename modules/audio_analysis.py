import librosa
import numpy as np


def analyze_audio(audio_path):
    """
    Analyze speech audio and return basic metrics.
    """

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Duration
    duration = librosa.get_duration(y=y, sr=sr)

    # Energy
    rms = librosa.feature.rms(y=y)[0]
    avg_energy = np.mean(rms)

    # Zero Crossing Rate (approximate speech activity)
    zcr = librosa.feature.zero_crossing_rate(y)[0]

    # Pause detection
    pauses = np.sum(rms < 0.02)
    pause_percentage = (pauses / len(rms)) * 100

    return {
        "duration": round(duration, 2),
        "energy": round(float(avg_energy), 4),
        "speech_rate": round(float(np.mean(zcr) * 100), 2),
        "pause_percentage": round(float(pause_percentage), 2)
    }
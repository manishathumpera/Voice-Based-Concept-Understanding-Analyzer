import os


def ensure_directories():
    """
    Create required project folders if they do not exist.
    """
    folders = [
        "reports",
        "assets",
        "sample_audio"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def allowed_audio(filename):
    """
    Check supported audio formats.
    """
    return filename.lower().endswith(
        (".wav", ".mp3", ".m4a", ".flac")
    )
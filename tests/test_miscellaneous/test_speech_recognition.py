from pathlib import Path
import speech_recognition as sr
import pytest

path_to_test_file = Path(__file__).parents[2] / "data" / "downloads" / "test_audio.mp4"


def recognize_speech_from_file(path_to_file: Path) -> str:
    """
    Recognize speech from a file.
    """
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(str(path_to_file))

    with audio_file as source:
        audio_data = recognizer.record(source)

    text = recognizer.recognize_tensorflow(audio_data)

    return text


@pytest.mark.xfail(reason="Trouble implementing speech to text tool")
def test_recognize_speech_from_file():
    text = recognize_speech_from_file(path_to_test_file)
    assert isinstance(text, str), text


if __name__ == "__main__":
    test_recognize_speech_from_file()
    print("Test passed")

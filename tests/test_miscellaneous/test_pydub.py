from pydub import AudioSegment
from pathlib import Path

from tests.test_miscellaneous.conftest_ import TASK_ID_WITH_AUDIO


def test_pydub():
    """Test the `pydub` library."""

    path_to_sample_task_files = Path(__file__).parents[2] / "data" / "sample_task_files"
    path_to_audio = path_to_sample_task_files / f"{TASK_ID_WITH_AUDIO}.mp3"
    audio = AudioSegment.from_mp3(path_to_audio)
    assert isinstance(audio, AudioSegment)


def main():
    """Main function."""

    test_pydub()
    print("Done!")


if __name__ == "__main__":
    main()

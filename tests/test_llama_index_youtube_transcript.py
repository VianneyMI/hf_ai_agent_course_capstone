from llama_index.core.schema import Document
from llama_index.readers.youtube_transcript.base import YoutubeTranscriptReader
from llama_index.readers.youtube_transcript.utils import is_youtube_video


def test_is_youtube_video():
    youtube_url_to_test = "https://www.youtube.com/watch?v=1htKBjuUWec"
    vimeo_url_to_test = "https://vimeo.com/272134160"

    assert is_youtube_video(youtube_url_to_test)
    assert not is_youtube_video(vimeo_url_to_test)


def test_youtube_transcript_reader():
    youtube_url_to_test = "https://www.youtube.com/watch?v=1htKBjuUWec"
    reader = YoutubeTranscriptReader()

    documents = reader.load_data([youtube_url_to_test])

    assert len(documents) > 0, "No documents returned"
    document = documents[0]
    assert isinstance(document, Document)

    assert document.text
    assert "extremely" in document.text.lower(), document.text[:100]


if __name__ == "__main__":
    test_is_youtube_video()
    test_youtube_transcript_reader()
    print("Test passed")

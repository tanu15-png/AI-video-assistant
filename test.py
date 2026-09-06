from utils.audio_processor import process_input
from core.transcriber import transcribe_all
import os

# source = "https://www.youtube.com/watch?v=ynhl8KjjS3Y"


source = "https://www.youtube.com/shorts/WyLTqPXV1K4"

chunks = process_input(source)
print(transcribe_all(chunks,"hinglish"))

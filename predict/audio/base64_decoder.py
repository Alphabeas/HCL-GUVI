import base64
import uuid
import os


def save_base64_audio(base64_audio, audio_format="mp3"):
    """
    Save base64 audio to temporary file.
    Uses /tmp on Render (production).
    """
    try:
        # ✅ Always use /tmp on Render
        temp_dir = '/tmp'
        
        # Decode base64
        audio_bytes = base64.b64decode(base64_audio)

        # Create unique filename
        file_path = os.path.join(
            temp_dir,
            f"{uuid.uuid4()}.{audio_format}"
        )

        # Write file
        with open(file_path, "wb") as f:
            f.write(audio_bytes)

        return file_path

    except Exception as e:
        raise Exception(f"Invalid base64 audio: {str(e)}")
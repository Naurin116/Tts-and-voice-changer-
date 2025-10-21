# Example integration with Coqui TTS (open-source).
# This is a minimal example — for emotion control you will need a model that supports style/emotion tokens
# and pass the appropriate parameters (style_wav, style, speaker, etc.)
#
# Install Coqui TTS via: pip install TTS
# Example model names: "tts_models/en/vctk/vits" (multi-speaker VITS) — replace with an emotion-capable model.

from TTS.api import TTS

# Lazy-load the model (first run downloads model)
_tts_model = None

def _get_tts(model_name="tts_models/en/vctk/vits"):
    global _tts_model
    if _tts_model is None:
        _tts_model = TTS(model_name)
    return _tts_model

def synthesize_text(text: str, emotion: str, out_path: str):
    """
    Simple wrapper. Many models accept extra args for speaker or style.
    To add emotion: choose a model trained with style/emotion tokens or use style_wav.
    """
    tts = _get_tts()
    # This call will create a WAV file at out_path
    # For emotion control, see TTS model docs (args like speaker_wav, style_wav, style, speaker)
    tts.tts_to_file(text=text, file_path=out_path)
    return out_path

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
import os, uuid
import numpy as np
import soundfile as sf

# try to import a real TTS helper if present
try:
    from src.infer.tts_infer import synthesize_text
    HAS_TTS = True
except Exception:
    HAS_TTS = False

app = FastAPI(title="Voice Emotion TTS + Voice Conversion (starter)")

@app.post("/tts")
async def tts(text: str = Form(...), emotion: str = Form("neutral")):
    """
    Generate speech from text. If a real TTS model is installed & configured,
    it will be used. Otherwise this returns a short test tone placeholder.
    """
    out_path = f"/tmp/out_{uuid.uuid4().hex}.wav"
    if HAS_TTS:
        try:
            synthesize_text(text=text, emotion=emotion, out_path=out_path)
        except Exception as e:
            return JSONResponse({"error": "TTS synthesis failed", "detail": str(e)}, status_code=500)
    else:
        # placeholder sine wave (1s)
        sr = 22050
        t = np.linspace(0, 1.0, int(sr * 1.0), False)
        x = 0.1 * np.sin(2 * np.pi * 220 * t)
        sf.write(out_path, x, sr)

    return FileResponse(out_path, media_type="audio/wav", filename=os.path.basename(out_path))

@app.post("/convert")
async def convert(file: UploadFile = File(...), target_voice: str = Form("default"), emotion: str = Form("neutral")):
    """
    Upload a wav and (placeholder) return it back.
    Later: run a voice-conversion model to convert speaker/emotion.
    """
    in_path = f"/tmp/in_{uuid.uuid4().hex}.wav"
    with open(in_path, "wb") as f:
        f.write(await file.read())

    # TODO: run voice conversion model here. For now return uploaded file.
    return FileResponse(in_path, media_type="audio/wav", filename=os.path.basename(in_path))

@app.get("/health")
def health():
    return {"status": "ok", "tts_available": HAS_TTS}

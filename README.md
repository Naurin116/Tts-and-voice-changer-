# TTS and Voice Changer

This project is a FastAPI application for text-to-speech (TTS) and voice conversion.

## Features
- FastAPI-based API for TTS and voice conversion
- Integration with Coqui TTS (example)
- Placeholder endpoints for voice conversion (add model later)

## Installation (local)
1. Clone the repository:
   ```bash
   git clone https://github.com/Naurin116/Tts-and-voice-changer-
   cd Tts-and-voice-changer-
   ```

2. Create & activate virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows (PowerShell)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. API docs:
   Open http://localhost:8000/docs

## Quick usage examples
- TTS:
  ```bash
  curl -X POST -F "text=Hello world" -F "emotion=happy" http://localhost:8000/tts --output sample.wav
  ```
- Convert (upload wav):
  ```bash
  curl -X POST -F "file=@your.wav" -F "target_voice=female" -F "emotion=angry" http://localhost:8000/convert --output converted.wav
  ```

## Notes
- This scaffold uses Coqui TTS as an example (open-source). Emotion control requires a model trained with style/emotion tokens or using style_wav.
- For voice conversion, recommended OSS projects: AutoVC, StarGAN-VC2, DiffVC — these need GPU for good quality.
- Respect consent & legal/ethical rules before cloning voices.

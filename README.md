# AI Doctor: A Multimodal Generative Chatbot with Vision and Voice

**AI Doctor** is a sophisticated, end-to-end multimodal chatbot that integrates advanced generative AI capabilities—combining image analysis, speech recognition, large language modeling, and text-to-speech—to simulate realistic doctor‑patient interactions. This project highlights expertise in generative AI, prompt engineering, and real-time voice‑vision integration.

---

## 🧠 Project Overview

* **Image input**: Users upload a medical image (e.g., skin photo).
* **Voice input**: Patients verbally describe symptoms.
* **AI analysis**: A Groq-powered multimodal LLM generates a professional-sounding medical response tailored to the visual and verbal prompt.
* **Voice output**: The AI doctor responds via synthesized speech using either gTTS or ElevenLabs.
* **Interface**: A clean Gradio-based interface enables seamless, interactive use.

---

## 🔧 Key Components

### `brain_of_the_doctor.py`

* Loads environment variables (e.g., `GROQ_API_KEY`).
* Encodes images into Base64.
* Sends multimodal (image + text) prompts to a Groq-based LLM using professional prompt engineering.

### `voice_of_the_patient.py`

* Records live audio from the mic (`SpeechRecognition`, `pydub`).
* Exports as MP3 and transcribes with Groq's Whisper model.

### `voice_of_the_doctor.py`

* Provides two TTS options:

  * **gTTS**: Lightweight and offline-friendly.
  * **ElevenLabs**: Higher fidelity voice synthesis.
* Supports audio playback on macOS, Windows, and Linux.

### `gradio_app.py`

* Combines audio and image inputs into a unified Gradio interface.
* Orchestrates the full pipeline: STT → Vision + LLM → TTS.
* Implements structured logging for debugging and monitoring.

### `requirements.txt`

Key dependencies include:

```
groq, dotenv, ffmpeg, SpeechRecognition, pydub, PyAudio,
gTTS, elevenlabs, playsound, gradio
```

---

## ⚙️ Setup & Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/Aznair25/ai-doctor.git
   cd ai-doctor
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure `.env`**

   ```
   GROQ_API_KEY=your_groq_key
   ELEVENLABS_API_KEYS=your_elevenlabs_key
   ```

4. **Run the app**

   ```bash
   python gradio_app.py
   ```

   * The UI opens locally. Speak into the mic and upload an image to interact with the AI Doctor.

---

## ⚠️ Medical Disclaimer

> **Important:** This project is strictly for educational and learning purposes only.
> I am *not a real medical doctor* nor a licensed healthcare professional.
> The AI-generated responses are *not intended* for diagnosis, treatment, or medical advice.
> In case of illness, symptoms, or medical concerns, **consult a qualified healthcare provider immediately**.

Including a clear medical disclaimer is essential to inform users that this chatbot is not a substitute for real medical expertise.

---

## 🧪 Project Highlights

* **True multimodal integration**: Combines speech and vision inputs to inform AI analysis—demonstrates mature prompt engineering and interaction design.
* **Real-time conversational loop**: Full-cycle audio capture, transcription, image interpretation, and speech synthesis—all delivered in a responsive web UI.
* **Leveraging Groq hardware/software**: Utilizes Groq's multimodal LLM inference capabilities for efficient, low-latency responses.
* **Professional-grade architecture**: Clean separation of concerns, robust error handling, and platform-independent functionality.

Multimodal generative AI is a rapidly growing field, with huge potential in conversational and assistive applications .

---

## 🧩 Skills & Learning Outcomes

This project demonstrates:

* **Advanced prompt engineering**: Crafting professional, medical-mimicking responses.
* **Voice application engineering**: Real-time audio recording, STT via Whisper, and cross-platform TTS.
* **Multimodal AI system design**: Orchestrating complex pipelines for image and audio fusion.
* **Production-level readiness**: Logging, error management, and extensible Gradio deployment.

Together, these components showcase high-level proficiency with generative AI and voice‑vision conversational systems.

---

## 💡 Future Enhancements

* 🔗 Connect to medical databases or symptom checkers for deeper insights.
* 🌐 Add multilingual modalities via Whisper + voice cloning.
* 📦 Containerize with Docker for offline and secure deployment.
* 🧠 Implement session memory for extended multi-turn medical dialogues.

---

Developed by **Azniar Manzoor**
*Showcasing expertise in generative AI, multimodal systems, and real-time voice‑vision applications.*

Katharine willingness to expand or publish this as a showcase within health‑tech communities—feel free to reach out!
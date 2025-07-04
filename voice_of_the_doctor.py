import subprocess
import platform
import os
from gtts import gTTS
def text_to_speech_with_gtts(input_text,output_file_path):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    audioobj.save(output_file_path)
    os_name=platform.system()
    try:
        if os_name=="Darwin": #mac
            subprocess.run(['afplay',output_file_path])
        elif os_name=='Windows': #windows
            from playsound import playsound
            playsound(output_file_path)
        elif os_name=="Linux": #linux
            subprocess.run(['aplay',output_file_path])
        else:
            raise OSError("Unsupported Operating System.")
    except Exception as e:
        print(f"An error occured while trying to play the audio: {e}")

import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
ELEVENLABS_API_KEYS=os.getenv("ELEVENLABS_API_KEYS")

def text_to_speech_with_elevenlabs(input_text,output_file_path):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEYS)
    audio=client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_file_path)
    os_name=platform.system()
    try:
        if os_name=="Darwin": #mac
            subprocess.run(['afplay',output_file_path])
        elif os_name=='Windows': #windows
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_file_path])
        elif os_name=="Linux": #linux
            subprocess.run(['aplay',output_file_path])
        else:
            raise OSError("Unsupported Operating System.")
    except Exception as e:
        print(f"An error occured while trying to play the audio: {e}")

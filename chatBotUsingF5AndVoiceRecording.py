import speech_recognition as sr
import subprocess
import sounddevice as sd
from pydub import AudioSegment
import io
import torch
import openai
import os
import numpy as np
import time

# Initialize F5-TTS
def generate_tts(text):
    """Generate TTS from F5-TTS and play the result"""
    # Generate a unique file name using timestamp
    timestamp = int(time.time())
    output_file = "C:/Users/arinm/OneDrive/Desktop/testing questions/TTS-F5-test/F5-TTS/tests/out.wav"
    
    # Absolute path to inference-cli.py
    inference_script = "C:/Users/arinm/OneDrive/Desktop/testing questions/TTS-F5-test/F5-TTS/inference-cli.py"
    
    # Path to the F5-TTS directory
    f5_tts_directory = "C:/Users/arinm/OneDrive/Desktop/testing questions/TTS-F5-test/F5-TTS"

    # Path to Python in F5-TTS virtual environment
    python_executable = "C:/Users/arinm/OneDrive/Desktop/testing questions/TTS-F5-test/F5-TTS/venv/Scripts/python"
    
    # Running inference and saving the audio to a unique file
    command = [
        python_executable, inference_script,
        '--model', 'F5-TTS',
        '--gen_text', text
    ]
    
    # Run the command with the correct working directory
    subprocess.run(command, cwd=f5_tts_directory)
    
    # Ensure file is saved and exists before proceeding
    if not os.path.exists(output_file):
        raise FileNotFoundError(f"Audio file {output_file} not found.")
    
    # Use Pydub to load the audio file
    audio_segment = AudioSegment.from_file(output_file, format="wav")
    
    # Extract raw audio data and convert to NumPy array
    raw_audio = np.array(audio_segment.get_array_of_samples())  # Convert to NumPy array
    sample_rate = audio_segment.frame_rate
    
    # Play audio in real-time using sounddevice
    sd.play(raw_audio, samplerate=sample_rate)
    sd.wait()

# Function to record the user's voice and convert to text
def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with Google API; {e}")
        return None

# Chatbot that communicates with the local LLM
def generate_response(prompt):
    """Use the local LLM to generate a response"""
    client = openai.OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
    
    completion = client.chat.completions.create(
        model="lmstudio-community/dolphin-2.8-mistral-7b-v02-GGUF",
        messages=[
            {"role": "system", "content": "You're a chill girl who likes to flirt."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    return completion.choices[0].message.content

# Main conversation loop
def conversation():
    print("Welcome to the voice-powered chatbot with TTS response!")
    
    while True:
        user_input = record_voice()
        if user_input is None or user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Generate response from LLM
        bot_response = generate_response(user_input)
        print("Bot:", bot_response)
        
        # Convert the response to speech and play it
        generate_tts(bot_response)

if __name__ == "__main__":
    conversation()

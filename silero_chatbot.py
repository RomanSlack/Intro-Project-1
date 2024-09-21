from langchain_ollama import OllamaLLM
import torch
import sounddevice as sd
import numpy as np
import librosa

# Initialize the LLaMA 3 model
llama_model = OllamaLLM(model="llama3")

# Load Silero TTS model
device = torch.device('cuda')  # 'cpu' for local non-GPU usage
model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language='en', 
                                     speaker='v3_en')

# Function to change the pitch of the audio
def change_pitch(audio, sr, n_steps):
    return librosa.effects.pitch_shift(audio, sr=sr, n_steps=n_steps)

# Function to stop audio playback
def stop_audio():
    sd.stop()

# Function to convert text to speech and play it with pitch adjustment
def speak_text(text):
    # Choose a higher-pitched speaker ID
    speaker_id = 'en_2'  # Try different speaker IDs for different voices

    # Generate speech from text using Silero TTS
    audio = model.apply_tts(text=text, speaker=speaker_id)
    
    # Convert the audio to numpy array if needed and adjust the pitch
    audio = np.array(audio)  # Ensure it's a numpy array
    adjusted_audio = change_pitch(audio, sr=16000, n_steps=10)  # Raise pitch by 4 semitones
    
    # Play the adjusted speech
    sd.play(adjusted_audio, samplerate=32000)  # Play at 16kHz
    sd.wait()  # Wait for playback to finish

# Function to generate a response using LLaMA 3 model and speak it
def generate_and_speak(prompt):
    # Generate a response using the LLaMA 3 model
    response = llama_model.invoke(input=prompt)

    # Print the generated response
    print("Generated Text:", response)

    # Speak the generated response
    speak_text(response)

# Main loop to take user input and speak the response
if __name__ == "__main__":
    while True:
        prompt = input("Enter a prompt for LLaMA 3 (type 'stop' to halt playback): ")

        if prompt.lower() == "stop":
            stop_audio()  # Stop the playback if user enters 'stop'
        else:
            generate_and_speak(prompt)

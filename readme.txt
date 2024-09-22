Silero Chatbot Project

This project integrates a simple chatbot using the LLaMA 3 model with Silero TTS for speech synthesis. The chatbot responds to user inputs using a pre-trained LLaMA 3 model and converts its responses to speech with pitch adjustments using Silero.

Prerequisites:
1. Download and install the Windows version of Ollama: https://ollama.com/
1.2 Download llam3 via Ollama (in cmd - Ollama pull llama3)
2. Ensure Python (preferably version 3.8 or higher) is installed.
3. Install the required packages (listed below).

Setup Instructions:

1. Create a Virtual Environment
   - Open a terminal/command prompt and navigate to your project directory.
   - Run the following command to create a virtual environment:
   
     python -m venv venv
     
   - Activate the virtual environment:
     - On Windows:
       
       venv\Scripts\activate
     - On macOS/Linux:
       
       source venv/bin/activate

2. Install Required Dependencies:
   - You can install all the required packages by using the provided requirements.txt file:
     
     pip install -r requirements.txt
     
   - Or you can install them manually by running:
     
     pip install langchain-ollama
     pip install torch
     pip install sounddevice
     pip install numpy
     pip install librosa

3. Running the Chatbot:
   - Once everything is installed, run the chatbot by typing the following command:
   
     python main.py

Project Overview:

- The chatbot uses the LLaMA 3 model to generate text responses based on user prompts.
- The generated text is passed to Silero TTS, which converts the text to speech.
- Pitch adjustments can be made, and the speech is played back using the sounddevice library.

Requirements:

The following packages are required to run the project:

langchain-ollama
torch
sounddevice
numpy
librosa

Install them by running:

pip install -r requirements.txt

Additional Resources:
- Ollama Documentation: https://ollama.com/docs
- Silero TTS: https://github.com/snakers4/silero-models

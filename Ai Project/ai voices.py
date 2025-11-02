import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to list available voices
def list_available_voices():
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name} - {voice.languages}")

# Function to set a preferred voice
def set_preferred_voice(voice_id):
    voices = engine.getProperty('voices')
    if 0 <= voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
        print(f"Voice set to: {voices[voice_id].name}")
    else:
        print("Invalid voice ID. Please select a valid one.")

# Function to respond with text-to-speech
def respond_with_speech(response_text):
    engine.say(response_text)
    engine.runAndWait()

# Main Code:
# List all voices available
list_available_voices()

# Set preferred voice by its index (e.g., 0 or 1)
set_preferred_voice(0)  # Change 1 to the desired index after listing voices

# Test speaking with the chosen voice
respond_with_speech("This is the selected voice for your assistant.")

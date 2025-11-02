import speech_recognition as sr
import pyttsx3
import sqlite3
import time
from datetime import datetime
import os
import subprocess
import requests
from bs4 import BeautifulSoup

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to list available voices
def list_available_voices():
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name} - {voice.languages}")

def respond_with_speech(response_text):
    # Set the volume to 1.0 (maximum volume)
    engine.setProperty('volume', 1.0)  # Set to maximum volume
    engine.say(response_text)
    engine.runAndWait()

# Function to set a preferred voice
def set_preferred_voice(voice_id):
    voices = engine.getProperty('voices')
    if 0 <= voice_id < len(voices):
        engine.setProperty('voice', voices[voice_id].id)
        print(f"Voice set to: {voices[voice_id].name}")
    else:
        print("Invalid voice ID. Please select a valid one.")

# Function to create a new database connection and cursor
def create_db_connection():
    conn = sqlite3.connect('assistant_data.db', check_same_thread=False)
    c = conn.cursor()
    return conn, c

# Create tables to store user data, preferences, and reminders
def initialize_database():
    conn, c = create_db_connection()
    c.execute('''CREATE TABLE IF NOT EXISTS user_data
                 (id INTEGER PRIMARY KEY, name TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS preferences
                 (id INTEGER PRIMARY KEY, preference_name TEXT, preference_value TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reminders
                 (id INTEGER PRIMARY KEY, reminder_text TEXT, reminder_datetime TEXT)''')
    conn.commit()
    conn.close()

# Initialize the database
initialize_database()

# Function to listen to the microphone and convert speech to text
def listen_to_microphone():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Capture the audio from the microphone
        try:
            print("Processing...")
            # Use Google Web Speech API to recognize the speech
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

# Function to store the user's name in the database
def store_user_name(name):
    conn, c = create_db_connection()
    c.execute("INSERT INTO user_data (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Function to get the user's name from the database
def get_user_name():
    conn, c = create_db_connection()
    c.execute("SELECT name FROM user_data ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

# Function to store a reminder with both date and time
def store_reminder(reminder, reminder_datetime):
    conn, c = create_db_connection()
    c.execute("INSERT INTO reminders (reminder_text, reminder_datetime) VALUES (?, ?)", (reminder, reminder_datetime))
    conn.commit()
    conn.close()

# Function to get all reminders
def get_reminders():
    conn, c = create_db_connection()
    c.execute("SELECT reminder_text, reminder_datetime FROM reminders")
    results = c.fetchall()
    conn.close()
    return [(result[0], result[1]) for result in results]

# Function to store a preference
def store_preference(preference_name, preference_value):
    conn, c = create_db_connection()
    c.execute("INSERT INTO preferences (preference_name, preference_value) VALUES (?, ?)", 
              (preference_name, preference_value))
    conn.commit()
    conn.close()

# Function to get a specific preference
def get_preference(preference_name):
    conn, c = create_db_connection()
    c.execute("SELECT preference_value FROM preferences WHERE preference_name = ?", (preference_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

# Function to constantly listen for the wake word "Jarvis"
def listen_for_wake_word(wake_word="open"):
    while True:
        print("Listening for wake word...")
        audio_text = listen_to_microphone()
        if audio_text and wake_word in audio_text:
            print("Edith User voice detected. Activating assistant...")
            respond_with_speech(f"Hello, how can I assist you?")
            return True

# Function to parse date and time from user input (e.g., '9:00 on 2025-02-12')
def parse_datetime(datetime_str):
    try:
        # Attempt to parse a datetime like '9:00 on 2025-02-12'
        return datetime.strptime(datetime_str, " %H:%M on %d-%m-%y")
    except ValueError:
        return None

# Function to check reminders and alert if the date and time matches
def check_for_reminders():
    while True:
        # Get current datetime
        current_datetime = datetime.now().strftime(" %H:%M on %d-%m-%y")
        
        # Fetch reminders from the database
        reminders = get_reminders()
        
        for reminder, reminder_datetime in reminders:
            # Check if it's time for the reminder (both date and time must match)
            if reminder_datetime == current_datetime:
                respond_with_speech(f"Reminder: {reminder}")
                # Delete the reminder after it has been triggered
                conn, c = create_db_connection()
                c.execute("DELETE FROM reminders WHERE reminder_datetime = ?", (reminder_datetime,))
                conn.commit()
                conn.close()
            
            # Delete reminders that have passed (older than current datetime)
            elif reminder_datetime < current_datetime:
                conn, c = create_db_connection()
                c.execute("DELETE FROM reminders WHERE reminder_datetime = ?", (reminder_datetime,))
                conn.commit()
                conn.close()
        
        time.sleep(60)  # Check every minute

# Function to open applications
def open_application(app_name):
    # Map application names to their executable paths
    app_paths = {
        "notepad": "C:\Program Files\Notepad++\notepad++.exe",
        #"calculator": "calc.exe",
        "spyder" : "C:\Program Files\Spyder\Python\pythonw.exe" "C:\Program Files\Spyder\Spyder.launch.pyw",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "spotify": "C:\\Users\\YourUsername\\AppData\\Roaming\\Spotify\\Spotify.exe",
        "microsoft edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
        "vs code": "C:\\Users\\kemis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
        # Add more applications and their paths here
    }

    if app_name in app_paths:
        try:
            subprocess.Popen(app_paths[app_name])
            respond_with_speech(f"Opening {app_name}.")
        except Exception as e:
            respond_with_speech(f"Sorry, I couldn't open {app_name}. Error: {str(e)}")
    else:
        respond_with_speech(f"Sorry, I don't know how to open {app_name}.")

# Function to fetch information from the web
def fetch_web_info(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the first few search results
    results = []
    for g in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
        results.append(g.text)
    
    if results:
        return results[:3]  # Return the first 3 results
    else:
        return ["No results found."]

# Main function
def main():
    # List all available voices
    list_available_voices()

    # Set preferred voice by its index (e.g., 1 or 2)
    set_preferred_voice(0)  # Change to the desired index after listing voices

    # Start reminder checking in a separate thread or process
    import threading
    reminder_thread = threading.Thread(target=check_for_reminders)
    reminder_thread.daemon = True  # This will allow the thread to exit when the program ends
    reminder_thread.start()
    
    while True:
        # Start listening for the wake word "Jarvis"
        if listen_for_wake_word("open"):
            # After detecting the wake word, start processing commands
            while True:
                user_input = listen_to_microphone()
                if user_input is None:
                    continue

                # Check for specific commands
                if "hello" in user_input:
                    respond_with_speech("Hello! How can I help you today?")

                elif "what can you do" in user_input:
                    respond_with_speech("I can tell time and date. I can get you information online. I can set you reminders and remind due time and or date, or tell you what are your reminders. and I can also open Applications for you.")

                elif "what is your name" in user_input:
                    respond_with_speech("my name is edith. can I get your name?")

                elif "your name" in user_input:
                    name = get_user_name()
                    if name:
                        respond_with_speech(f"My name is EDITH your personal AI assistant. I know you as {name}.")
                    else:
                        respond_with_speech("I don't know your name yet. You can tell me your name.")

                elif "my name is" in user_input:
                    # Extract name from user input
                    name = user_input.split("my name is")[-1].strip()
                    store_user_name(name)
                    respond_with_speech(f"Nice to meet you, {name}. I will remember that.")

                elif "I am" in user_input:
                    # Extract name from user input
                    name = user_input.split("my name is")[-1].strip()
                    store_user_name(name)
                    respond_with_speech(f"Nice to meet you, {name}. I will remember that.")

                elif "set a reminder" in user_input and "at" in user_input and "on" in user_input:
                    # Extract the time and date from the user input (e.g., '2025-02-12 at 9:00')
                    parts = user_input.split("on")

                    if len(parts) > 1:
                        date_part = parts[1].split("at")[0].strip()  # Date portion
                        time_part = parts[1].split("at")[1].strip() if len(parts[1].split("at")) > 1 else None  # Time portion
                        
                        if time_part:  # If time part exists, parse the datetime
                            datetime_str = f"{date_part} at {time_part}"
                            parsed_datetime = parse_datetime(datetime_str)
                        
                            if parsed_datetime:
                                store_reminder(parts[0].strip(), parsed_datetime.strftime("%H:%M on %d-%m-%y"))
                                respond_with_speech(f"Reminder set: {parts[0].strip()} at {time_part} on {date_part}.")
                            else:
                                respond_with_speech("I couldn't understand the date and time. Please try again.")
           
                        else:
                            respond_with_speech("I couldn't understand the date and time. Please try again.")

                    else:
                        respond_with_speech("I need both the date and time along with your reminder.")
                
                elif "what are my reminders" in user_input:
                    reminders = get_reminders()
                    if reminders:
                        response = "Here are your reminders: " + ", ".join([f"{reminder} on {datetime_str}" for reminder, datetime_str in reminders])
                    else:
                        response = "You don't have any reminders."
                    respond_with_speech(response)

                elif "open" in user_input:
                    # Extract the application name from the command
                    app_name = user_input.split("open")[-1].strip()
                    open_application(app_name)

                elif "search" in user_input:
                    query = user_input.split("search for")[-1].strip()
                    results = fetch_web_info(query)
                    respond_with_speech("Here are the top results I found:")
                    for result in results:
                        respond_with_speech(result)

                elif "what time is it" in user_input:
                    current_time = datetime.now().strftime("%I:%M %p")  # Format: HH:MM AM/PM
                    respond_with_speech(f"The time is {current_time}")

                elif "what date is it" in user_input:
                    current_date = datetime.now().strftime("%B %d, %Y")  # Format: Month Day, Year
                    respond_with_speech(f"Today's date is {current_date}")

                elif "close" in user_input:
                    respond_with_speech("Goodbye!")
                    break
                else:
                    respond_with_speech(f"You said: {user_input}")

# Run the program
if __name__ == "__main__":
    main()
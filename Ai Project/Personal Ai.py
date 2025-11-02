import os
import re
import time
import json
import queue
import threading
import sqlite3
import psutil
import platform
import subprocess
import concurrent.futures
import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser
import screen_brightness_control as sbc
import pyautogui
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests
from collections import deque

# ========== CONFIGURATION ==========
WAKE_WORD = "open"
PERSONAL_NAME = "Sir"
AI_NAME = "E.D.I.T.H"
DESKTOP_REPORTS_FOLDER = os.path.join(os.path.expanduser('~'), 'Desktop', 'EDITH_Reports')
os.makedirs(DESKTOP_REPORTS_FOLDER, exist_ok=True)

# ========== VOICE ENGINE ==========
class VoiceSystem:
    def __init__(self):
        self.engine = pyttsx3.init()
        self._configure_voice()
        
    def _configure_voice(self):
        """Configure deep male voice with J.A.R.V.I.S. style"""
        voices = self.engine.getProperty('voices')
        
        # Prefer these voice IDs (Windows)
        preferred_voices = [
            'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0',
            'com.apple.speech.synthesis.voice.daniel',  # Mac
            'english-mb-en1'  # Linux
        ]
        
        for voice_id in preferred_voices:
            try:
                self.engine.setProperty('voice', voice_id)
                break
            except:
                continue
        else:
            # Fallback to any male voice
            for voice in voices:
                if 'male' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
        
        # J.A.R.V.I.S. voice parameters
        self.engine.setProperty('rate', 175)
        self.engine.setProperty('volume', 0.9)
        self.engine.setProperty('pitch', 50)
    
    def speak(self, text, priority='normal'):
        """Priority levels: 'normal', 'alert', 'system'"""
        if priority == 'alert':
            self.engine.setProperty('rate', 190)
            self.engine.setProperty('volume', 1.0)
        elif priority == 'system':
            self.engine.setProperty('rate', 165)
            self.engine.setProperty('volume', 0.85)
        
        self.engine.say(text)
        self.engine.runAndWait()
        
        # Reset to defaults
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)

# ========== USER INTERFACE ==========
class AIDisplay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.85)
        self.root.configure(bg='#0a0a1a')
        
        # Setup HUD-style display
        self.canvas = tk.Canvas(self.root, width=400, height=120, bg='#0a0a1a', highlightthickness=0)
        self.canvas.pack()
        
        # Status elements
        self.status_text = tk.Label(self.root, text="SYSTEM ACTIVE", fg='#00ffaa',
                                   bg='#0a0a1a', font=('Courier New', 12, 'bold'))
        self.status_text.place(relx=0.5, rely=0.3, anchor='center')
        
        self.response_text = tk.Label(self.root, text="", fg='white', bg='#0a0a1a',
                                    font=('Courier New', 10), wraplength=380)
        self.response_text.place(relx=0.5, rely=0.65, anchor='center')
        
        # Position at bottom right
        self._position_window()
        
    def _position_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"400x120+{screen_width-420}+{screen_height-170}")
    
    def update(self, status, response):
        self.status_text.config(text=status.upper())
        self.response_text.config(text=response)
        self.root.update()

# ========== CORE FUNCTIONALITY ==========
class AIAssistant:
    def __init__(self):
        self.voice = VoiceSystem()
        self.ui = AIDisplay()
        self.recognizer = sr.Recognizer()
        self.command_queue = queue.Queue()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        self.running = True
        
        # Initialize subsystems
        self._setup_voice_authentication()
        self._start_system_monitor()
        self._start_command_processor()
        
    def _setup_voice_authentication(self):
        """Placeholder for voice recognition"""
        self.voice.speak(f"{AI_NAME} online. Authentication complete. How may I assist you, {PERSONAL_NAME}?", 'system')
    
    def _start_system_monitor(self):
        """Background system monitoring"""
        def monitor():
            while self.running:
                # Battery check
                battery = psutil.sensors_battery()
                if battery and battery.percent < 20 and not battery.power_plugged:
                    self.voice.speak(f"{PERSONAL_NAME}, battery at {battery.percent}%. Please connect to power.", 'alert')
                
                time.sleep(60)
        
        threading.Thread(target=monitor, daemon=True).start()
    
    def _start_command_processor(self):
        """Parallel command processing"""
        def processor():
            while self.running:
                command = self.command_queue.get()
                self.executor.submit(self._process_command, command)
        
        threading.Thread(target=processor, daemon=True).start()
    
    def listen(self):
        """Continuous listening with wake word detection"""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.running:
                try:
                    audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=5)
                    text = self.recognizer.recognize_google(audio).lower()
                    
                    if WAKE_WORD in text:
                        command = text.replace(WAKE_WORD, "").strip()
                        self.command_queue.put(command)
                        self.ui.update("PROCESSING", f"Executing: {command}")
                except sr.WaitTimeoutError:
                    continue
                except Exception as e:
                    print(f"Audio error: {e}")
    
    def _process_command(self, command):
        """J.A.R.V.I.S.-style command processing"""
        try:
            # System commands
            if any(w in command for w in ["hello", "hi", "hey"]):
                self.voice.speak(f"Hello {PERSONAL_NAME}. How may I assist you?")
            
            elif "time" in command:
                current_time = datetime.now().strftime("%I:%M %p")
                self.voice.speak(f"The time is {current_time}")
            
            elif "date" in command:
                current_date = datetime.now().strftime("%A, %B %d, %Y")
                self.voice.speak(f"Today is {current_date}")
            
            # Knowledge queries
            elif any(w in command for w in ["what is", "who is", "tell me about"]):
                query = command.split("is")[-1].strip()
                try:
                    summary = wikipedia.summary(query, sentences=2)
                    self.voice.speak(summary)
                except:
                    self.voice.speak(f"I couldn't find information about {query}")
            
            # System control
            elif "brightness" in command:
                current = sbc.get_brightness()[0]
                if "increase" in command:
                    sbc.set_brightness(min(current + 20, 100))
                    self.voice.speak("Brightness increased")
                elif "decrease" in command:
                    sbc.set_brightness(max(current - 20, 0))
                    self.voice.speak("Brightness decreased")
            
            else:
                self.voice.speak("Command not recognized. Please try again.")
                
            self.ui.update("READY", "Awaiting command...")
        except Exception as e:
            self.voice.speak("Processing error occurred", 'alert')
            print(f"Command error: {e}")

# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    assistant = AIAssistant()
    
    # Start continuous listening
    listen_thread = threading.Thread(target=assistant.listen, daemon=True)
    listen_thread.start()
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        assistant.running = False
        assistant.voice.speak("Shutting down systems. Goodbye.")
        time.sleep(1)
        os._exit(0)
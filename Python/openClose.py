





import tkinter as tk
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
import re

class CountdownUi:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_attributes("-transparentcolor", "black")
        self.root.wm_attributes("-alpha", 0.8)
        self.root.config(bg="black")
        self.root.geometry("100x200")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 400) // 35
        y = (screen_height - 200) // 33
        self.root.geometry(f"250x80+{x}+{y}")

        self.border_frame = tk.Frame(self.root, bg="#212121", highlightthickness=2, highlightbackground="green")
        self.border_frame.pack(fill="both", expand=True)


        self.timelabel = tk.Label(self.border_frame, text="Time left:", font=8, fg="white", bg="#212121")
        self.timelabel.pack(pady=(3, 0))

        self.count = tk.Label(self.border_frame, text="00 hrs : 00 min : 12 sec", font=("Times New Roman", 18), fg="white", bg="green")
        self.count.pack(pady=(7, 0))

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Set speech rate
        self.engine.say("Please say the time for the countdown.")
        self.engine.runAndWait()

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.get_time()

    def get_time(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            time_str = self.recognizer.recognize_google(audio)
            print(time_str)
            self.parse_time(time_str)
        except sr.UnknownValueError:
            self.engine.say("Sorry, I didn't catch that.")
            self.engine.runAndWait()
            self.get_time()

    def parse_time(self, time_str):
        hours = 0
        minutes = 0
        seconds = 0

        match = re.search(r'(\d+) hour', time_str)
        if match:
            hours = int(match.group(1))

        match = re.search(r'(\d+) minute', time_str)
        if match:
            minutes = int(match.group(1))

        match = re.search(r'(\d+) second', time_str)
        if match:
            seconds = int(match.group(1))

        self.time_left = hours * 3600 + minutes * 60 + seconds
        hours = self.time_left // 3600
        minutes = (self.time_left // 60) % 60
        seconds = self.time_left % 60
        self.count.config(text=f"{hours:02} hrs : {minutes:02} min : {seconds:02} sec")
        self.root.after(1000, self.update_countdown)

    def update_countdown(self):
        self.time_left -= 1
        hours = self.time_left // 3600
        minutes = (self.time_left // 60) % 60
        seconds = self.time_left % 60
        self.count.config(text=f"{hours:02} hrs : {minutes:02} min : {seconds:02} sec")

        if self.time_left <= 10:
            self.root.config(bg="black")
            self.timelabel.config(bg="#212121")
            self.count.config(bg="red")
            self.border_frame.config(highlightbackground="red")

        if self.time_left > 0:
            self.root.after(1000, self.update_countdown)
        else:
            self.engine.say("Time's up!")
            self.engine.runAndWait()
            self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    countdown = CountdownUi()
    countdown.run()



import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def system_check():

    check_window = tk.Tk()
    check_window.overrideredirect(True)
    check_window.title("System Check")
    check_window.geometry("400x200")
    
    # Center the window
    screen_width = check_window.winfo_screenwidth()
    screen_height = check_window.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 200) // 2
    check_window.geometry(f"400x200+{x}+{y}")
    
    # Make the window appear on top
    check_window.attributes('-topmost', True)
    
    status_label = tk.Label(check_window, text="Running system diagnostics...", font=('Arial', 12))
    status_label.pack(pady=20)
    
    progress = ttk.Progressbar(check_window, orient='horizontal', length=200, mode='indeterminate')
    progress.pack()
    progress.start()
    
    def finish_check():
        progress.stop()
        status_label.config(text="System check complete! \n Assistant ready! \n Device ready!", bg="green", font=('Arial', 12, 'bold') ,fg = "white")
        check_window.config(bg="green")
        # Close the window after 2 seconds
        check_window.after(2000, check_window.destroy)
    
    # Simulate a delay for the system check
    check_window.after(5000, finish_check)
    check_window.mainloop()




system_check()

import tkinter as tk
from tkinter import messagebox

class Gift:
    
    def __init__(self):
        
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text="Sign In", font=("Arial", 24))
        self.label.pack(padx=15, pady=15)
        
        self.label = tk.Label(self.root, text="First Name:")
        self.label.pack(padx=15, pady=5)
        self.textbox = tk.Entry(self.root, width=70)
        self.textbox.pack(padx=15, pady=5)
        
        self.label = tk.Label(self.root, text="Second Name:")
        self.label.pack(padx=15, pady=5)
        self.textbox = tk.Entry(self.root, width=70)
        self.textbox.pack(padx=15, pady=5)
        
        self.label = tk.Label(self.root, text="Email:")
        self.label.pack(padx=15, pady=5)
        self.textbox = tk.Entry(self.root, width=70)
        self.textbox.pack(padx=15, pady=5)
        
        self.label = tk.Label(self.root, text="Cell Number:")
        self.label.pack(padx=15, pady=5)
        self.textbox = tk.Entry(self.root, width=70)
        self.textbox.pack(padx=15, pady=5)
        
        self.label = tk.Label(self.root, text="Enter Password:")
        self.label.pack(padx=15, pady=5)
        self.textbox = tk.Entry(self.root, width=70)
        self.textbox.pack(padx=15, pady=5)
        
        self.label = tk.Label(self.root, text="Comfirm Password:")
        self.label.pack(padx=15, pady=5)
        self.textbox = tk.Entry(self.root, width=70)
        self.textbox.pack(padx=15, pady=5)


        self.checkState = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="Remember me", variable=self.checkState)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Login", command=self.show, bg="pink" ,width=10, height=2)
        self.button.pack(padx=10, pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.root.mainloop()

    def show(self):
        
        if self.checkState.get() == 0:
            print(self.textbox.get())
            
        else:
            messagebox.showinfo(title="Warning", message="Should we save your logins?")

    def shortcut(self, event):
        
        if event.state == 12 and event.keysym == 'Return':
            self.show()

    def close(self):
        
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

Gift()

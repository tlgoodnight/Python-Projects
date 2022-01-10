import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import os



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Change HTML File Body')
        self.geometry("500x80")

        self.name_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 5, 'pady': 5}
        # label
        ttk.Label(self, text='Replacement Text:').grid(column=0, row=0, **padding)

        # Entry
        name_entry = ttk.Entry(self, textvariable=self.name_var)
        name_entry.grid(column=1, row=0, **padding)
        name_entry.focus()

        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

    def submit(self):
        f = open("Pythonchallenge.html", "w")
        f.write(self.name_var.get())
        f.close()
        webbrowser.open_new_tab("Pythonchallenge.html")
        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()

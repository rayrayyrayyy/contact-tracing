# import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class SearchEntry(): # create class search entry

    def __init__(self):
    # create GUI window
        self.root_window = tk.Tk()
        self.root_window.title("COVID-19 Contact Tracing APP")
        self.root_window.geometry("1000x930")
        self.root_window.config( bg = "#FFF7D4" )

        self.root_window.mainloop()

    def execute(self):
        self.root_window.mainloop()

if __name__ == "__main__":
    contact_tracing = SearchEntry()
    contact_tracing.execute()
# main program/this file is the one to be executed
# import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from data_entry import DataEntry
from search_data import SearchEntry

class HomePage(): # create class

    def __init__(self):
        # create window
        self.home_page = tk.Tk()
        self.home_page.title("COVID-19 Contact Tracing APP")
        self.home_page.geometry("1100x950")
        self.home_page.config( bg = "#FFF7D4")

        # add data entry button
        entry_button = Button(self.home_page, text= "ENTER DATA", width=20, height=10, command = self.entry_window)
        entry_button.place(x=400, y=440)

        # add search data button
        search_button = Button(self.home_page, text= "SEARCH ENTRY", width=20, height=10, command = self.search_window)
        search_button.place(x=630, y=440)

        self.home_page.mainloop()

    def entry_window(self):
        self.home_page.destroy()
        DataEntry()

    def search_window(self):
        self.home_page.destroy()
        SearchEntry()

    def execute(self):
        self.home_page.mainloop()

if __name__ == "__main__":
    contact_tracing = HomePage()
    contact_tracing.execute()
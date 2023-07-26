# main program/this file is the one to be executed
# import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from data_entry import DataEntry
from search_data import SearchEntry
from PIL import ImageTk, Image        

class HomePage(): # create class

    def __init__(self):
        # create window
        self.home_page = tk.Tk()
        self.home_page.title("COVID-19 Contact Tracing APP")
        self.home_page.geometry("1000x930")
        self.home_page.config(bg = "#FFF7D4")
        self.home_page.resizable(False, False)

        Label(self.home_page, text = "COVID-19 CONTACT TRACING", width=20, height=3, bg='#4C3D3D', fg='#FFD95A', font='times 25 bold').pack(side = TOP, fill = 'x')
        Label(self.home_page, text = "PUP contact tracing", width=15, height=1, bg='#4C3D3D', fg='#FFD95A', font='arial 10 italic', anchor='w').pack(side = BOTTOM, fill = 'x')
        Label(self.home_page, text = "ajhsfjgweyfgyegfgeyfgdjf", width=30, height=2, bg='#4C3D3D', fg='#FFD95A', font='times 20 bold', anchor='center').pack(side = RIGHT, fill = 'y')

        original_image = Image.open('cvd.jpg')
        resized_image = original_image.resize((480, 787))  
        background_image = ImageTk.PhotoImage(resized_image)

        label1 = tk.Label(image=background_image)
        label1.image = background_image

        label1.place(x=514, y=117)

        # add data entry button
        entry_button = ctk.CTkButton(self.home_page, text= "ENTER DATA", width=150, height=60, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command = self.entry_window)
        entry_button.place(x=180, y=460)

        # add search data button
        search_button = ctk.CTkButton(self.home_page, text= "SEARCH ENTRY", width=150, height=60, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command = self.search_window)
        search_button.place(x=180, y=540)

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
# import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
import csv

class SearchEntry(): # create class search entry

    def __init__(self):
        # create GUI window
        self.root_window = tk.Tk()
        self.root_window.title("COVID-19 Contact Tracing APP")
        self.root_window.geometry("1000x930")
        self.root_window.config( bg = "#FFF7D4" )
        self.root_window.resizable(False, False)  

        Label(self.root_window, text = "SEARCH ENTRY", width=15, height=2, bg='#4C3D3D', fg='#FFD95A', font='times 20 bold').pack(side = TOP, fill = 'x')
        Label(self.root_window, text = "PUP contact tracing", width=15, height=1, bg='#4C3D3D', fg='#FFD95A', font='arial 10 italic', anchor='w').pack(side = BOTTOM, fill = 'x')

        frame = ctk.CTkFrame(self.root_window, fg_color="#FFD95A", width=850, height=850)
        frame.pack()

        self.surname_label = ctk.CTkLabel(self.root_window, text="Last Name: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.surname_label.place(x=158, y=136)
        self.surname_entry = tk.Entry(self.root_window, width=20)
        self.surname_entry.place(x=230, y=140)

        self.name_label = ctk.CTkLabel(self.root_window, text="First Name: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.name_label.place(x=390, y=136)
        self.name_entry = tk.Entry(self.root_window, width=25)
        self.name_entry.place(x=465, y=140)

        self.middle_label = ctk.CTkLabel(self.root_window, text="Middle Name: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.middle_label.place(x=640, y=136)
        self.middle_entry = tk.Entry(self.root_window, width=15)
        self.middle_entry.place(x=725, y=140)



        # add search button
        search_button = ctk.CTkButton(self.root_window, text= "SEARCH ENTRY", width=100, height=40, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', bg_color='#FFD95A', command = self.locate_entry)
        search_button.place(x=500, y=180)

        def clear(): # define clear function
            self.surname_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.middle_entry.delete(0, END)
        # add clear button
        clear_button = ctk.CTkButton(self.root_window, text= "CLEAR", width=100, height=40, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', bg_color='#FFD95A', command = clear)
        clear_button.place(x=380, y=180)


    def locate_entry():
        pass

    def execute(self):
        self.root_window.mainloop()

if __name__ == "__main__":
    contact_tracing = SearchEntry()
    contact_tracing.execute()
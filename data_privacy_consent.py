import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk

def consent():
    consent_window = tk.Toplevel() # toplevel window for data privacy consent
    consent_window.title("COVID-19 Contact Tracing APP")
    consent_window.geometry("1000x930+400+50")
    consent_window.config( bg = "#FFF7D4" )
    consent_window.resizable(False, False)       

    # create elements 
    Label(consent_window, text = "DATA PRIVACY CONSENT", width=15, height=2, bg='#4C3D3D', fg='#FFD95A', font='times 20 bold').pack(side = TOP, fill = 'x')
    Label(consent_window, text = "PUP contact tracing", width=15, height=1, bg='#4C3D3D', fg='#FFD95A', font='arial 10 italic', anchor='w').pack(side = BOTTOM, fill = 'x')

    consent_window.mainloop()
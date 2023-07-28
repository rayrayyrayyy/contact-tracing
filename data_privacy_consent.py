import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image  

def consent():
    consent_window = tk.Toplevel() # toplevel window for data privacy consent
    consent_window.title("COVID-19 Contact Tracing APP")
    consent_window.geometry("1000x930+400+50")
    consent_window.config( bg = "#FFF7D4" )
    consent_window.resizable(False, False)       

    # create elements 
    Label(consent_window, text = "DATA PRIVACY CONSENT", width=15, height=2, bg='#4C3D3D', fg='#FFD95A', font='times 20 bold').pack(side = TOP, fill = 'x')
    Label(consent_window, text = "PUP contact tracing", width=15, height=1, bg='#4C3D3D', fg='#FFD95A', font='arial 10 italic', anchor='w').pack(side = BOTTOM, fill = 'x')

    text_1 = tk.Label(consent_window, text = "We value your privacy and are committed to protecting your personal information. \nBefore you continue using our services, we kindly ask for your consent to collect, process, \nand store your data in accordance with our privacy policy.", bg='#FFF7D4', fg='#4C3D3D', font='times 16 bold')
    text_1.place(x=120, y=90)

    text_2 = tk.Label(consent_window, text = "I understand and concur that by clicking the “I Agree to the Data Privacy Consent”, \nI confirm that I freely and voluntarily give consent to the collection and processing \nof my data, which may include personal information and/or sensitive information set \nout in this registration and application possessed by City for the following purposes:", bg='#FFF7D4', fg='#4C3D3D', font='times 18 italic')
    text_2.place(x=80, y=230)

    text_3 = tk.Label(consent_window, text = "\n(a) Health update processing and tracking;\n\n(b) Emergency response purposes; and\n\n(c) Any other tracing activities necessary for the containment of COVID-19.", bg='#FFF7D4', fg='#4C3D3D', font='times 18 italic')
    text_3.place(x=120, y=390)

    text_4 = tk.Label(consent_window, text = "\n I am aware of my right to be informed, to access, to object, to erasure or blocking, \nto damages, to file a complaint, to rectify and to data portability, and I understand \nthat there are procedures, conditions and exceptions to be complied with in order \nto exercise or invoke such rights.", bg='#FFF7D4', fg='#4C3D3D', font='times 18 italic')
    text_4.place(x=100, y=610)


    def back_bttn(): # define back function
        consent_window.destroy()

    # add back button
    back_butt = ctk.CTkButton(consent_window, text= "BACK", width=90, height=50, corner_radius=10, hover_color='#CD3333', fg_color='#4C3D3D', command = back_bttn)
    back_butt.place(x=430, y=800)

    consent_window.mainloop()
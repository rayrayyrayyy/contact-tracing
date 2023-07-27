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
        self.root_window.geometry("1000x930+400+50")
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

        # respondent's details
        self.contact_label = tk.Label(self.root_window, text="Respondent's Details ", fg='#4C3D3D', bg = "#FFF7D4", font='times 10 bold')
        self.contact_label.place(x=130, y=240)

        self.last_name = tk.Label(self.root_window, text="LAST NAME", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold')
        self.last_name.place(x=240, y=290, anchor=CENTER)
        self.last_name_display = ctk.CTkLabel(self.root_window, text="sdgfg: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.last_name_display.place(x=240, y=320, anchor=CENTER)

        self.first_name = tk.Label(self.root_window, text="FIRST NAME", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold')
        self.first_name.place(x=485, y=290, anchor=CENTER)
        self.first_name_display = ctk.CTkLabel(self.root_window, text="djshd: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.first_name_display.place(x=485, y=320, anchor=CENTER)

        self.middle_name = tk.Label(self.root_window, text="MIDDLE NAME", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold')
        self.middle_name.place(x=730, y=290, anchor=CENTER)
        self.middle_name_display = ctk.CTkLabel(self.root_window, text="skjd ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.middle_name_display.place(x=730, y=320, anchor=CENTER)

        self.age_label = tk.Label(self.root_window, text="AGE", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold')
        self.age_label.place(x=240, y=380, anchor=CENTER)
        self.age_display = ctk.CTkLabel(self.root_window, text="sdgfg: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.age_display.place(x=240, y=410, anchor=CENTER)

        self.email_label = tk.Label(self.root_window, text="EMAIL", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold')
        self.email_label.place(x=485, y=380, anchor=CENTER)
        self.email_display = ctk.CTkLabel(self.root_window, text="djshd: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.email_display.place(x=485, y=410, anchor=CENTER)

        self.number_label = tk.Label(self.root_window, text="CONTACT NUMBER", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold')
        self.number_label.place(x=730, y=380, anchor=CENTER)
        self.number_display = ctk.CTkLabel(self.root_window, text="skjd ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.number_display.place(x=730, y=410, anchor=CENTER)


        # health declaration
        self.health_label = tk.Label(self.root_window, text="Health Declaration", fg='#4C3D3D', bg = "#FFF7D4", font='times 10 bold')
        self.health_label.place(x=130, y=440)

        self.vaccinated_label = tk.Label(self.root_window, text="Vaccinated for Covid-19? ", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold italic')
        self.vaccinated_label.place(x=165, y=470)
        self.display_if_vaccinated = ctk.CTkLabel(self.root_window, text="Not yet", text_color='#4C3D3D', bg_color='#FFD95A')
        self.display_if_vaccinated.place(x=490, y=490, anchor=CENTER)

        self.symptoms_label = tk.Label(self.root_window, text="Symptoms experienced: ", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold italic')
        self.symptoms_label.place(x=165, y=520)
        self.show_symptoms = ctk.CTkLabel(self.root_window, text="None", text_color='#4C3D3D', bg_color='#FFD95A')
        self.show_symptoms.place(x=490, y=540, anchor=CENTER)

        self.tested_label = tk.Label(self.root_window, text="Been tested for Covid-19 in the last 14 days? ", fg='#4C3D3D', bg ='#FFD95A', font='verdana 15 bold italic')
        self.tested_label.place(x=165, y=570)
        self.show_if_tested = ctk.CTkLabel(self.root_window, text="Yes(negative)", text_color='#4C3D3D', bg_color='#FFD95A')
        self.show_if_tested.place(x=730, y=590, anchor=CENTER)
        

        # contact person details
        self.contact_label = tk.Label(self.root_window, text="Contact Person Details ", fg='#4C3D3D', bg = "#FFF7D4", font='times 10 bold')
        self.contact_label.place(x=130, y=630)

        self.contact_person_label = tk.Label(self.root_window, text="CONTACT PERSON", fg='#4C3D3D', bg ='#FFD95A', font='verdana 14 bold')
        self.contact_person_label.place(x=160, y=670)
        self.contact_person_display = ctk.CTkLabel(self.root_window, text="sdgfg: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.contact_person_display.place(x=160, y=700)

        self.relationship_label = tk.Label(self.root_window, text="RELATIONSHIP", fg='#4C3D3D', bg ='#FFD95A', font='verdana 14 bold')
        self.relationship_label.place(x=550, y=670)
        self.relationship_display = ctk.CTkLabel(self.root_window, text="djshd: ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.relationship_display.place(x=550, y=700)

        self.conatact_number_label = tk.Label(self.root_window, text="CONTACT NUMBER", fg='#4C3D3D', bg ='#FFD95A', font='verdana 14 bold')
        self.conatact_number_label.place(x=160, y=750)
        self.contact_number_display = ctk.CTkLabel(self.root_window, text="skjd ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.contact_number_display.place(x=160, y=780)

        self.conatact_email_label = tk.Label(self.root_window, text="CONTACT NUMBER", fg='#4C3D3D', bg ='#FFD95A', font='verdana 14 bold')
        self.conatact_email_label.place(x=550, y=750)
        self.contact_email_display = ctk.CTkLabel(self.root_window, text="skjd ", text_color='#4C3D3D', bg_color='#FFD95A')
        self.contact_email_display.place(x=550, y=780)



        # add search button
        search_button = ctk.CTkButton(self.root_window, text= "SEARCH ENTRY", width=100, height=40, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', bg_color='#FFD95A', command = self.locate_entry)
        search_button.place(x=500, y=180)

        def clear(): # define clear function
            self.surname_entry.delete(0, END)
            self.name_entry.delete(0, END)
            self.middle_entry.delete(0, END)
            self.last_name_display.configure(text = "")
            self.first_name_display.configure(text = "")
            self.middle_name_display.configure(text = "")
            self.age_display.configure(text = "")
            self.email_display.configure(text = "")
            self.number_display.configure(text = "")
            self.display_if_vaccinated.configure(text = "")
            self.show_symptoms.configure(text = "")
            self.show_if_tested.configure(text = "")
            self.contact_person_display.configure(text = "")
            self.relationship_display.configure(text = "")
            self.contact_number_display.configure(text = "")
            self.contact_email_display.configure(text = "")

        # add clear button
        clear_button = ctk.CTkButton(self.root_window, text= "CLEAR", width=100, height=40, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', bg_color='#FFD95A', command = clear)
        clear_button.place(x=380, y=180)


        def back(): # define back function
            from main_home_page import HomePage
            self.root_window.destroy()
            HomePage()

        # add back button
        back_button = ctk.CTkButton(self.root_window, text= "BACK", width=90, height=40, corner_radius=10, hover_color='#CD3333', fg_color='#4C3D3D', bg_color='#FFD95A', command = back)
        back_button.place(x=700, y=837)

        # add exit button


    def locate_entry():
        pass

    def execute(self):
        self.root_window.mainloop()

if __name__ == "__main__":
    contact_tracing = SearchEntry()
    contact_tracing.execute()
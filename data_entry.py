# Ray Allessandra D. Pacis | BSCPE 1-5
# create a contact tracing app that can add and search entry

# import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
import csv

class DataEntry(): # put in class

    def __init__(self):
        # create GUI window
        self.root_window = tk.Tk()
        self.root_window.title("COVID-19 Contact Tracing APP")
        self.root_window.geometry("1000x930+400+50")
        self.root_window.config( bg = "#FFF7D4" )
        self.root_window.resizable(False, False)        

        # create GUI elements for personal details
        Label(self.root_window, text = "DATA ENTRY", width=15, height=2, bg='#4C3D3D', fg='#FFD95A', font='times 20 bold').pack(side = TOP, fill = 'x')
        Label(self.root_window, text = "PUP contact tracing", width=15, height=1, bg='#4C3D3D', fg='#FFD95A', font='arial 10 italic', anchor='w').pack(side = BOTTOM, fill = 'x')
        frame = ctk.CTkFrame(self.root_window, fg_color="#FFD95A")
        frame.pack()

        self.personal_details_frame =tk.LabelFrame(frame)
        self.personal_details_frame.grid(row= 0, column=0, padx=50, pady=20)

        self.last_name_label = ctk.CTkLabel(self.personal_details_frame, text="Last Name: ", text_color='#4C3D3D')
        self.last_name_label.grid(row=0, column=0)
        self.last_name_entry = tk.Entry(self.personal_details_frame)
        self.last_name_entry.grid(row=0, column=1)

        self.first_name_label = ctk.CTkLabel(self.personal_details_frame, text="First Name: ", text_color='#4C3D3D')
        self.first_name_label.grid(row=0, column=2)
        self.first_name_entry = tk.Entry(self.personal_details_frame)
        self.first_name_entry.grid(row=0, column=3)

        self.middle_name_label = ctk.CTkLabel(self.personal_details_frame, text="Middle Name: ", text_color='#4C3D3D')
        self.middle_name_label.grid(row=0, column=5)
        self.middle_name_entry = tk.Entry(self.personal_details_frame)
        self.middle_name_entry.grid(row=0, column=6)

        self.age_label = ctk.CTkLabel(self.personal_details_frame, text="Age: ", text_color='#4C3D3D')
        self.age_entry = tk.Entry(self.personal_details_frame)
        self.age_label.grid(row=1, column=0)
        self.age_entry.grid(row=1, column=1)

        self.email_label = ctk.CTkLabel(self.personal_details_frame, text="Email: ", text_color='#4C3D3D')
        self.email_label.grid(row=1, column=2)
        self.email_entry = tk.Entry(self.personal_details_frame)
        self.email_entry.grid(row=1, column=3)

        self.number_label = ctk.CTkLabel(self.personal_details_frame, text="Contact Number: ", text_color='#4C3D3D')
        self.number_label.grid(row=1, column=5)
        self.number_entry = tk.Entry(self.personal_details_frame)
        self.number_entry.grid(row=1, column=6)

        self.address_label = ctk.CTkLabel(self.personal_details_frame, text="Address: ", text_color='#4C3D3D')
        self.address_label.grid(row=2, column=0)
        self.address_entry = tk.Entry(self.root_window, width=105)
        self.address_entry.place(x=230, y=160)

        for widget in self.personal_details_frame.winfo_children():
            widget.grid_configure(padx=12, pady=2)

        # create GUI elements to ask user if vaccinated or not
        self.vaccinated_frame =tk.LabelFrame(frame)
        self.vaccinated_frame.grid(row= 1, column=0, sticky='news', padx=50, pady=20)

        self.vaccinated_label = ctk.CTkLabel(self.vaccinated_frame, text=" Are you vaccinated for COVID-19?")
        self.vaccinated_label.grid(row=0, column=0)

        self.radiobutton_var = ctk.StringVar(value=0)

        self.radio_button_1 = ctk.CTkRadioButton(self.vaccinated_frame, variable=self.radiobutton_var, text='Not yet', value='Not vaccinated', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_1.grid(row=3, column=0)

        self.radio_button_2 = ctk.CTkRadioButton(self.vaccinated_frame, variable=self.radiobutton_var, text='1st Dose', value='1st Dose', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_2.grid(row=4, column=0)

        self.radio_button_3 = ctk.CTkRadioButton(self.vaccinated_frame, variable=self.radiobutton_var, text='2nd Dose', value='2nd Dose', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_3.grid(row=5, column=0)

        self.radio_button_4 = ctk.CTkRadioButton(self.vaccinated_frame, variable=self.radiobutton_var, text='1st Booster Shot', value='1st booster shot', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_4.grid(row=3, column=2)

        self.radio_button_5 = ctk.CTkRadioButton(self.vaccinated_frame, variable=self.radiobutton_var, text='2nd Booster Shot', value='Complete booster shot', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_5.grid(row=4, column=2)

        # create GUI elements for symptoms
        self.symptoms_frame =tk.LabelFrame(frame)
        self.symptoms_frame.grid(row= 2, column=0, sticky='news', padx=50, pady=20)

        self.symptoms_label = ctk.CTkLabel(self.symptoms_frame, text=" *Please select all symptoms that you have experienced for the past 7 days.")
        self.symptoms_label.grid(row=0, column=0)

        self.sore_throat_symptom = BooleanVar()
        self.checkbox_1 = ctk.CTkCheckBox(self.symptoms_frame, text='Sore throat', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.sore_throat_symptom, onvalue = True, offvalue = False)
        self.checkbox_1.grid(row=3)

        self.cough_symptom = BooleanVar()
        self.checkbox_2 = ctk.CTkCheckBox(self.symptoms_frame, text='Cough', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.cough_symptom, onvalue = True, offvalue = False)
        self.checkbox_2.grid(row=4)

        self.fever_symptom = BooleanVar()
        self.checkbox_3 = ctk.CTkCheckBox(self.symptoms_frame, text='Fever', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.fever_symptom, onvalue = True, offvalue = False)
        self.checkbox_3.grid(row=5)


        self.loss_taste_symptom = BooleanVar()
        self.checkbox_4 = ctk.CTkCheckBox(self.symptoms_frame, text='Loss of taste', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.loss_taste_symptom, onvalue = True, offvalue = False)
        self.checkbox_4.grid(row=4, column=3)

        self.loss_smell_symptom = BooleanVar()
        self.checkbox_5 = ctk.CTkCheckBox(self.symptoms_frame, text='Loss of smell', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.loss_smell_symptom, onvalue = True, offvalue = False)
        self.checkbox_5.grid(row=5, column=3)

        self.breathlessness_symptom = BooleanVar()
        self.checkbox_6 = ctk.CTkCheckBox(self.symptoms_frame, text='Shortness of breath', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.breathlessness_symptom, onvalue = True, offvalue = False)
        self.checkbox_6.grid(row=3, column=3)

        self.runny_nose_symptom = BooleanVar()
        self.checkbox_7 = ctk.CTkCheckBox(self.symptoms_frame, text='Runny nose', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.runny_nose_symptom, onvalue = True, offvalue = False)
        self.checkbox_7.grid(row=6)

        self.fatigue_symptom = BooleanVar()
        self.checkbox_8 = ctk.CTkCheckBox(self.symptoms_frame, text='Fatigue', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.fatigue_symptom, onvalue = True, offvalue = False)
        self.checkbox_8.grid(row=7)

        self.no_symptom = BooleanVar()
        self.checkbox_9 = ctk.CTkCheckBox(self.symptoms_frame, text='None of the above', hover_color='#FFD95A', fg_color='#4C3D3D', variable=self.no_symptom, onvalue = True, offvalue = False)
        self.checkbox_9.grid(row=6, column=3)

        # create GUI elements to ask user if he/she had been tested for Covid-19 in the last two weeks
        self.tested_frame =tk.LabelFrame(frame)
        self.tested_frame.grid(row= 3, column=0, sticky='news', padx=50, pady=20)

        self.tested_label = ctk.CTkLabel(self.tested_frame, text=" Have you been tested for COVID-19 in the last 14 days?")
        self.tested_label.grid(row=0, column=0)

        self.radiobutton_tested_var = ctk.StringVar(value=0)

        self.radio_button_6 = ctk.CTkRadioButton(self.tested_frame, variable=self.radiobutton_tested_var, text='NO', value='No', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_6.grid(row=3, column=0)

        self.radio_button_7 = ctk.CTkRadioButton(self.tested_frame, variable=self.radiobutton_tested_var, text='YES - positive', value='Yes(positive)', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_7.grid(row=4, column=0)

        self.radio_button_8 = ctk.CTkRadioButton(self.tested_frame, variable=self.radiobutton_tested_var, text='YES - negative', value='Yes(negative)', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_8.grid(row=5, column=0)

        self.radio_button_9 = ctk.CTkRadioButton(self.tested_frame, variable=self.radiobutton_tested_var, text='YES - pending', value='Yes(pending)', hover_color='#FFD95A', fg_color='#4C3D3D')
        self.radio_button_9.grid(row=6, column=0)

        # create GUI elements for contact person's details
        self.contact_person_details_frame =tk.LabelFrame(frame, text="Contact Person Details", font='arial 10 italic')
        self.contact_person_details_frame.grid(row= 5, column=0, padx=50, pady=20)

        self.name_label = ctk.CTkLabel(self.contact_person_details_frame, text="Contact Person: ", text_color='#4C3D3D')
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.contact_person_details_frame)
        self.name_entry.grid(row=0, column=1)

        self.email_label = ctk.CTkLabel(self.contact_person_details_frame, text="Email: ", text_color='#4C3D3D')
        self.email_label.grid(row=1, column=2)
        self.email_contact_entry = tk.Entry(self.contact_person_details_frame)
        self.email_contact_entry.grid(row=1, column=3)

        self.number_label = ctk.CTkLabel(self.contact_person_details_frame, text="Contact Number: ", text_color='#4C3D3D')
        self.number_label.grid(row=0, column=2)
        self.contact_number_entry = tk.Entry(self.contact_person_details_frame)
        self.contact_number_entry.grid(row=0, column=3)

        self.relationship_label = ctk.CTkLabel(self.contact_person_details_frame, text="Relationship to the contact person: ", text_color='#4C3D3D')
        self.relationship_label.grid(row=1, column=0)
        self.relationship_entry = tk.Entry(self.contact_person_details_frame)
        self.relationship_entry.grid(row=1, column=1)

        for widget in self.contact_person_details_frame.winfo_children():
            widget.grid_configure(padx=20, pady=2)

        # add buttons

        def clear(): # define clear function
            self.last_name_entry.delete(0, END)
            self.first_name_entry.delete(0, END)
            self.middle_name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.address_entry.delete(0, END)
            self.number_entry.delete(0, END)
            self.checkbox_1.deselect()
            self.checkbox_2.deselect()
            self.checkbox_3.deselect()
            self.checkbox_4.deselect()
            self.checkbox_5.deselect()
            self.checkbox_6.deselect()
            self.checkbox_7.deselect()
            self.checkbox_8.deselect()
            self.checkbox_9.deselect()
            self.name_entry.delete(0, END)
            self.email_contact_entry.delete(0, END)
            self.contact_number_entry.delete(0, END)
            self.relationship_entry.delete(0, END)
            self.radiobutton_var.set(0)
            self.radiobutton_tested_var.set(0)

        # add clear button
        clear_button = ctk.CTkButton(self.root_window, text= "CLEAR", width=90, height=50, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command = clear)
        clear_button.place(x=150, y=840)


        def exit(): # define function to exit program
            msg_box = messagebox.askyesno("NOTICE", "You're about to exit the program?")
            if msg_box == YES:
                self.root_window.quit()
            else:
                return
        # add exit button
        exit_button = ctk.CTkButton(self.root_window, text= "EXIT", width=90, height=50, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command = exit)
        exit_button.place(x=260, y=840)


        def submit_data(): # define function to save data
            user_name = self.last_name_entry.get(), self.first_name_entry.get(), self.middle_name_entry.get()
            age = self.age_entry.get()
            email = self.email_entry.get()
            number = self.number_entry.get()
            address = self.address_entry.get()
            vaccinated = self.radiobutton_var.get()
            tested = self.radiobutton_tested_var.get()
            contact_person = self.name_entry.get()
            contact_number = self.contact_number_entry.get()
            relationship = self.relationship_entry.get()
            contact_email = self.email_contact_entry.get()

            symptoms = {"Sore throath": self.sore_throat_symptom.get(),
            "Cough": self.cough_symptom.get(),
            "Fever": self.fever_symptom.get(),
            "Loss of taste": self.loss_taste_symptom.get(),
            "Loss of smell": self.loss_smell_symptom.get(),
            "Shortness of breath": self.breathlessness_symptom.get(),
            "Fatigue": self.fatigue_symptom.get(),
            "None of the above": self.no_symptom.get()}

            try:
                if not (user_name and age and email and number and address and vaccinated and tested and contact_person and contact_number and relationship and contact_email):
                    messagebox.showerror('NOTICE', 'Please enter all fields.')
                if symptoms == '':
                    messagebox.showerror('ERROR', 'Check atleast one of the following symptoms or None of the above.')
                    return
                else:
                    user_age = int(age)
                    cp_number = int(number)
                    contact_num = int(contact_number)
                    with open('data_entries.cvs', 'a', newline='') as file:
                        data_input = csv.writer(file)
                        data_input.writerow([user_name, age, email, number, address, vaccinated, tested, contact_person, contact_number, relationship, contact_email])
                    messagebox.showinfo('SUCCESS', 'Data saved.')
            except ValueError:
                messagebox.showerror('ERROR', 'age and contact numbers should be an integer')              
            except:
                messagebox.showerror('ERROR', 'Error Occured.')
        # add submit button
        submit_button = ctk.CTkButton(self.root_window, text = "ENTER", width=90, height=50, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command=submit_data)
        submit_button.place(x=795, y=840)

    def execute(self):
        self.root_window.mainloop()

if __name__ == "__main__":
    contact_tracing = DataEntry()
    contact_tracing.execute()
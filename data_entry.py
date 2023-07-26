# Ray Allessandra D. Pacis | BSCPE 1-5
# create a contact tracing app that can add and search entry

# import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk

# create GUI window
root_window = ctk.CTk()
root_window.title("COVID-19 Contact Tracing APP")
root_window.geometry("1100x950")
root_window.config( bg = "#FFF7D4" )

# create GUI elements for personal details
Label(root_window, text = "CONTACT TRACING DATA ENTRY", width=15, height=2, bg='#4C3D3D', fg='#FFD95A', font='times 20 bold').pack(side = TOP, fill = 'x')
Label(root_window, text = "PUP contact tracing", width=15, height=1, bg='#4C3D3D', fg='#FFD95A', font='arial 10 italic', anchor='w').pack(side = BOTTOM, fill = 'x')
frame = ctk.CTkFrame(root_window, fg_color="#FFD95A")
frame.pack()

personal_details_frame =tk.LabelFrame(frame)
personal_details_frame.grid(row= 0, column=0, padx=50, pady=20)

last_name_label = ctk.CTkLabel(personal_details_frame, text="Last Name: ", text_color='#4C3D3D')
last_name_label.grid(row=0, column=0)
last_name_entry = tk.Entry(personal_details_frame)
last_name_entry.grid(row=0, column=1)

first_name_label = ctk.CTkLabel(personal_details_frame, text="First Name: ", text_color='#4C3D3D')
first_name_label.grid(row=0, column=2)
first_name_entry = tk.Entry(personal_details_frame)
first_name_entry.grid(row=0, column=3)

middle_name_label = ctk.CTkLabel(personal_details_frame, text="Middle Name: ", text_color='#4C3D3D')
middle_name_label.grid(row=0, column=5)
middle_name_entry = tk.Entry(personal_details_frame)
middle_name_entry.grid(row=0, column=6)

age_label = ctk.CTkLabel(personal_details_frame, text="Age: ", text_color='#4C3D3D')
age_spinbox = ttk.Spinbox(personal_details_frame, from_=18, to=110)
age_label.grid(row=1, column=0)
age_spinbox.grid(row=1, column=1)

email_label = ctk.CTkLabel(personal_details_frame, text="Email: ", text_color='#4C3D3D')
email_label.grid(row=1, column=2)
email_entry = tk.Entry(personal_details_frame)
email_entry.grid(row=1, column=3)

number_label = ctk.CTkLabel(personal_details_frame, text="Contact Number: ", text_color='#4C3D3D')
number_label.grid(row=1, column=5)
number_entry = tk.Entry(personal_details_frame)
number_entry.grid(row=1, column=6)

address_label = ctk.CTkLabel(personal_details_frame, text="Address: ", text_color='#4C3D3D')
address_label.grid(row=2, column=0)
address_entry = tk.Entry(personal_details_frame)
address_entry.grid(row=2, column=3)

for widget in personal_details_frame.winfo_children():
    widget.grid_configure(padx=12, pady=2)

# create GUI elements to ask user if vaccinated or not
vaccinated_frame =tk.LabelFrame(frame)
vaccinated_frame.grid(row= 1, column=0, sticky='news', padx=50, pady=20)

vaccinated_label = ctk.CTkLabel(vaccinated_frame, text=" Are you vaccinated for COVID-19?")
vaccinated_label.grid(row=0, column=0)

radiobutton_var = ctk.IntVar()

radio_button_1 = ctk.CTkRadioButton(vaccinated_frame, variable=radiobutton_var, text='Not yet', value=1, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_1.grid(row=3, column=0)

radio_button_2 = ctk.CTkRadioButton(vaccinated_frame, variable=radiobutton_var, text='1st Dose', value=2, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_2.grid(row=4, column=0)

radio_button_3 = ctk.CTkRadioButton(vaccinated_frame, variable=radiobutton_var, text='2nd Dose', value=3, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_3.grid(row=5, column=0)

radio_button_4 = ctk.CTkRadioButton(vaccinated_frame, variable=radiobutton_var, text='1st Booster Shot', value=4, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_4.grid(row=3, column=2)

radio_button_5 = ctk.CTkRadioButton(vaccinated_frame, variable=radiobutton_var, text='2nd Booster Shot', value=5, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_5.grid(row=4, column=2)

# create GUI elements for symptoms
symptoms_frame =tk.LabelFrame(frame)
symptoms_frame.grid(row= 2, column=0, sticky='news', padx=50, pady=20)

symptoms_label = ctk.CTkLabel(symptoms_frame, text=" *Please select all symptoms that you have experienced for the past 7 days.")
symptoms_label.grid(row=0, column=0)

checkbox_1 = ctk.CTkCheckBox(symptoms_frame, text='Sore throat', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_1.grid(row=3)

checkbox_2 = ctk.CTkCheckBox(symptoms_frame, text='Cough', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_2.grid(row=4)

checkbox_3 = ctk.CTkCheckBox(symptoms_frame, text='Fever', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_3.grid(row=5)

checkbox_4 = ctk.CTkCheckBox(symptoms_frame, text='Loss of taste', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_4.grid(row=4, column=3)

checkbox_5 = ctk.CTkCheckBox(symptoms_frame, text='Loss of smell', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_5.grid(row=5, column=3)

checkbox_6 = ctk.CTkCheckBox(symptoms_frame, text='Shortness of breath', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_6.grid(row=3, column=3)

checkbox_7 = ctk.CTkCheckBox(symptoms_frame, text='Runny nose', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_7.grid(row=6)

checkbox_8 = ctk.CTkCheckBox(symptoms_frame, text='Fatigue', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_8.grid(row=7)

checkbox_9 = ctk.CTkCheckBox(symptoms_frame, text='None of the above', hover_color='#FFD95A', fg_color='#4C3D3D')
checkbox_9.grid(row=6, column=3)

# create GUI elements to ask user if he/she had been tested for Covid-19 in the last two weeks
tested_frame =tk.LabelFrame(frame)
tested_frame.grid(row= 3, column=0, sticky='news', padx=50, pady=20)

tested_label = ctk.CTkLabel(tested_frame, text=" Have you been tested for COVID-19 in the last 14 days?")
tested_label.grid(row=0, column=0)

radiobutton_var = ctk.IntVar(value=1)

radio_button_1 = ctk.CTkRadioButton(tested_frame, variable=radiobutton_var, text='NO', value=1, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_1.grid(row=3, column=0)

radio_button_2 = ctk.CTkRadioButton(tested_frame, variable=radiobutton_var, text='YES - positive', value=2, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_2.grid(row=4, column=0)

radio_button_3 = ctk.CTkRadioButton(tested_frame, variable=radiobutton_var, text='YES - negative', value=3, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_3.grid(row=5, column=0)

radio_button_4 = ctk.CTkRadioButton(tested_frame, variable=radiobutton_var, text='YES - pending', value=4, hover_color='#FFD95A', fg_color='#4C3D3D')
radio_button_4.grid(row=6, column=0)

# create GUI elements for contact person's details
contact_person_details_frame =tk.LabelFrame(frame, text="Contact Person Details", font='arial 10 italic')
contact_person_details_frame.grid(row= 5, column=0, padx=50, pady=20)

name_label = ctk.CTkLabel(contact_person_details_frame, text="Contact Person: ", text_color='#4C3D3D')
name_label.grid(row=0, column=0)
name_entry = tk.Entry(contact_person_details_frame)
name_entry.grid(row=0, column=1)

email_label = ctk.CTkLabel(contact_person_details_frame, text="Email: ", text_color='#4C3D3D')
email_label.grid(row=1, column=2)
email_contact_entry = tk.Entry(contact_person_details_frame)
email_contact_entry.grid(row=1, column=3)

number_label = ctk.CTkLabel(contact_person_details_frame, text="Contact Number: ", text_color='#4C3D3D')
number_label.grid(row=0, column=2)
contact_number_entry = tk.Entry(contact_person_details_frame)
contact_number_entry.grid(row=0, column=3)

relationship_label = ctk.CTkLabel(contact_person_details_frame, text="Relationship to the contact person: ", text_color='#4C3D3D')
relationship_label.grid(row=1, column=0)
relationship_entry = tk.Entry(contact_person_details_frame)
relationship_entry.grid(row=1, column=1)

for widget in contact_person_details_frame.winfo_children():
    widget.grid_configure(padx=20, pady=2)

# add buttons

def clear(): # define clear function
    last_name_entry.delete(0, END)
    first_name_entry.delete(0, END)
    middle_name_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    number_entry.delete(0, END)
    checkbox_1.deselect()
    checkbox_2.deselect()
    checkbox_3.deselect()
    checkbox_4.deselect()
    checkbox_5.deselect()
    checkbox_6.deselect()
    checkbox_7.deselect()
    checkbox_8.deselect()
    checkbox_9.deselect()
# add clear button
clear_button = ctk.CTkButton(root_window, text= "CLEAR", width=90, height=50, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command = clear)
clear_button.place(x=150, y=840)


def exit(): # define function to exit program
    msg_box = messagebox.askyesno("NOTICE", "You're about to exit the program?")
    if msg_box == YES:
        root_window.quit()
    else:
        return
# add exit button
exit_button = ctk.CTkButton(root_window, text= "EXIT", width=90, height=50, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command = exit)
exit_button.place(x=260, y=840)


def submit(): # define function to save data
    pass
# add submit button
submit_button = ctk.CTkButton(root_window, text = "ENTER", width=90, height=50, corner_radius=10, hover_color='#8B6508', fg_color='#4C3D3D', command = submit)
submit_button.place(x=895, y=840)


## collect information

root_window.mainloop()
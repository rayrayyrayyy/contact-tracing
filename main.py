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
root_window.geometry("1150x900+100+100")
root_window.config( bg = "#FFF7D4" )

# create GUI elements for personal details
Label(root_window, text = "CONTACT TRACING DATA ENTRY", width=15, height=2, bg='#4C3D3D', fg='#FFD95A', font='times 20 bold').pack(side = TOP, fill = 'x')
frame = ctk.CTkFrame(root_window, fg_color="#FFD95A")
frame.pack()

personal_details_frame =tk.LabelFrame(frame, text="")
personal_details_frame.grid(row= 0, column=0, padx=100, pady=50)

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
    widget.grid_configure(padx=5, pady=15)



# create GUI elements to ask user if vaccinated or not
# create GUI elements for symptoms
# create GUI elements to ask user if he/she had been tested for Covid-19 in the last two weeks
# create GUI elements for contact person's details
# add buttons

## collect information

root_window.mainloop()
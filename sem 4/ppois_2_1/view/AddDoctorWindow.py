import re
import uuid

from model.Doctor import Doctor
import tkinter as tk
from tkinter import ttk, messagebox
from view.CenteredWindowHelper import center_window

class AddDoctorWindow(tk.Toplevel):
    def __init__(self, master, application):
        super().__init__(master=master)
        self.title("Add doctor")
        self.application = application
        center_window(self, 300, 200)
        self.geometry('300x200')
        ttk.Label(self, text="Name:").pack()
        self.doctor_name_entry = ttk.Entry(self)
        self.doctor_name_entry.pack()
        ttk.Label(self, text="Specialization:").pack()
        self.doctor_specialization_entry = ttk.Entry(self)
        self.doctor_specialization_entry.pack()
        ttk.Button(self, text="Add", command = self.add_doctor_data).pack()

    def add_doctor_data(self):
        name = self.doctor_name_entry.get().strip()  # Remove leading/trailing spaces
        specialization = self.doctor_specialization_entry.get().strip()  # Remove leading/trailing spaces

        # Check if fields are empty
        if not name or not specialization:
            messagebox.showerror("Error!", "Fields should't be empty!")
            return

        # Check if name contains only letters
        if not all(re.match("^[A-Za-z]+$", word) for word in name.split()):
            messagebox.showerror("Error!", "Incorrect name: expected symbols from [A-Z],[a-z].")
            self.doctor_name_entry.delete(0, 'end')
            self.doctor_name_entry.focus_set()
            return

        # Check if specialization contains only letters
        if not all(re.match("^[A-Za-z]+$", word) for word in specialization.split()):
            messagebox.showerror("Error!", "Incorrect specialization: expected symbols from [A-Z],[a-z].")
            self.doctor_specialization_entry.delete(0, 'end')
            self.doctor_specialization_entry.focus_set()
            return

        if self.application.repo.doctor_exists(name, specialization):
            messagebox.showerror("Eror", "Doctor with this name is already exist")
            self.doctor_name_entry.delete(0, 'end')
            self.doctor_specialization_entry.delete(0, 'end')
            self.doctor_name_entry.focus_set()
            return

        self.application.repo.add_doctor(name, specialization)
        self.application.update_doctor_data()
        messagebox.showinfo("Success!", "Doctor has been added.")
        self.destroy()



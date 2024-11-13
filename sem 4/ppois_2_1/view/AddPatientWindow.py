from __future__ import annotations
from datetime import datetime
import re
from view.CenteredWindowHelper import center_window
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AddPatientWindow(tk.Toplevel):
    def __init__(self,master, application):
        super().__init__(master=master)
        self.title("Add patient")
        self.application = application
        self.doctor_list: list = self.application.repo.get_doctors()
        center_window(self, 300, 400)
        ttk.Label(self, text="Name:").pack()
        self.patient_name_entry = ttk.Entry(self)
        self.patient_name_entry.pack()
        ttk.Label(self, text="Address:").pack()
        self.patient_address_entry = ttk.Entry(self)
        self.patient_address_entry.pack()
        ttk.Label(self, text="Birthdate:").pack()
        self.patient_birthdate_entry = DateEntry(self)
        self.patient_birthdate_entry.pack()
        ttk.Label(self, text="Appointment Date:").pack()
        self.patient_appdate_entry = DateEntry(self)
        self.patient_appdate_entry.pack()
        ttk.Label(self, text="Doctors Name:").pack()
        self.patient_doctor_name_var = tk.StringVar()
        patient_doctor_name_combobox = ttk.Combobox(self, textvariable=self.patient_doctor_name_var, values=[doctor.get_docname() for doctor in self.doctor_list], state="readonly")
        patient_doctor_name_combobox.pack()
        ttk.Label(self, text="Conclusion:").pack()
        self.patient_conclusion_entry = ttk.Entry(self)
        self.patient_conclusion_entry.pack()
        ttk.Button(self, text="Add", command=self.add_patient_data).pack()

    from datetime import datetime

    def add_patient_data(self):
        from datetime import datetime

        name = self.patient_name_entry.get().strip()  # Remove leading/trailing spaces
        address = self.patient_address_entry.get().strip()  # Remove leading/trailing spaces
        birth_date_str = self.patient_birthdate_entry.get()
        app_date_str = self.patient_appdate_entry.get()
        doctor_name = self.patient_doctor_name_var.get()
        conclusion = self.patient_conclusion_entry.get().strip()  # Remove leading/trailing spaces

        # Check if any field is empty
        if not all((name, address, birth_date_str, app_date_str, doctor_name, conclusion)):
            messagebox.showerror("Error!", "All fields shouldn't be empty.")
            return

        # Convert date strings to datetime objects
        try:
            # Parse birth date
            birth_date = datetime.strptime(birth_date_str, "%m/%d/%y")
            birth_date_str = birth_date.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
        except ValueError:
            try:
                # Try parsing with single digit month and day
                birth_date = datetime.strptime(birth_date_str, "%-m/%-d/%y")
                birth_date_str = birth_date.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
            except ValueError:
                messagebox.showerror("Error!", "Incorrect date. Expected: MM/DD/YYYY")
                self.patient_birthdate_entry.delete(0, 'end')
                self.patient_birthdate_entry.focus_set()
                return

        try:
            # Parse appointment date
            app_date = datetime.strptime(app_date_str, "%m/%d/%y")
            app_date_str = app_date.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
        except ValueError:
            try:
                # Try parsing with single digit month and day
                app_date = datetime.strptime(app_date_str, "%-m/%-d/%y")
                app_date_str = app_date.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
            except ValueError:
                messagebox.showerror("Error!", "Incorrect date. Expected: MM/DD/YYYY")
                self.patient_appdate_entry.delete(0, 'end')
                self.patient_appdate_entry.focus_set()
                return

        if not all(re.match("^[A-Za-z]+$", word) for word in name.split()):
            messagebox.showerror("Error!", "Incorrect name: expected symbols from [A-Z],[a-z].")
            self.patient_name_entry.delete(0, 'end')
            self.patient_name_entry.focus_set()
            return

        if app_date < birth_date:
            messagebox.showerror("Error!", "Birthdate should be earlier than appointment date")
            self.patient_appdate_entry.delete(0, 'end')
            self.patient_appdate_entry.focus_set()
            return

        if self.application.repo.patient_exists(name, address, birth_date_str, app_date_str, doctor_name, conclusion):
            messagebox.showerror("Error", "Same patient is already exist")
            self.patient_name_entry.delete(0, 'end')
            self.patient_address_entry.delete(0, 'end')
            self.patient_conclusion_entry.delete(0, 'end')
            self.patient_name_entry.focus_set()
            return

        self.application.repo.add_patient(name, address, birth_date_str, app_date_str, doctor_name, conclusion)
        self.application.update_patient_data()
        messagebox.showinfo("Success!", "Patient has been successfully added.")
        self.destroy()


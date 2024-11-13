import tkinter as tk
from tkinter import ttk, messagebox
from controller.SearchController import SearchController
from tkcalendar import DateEntry
from controller.CriteriaController import Criteria


class DeleteWindow(tk.Toplevel):
    def __init__(self, master, application):
        super().__init__(master=master)
        self.title("Delete Patient")
        self.application = application

        self.criteria_values = [
            Criteria.NAME.value,
            Criteria.ADDRESS.value,
            Criteria.DOCNAME.value,
            Criteria.APPDATE.value,
            Criteria.BIRTHDATE.value
        ]

        # Checkbox variables
        self.name_checkbox_var = tk.BooleanVar()
        self.address_checkbox_var = tk.BooleanVar()
        self.doctor_name_checkbox_var = tk.BooleanVar()
        self.last_appointment_checkbox_var = tk.BooleanVar()
        self.birthdate_checkbox_var = tk.BooleanVar()

        # Initialize widgets
        self.init_widgets()

    def init_widgets(self):
        ttk.Label(self, text="Patient's Full Name:").pack()
        self.name_entry = ttk.Entry(self, state=tk.DISABLED)
        self.name_entry.pack()
        ttk.Checkbutton(self, text="Delete by Full Name", variable=self.name_checkbox_var,
                        command=lambda: self.toggle_entry_state(self.name_entry, self.name_checkbox_var)).pack()

        ttk.Label(self, text="Birth Date:").pack()
        self.birthdate_entry = DateEntry(self, state='disabled', readonly=True)
        self.birthdate_entry.pack()
        ttk.Checkbutton(self, text="Delete by Birth Date", variable=self.birthdate_checkbox_var,
                        command=lambda: self.toggle_entry_state(self.birthdate_entry, self.birthdate_checkbox_var)).pack()

        ttk.Label(self, text="Registered Address:").pack()
        self.address_entry = ttk.Entry(self, state=tk.DISABLED)
        self.address_entry.pack()
        ttk.Checkbutton(self, text="Delete by Address", variable=self.address_checkbox_var,
                        command=lambda: self.toggle_entry_state(self.address_entry, self.address_checkbox_var)).pack()

        ttk.Label(self, text="Doctor's Full Name:").pack()
        self.doctor_name_entry = ttk.Entry(self, state=tk.DISABLED)
        self.doctor_name_entry.pack()
        ttk.Checkbutton(self, text="Delete by Doctor's Full Name", variable=self.doctor_name_checkbox_var,
                        command=lambda: self.toggle_entry_state(self.doctor_name_entry, self.doctor_name_checkbox_var)).pack()

        ttk.Label(self, text="Last Appointment Date:").pack()
        self.last_appointment_entry = DateEntry(self, state='disabled', readonly=True)
        self.last_appointment_entry.pack()
        ttk.Checkbutton(self, text="Delete by Last Appointment Date", variable=self.last_appointment_checkbox_var,
                        command=lambda: self.toggle_entry_state(self.last_appointment_entry, self.last_appointment_checkbox_var)).pack()

        ttk.Button(self, text="Delete", command=self.delete_patient).pack()

    def toggle_entry_state(self, entry_widget, checkbox_var):
        state = tk.NORMAL if checkbox_var.get() else tk.DISABLED
        entry_widget.config(state=state)

    def delete_patient(self):
        from datetime import datetime

        criteria_value = None
        birth_date_str = None
        app_date_str = None

        if self.name_checkbox_var.get():
            criteria_value = Criteria.NAME.value
        elif self.address_checkbox_var.get():
            criteria_value = Criteria.ADDRESS.value
        elif self.doctor_name_checkbox_var.get():
            criteria_value = Criteria.DOCNAME.value
        elif self.last_appointment_checkbox_var.get():
            criteria_value = Criteria.APPDATE.value
            app_date_str = self.last_appointment_entry.get()
            try:
                app_date = datetime.strptime(app_date_str, "%m/%d/%y")
                app_date_str = app_date.strftime("%m/%d/%Y")
            except ValueError:
                try:
                    app_date = datetime.strptime(app_date_str,  "%-m/%-d/%y")
                    app_date_str = app_date.strftime("%m/%d/%Y")
                except ValueError:
                    messagebox.showerror("Error!", "Incorrect date. Expected: MM/DD/YYYY")
                    self.last_appointment_entry.delete(0, 'end')
                    self.last_appointment_entry.focus_set()
                return
        elif self.birthdate_checkbox_var.get():
            criteria_value = Criteria.BIRTHDATE.value
            birth_date_str = self.birthdate_entry.get()

            try:
                birth_date = datetime.strptime(birth_date_str,  "%m/%d/%y")
                birth_date_str = birth_date.strftime("%m/%d/%Y")
            except ValueError:
                try:
                    birth_date = datetime.strptime(birth_date_str, "%-m/%-d/%y")
                    birth_date_str = birth_date.strftime("%m/%d/%Y")
                except ValueError:
                    messagebox.showerror("Error!", "Incorrect date. Expected: MM/DD/YYYY")
                    self.birthdate_entry.delete(0, 'end')
                    self.birthdate_entry.focus_set()
                return

        search = SearchController(
            self.name_entry.get(), self.address_entry.get(), birth_date_str,
            app_date_str, self.doctor_name_entry.get(), None, 0, 0, criteria_value
        )
        amount_of_deleted_elements = self.application.repo.delete_patients(search)
        if amount_of_deleted_elements > 0:
            messagebox.showinfo("Patient Deletion", f"Successfully deleted {amount_of_deleted_elements} patients")
        else:
            messagebox.showinfo("Patient Deletion", "No patients found for the given criteria")

        self.name_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.doctor_name_entry.delete(0, 'end')
        self.birthdate_entry.delete(0, 'end')
        self.last_appointment_entry.delete(0, 'end')
        self.application._update_all_data()

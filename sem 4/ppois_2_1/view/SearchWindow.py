import tkinter as tk
from tkinter import ttk, messagebox
from controller.CriteriaController import Criteria
from tkcalendar import DateEntry
from view.CenteredWindowHelper import center_window
class SearchWindow(tk.Toplevel):
    def __init__(self, master, application):
        super().__init__(master=master)

        self.title("Search patients")
        self.application = application

        ttk.Label(self, text="Patient's Surname:").pack()
        surname_var = tk.StringVar()
        self.surname_entry = ttk.Entry(self, textvariable=surname_var, state=tk.DISABLED)
        self.surname_entry.pack()
        self.surname_checkbox_var = tk.BooleanVar()
        surname_checkbox = ttk.Checkbutton(self, text="Search by Surname", variable=self.surname_checkbox_var,
                                           command=lambda: self.toggle_entry_state(self.surname_entry, self.surname_checkbox_var))
        surname_checkbox.pack()
        ttk.Label(self, text="Registered Address:").pack()
        address_var = tk.StringVar()
        self.address_entry = ttk.Entry(self, textvariable=address_var, state=tk.DISABLED)
        self.address_entry.pack()
        self.address_checkbox_var = tk.BooleanVar()
        address_checkbox = ttk.Checkbutton(self, text="Search by Address", variable=self.address_checkbox_var,
                                           command=lambda: self.toggle_entry_state(self.address_entry, self.address_checkbox_var))
        address_checkbox.pack()
        ttk.Label(self, text="Birth Date:").pack()
        dob_var = tk.StringVar()
        self.dob_entry = DateEntry(self, textvariable=dob_var, state='readonly')
        self.dob_entry.pack()
        self.dob_checkbox_var = tk.BooleanVar()
        dob_checkbox = ttk.Checkbutton(self, text="Search by Birth Date", variable=self.dob_checkbox_var,
                                       command=lambda: self.toggle_entry_state(self.dob_entry, self.dob_checkbox_var))
        dob_checkbox.pack()
        ttk.Label(self, text="Doctor's Full Name:").pack()
        docname_var = tk.StringVar()  # Used for the Entry widget
        self.docname_entry = ttk.Entry(self, textvariable=docname_var, state=tk.DISABLED)
        self.docname_entry.pack()

        self.docname_checkbox_var = tk.BooleanVar()  # Used for the Checkbutton
        docname_checkbox = ttk.Checkbutton(self,
                                           text="Search by Doctor's Full Name",
                                           variable=self.docname_checkbox_var,
                                           command=lambda: self.toggle_entry_state(
                                               self.docname_entry,
                                               self.docname_checkbox_var))
        docname_checkbox.pack()

        ttk.Label(self, text="Last Appointment Date:").pack()
        last_visit_var = tk.StringVar()
        self.last_visit_entry = DateEntry(self, textvariable=last_visit_var, state='readonly')
        self.last_visit_entry.pack()
        self.last_visit_checkbox_var = tk.BooleanVar()
        last_visit_checkbox = ttk.Checkbutton(self,
                                                        text="Search by Last Appointment Date",
                                                        variable=self.last_visit_checkbox_var,
                                                        command=lambda: self.toggle_entry_state(
                                                            self.last_visit_entry,
                                                            self.last_visit_checkbox_var))
        last_visit_checkbox.pack()
        ttk.Button(self, text="Search", command = self.search_records).pack()
        ttk.Button(self, text="Reset", command=lambda: self.reset_search_fields(
            self.surname_entry, self.address_entry, self.dob_entry, self.last_visit_entry, self.docname_entry)).pack()

    def toggle_entry_state(self, entry_widget, checkbox_var):
        state = tk.NORMAL if checkbox_var.get() else tk.DISABLED
        entry_widget.config(state=state)

    def reset_search_fields(self, *entry_widgets):
        for entry_widget in entry_widgets:
            entry_widget.delete(0, tk.END)

    def search_records(self):
        from datetime import datetime

        # Check if any search criteria is selected and filled
        if not (self.surname_checkbox_var.get() or
                self.address_checkbox_var.get() or
                self.dob_checkbox_var.get() or
                self.last_visit_checkbox_var.get() or
                self.docname_checkbox_var.get()):
            messagebox.showerror("Error", "Select and fill in at least one field for search")
            return

        try:
            criteria_value = None
            dob_str = None
            last_visit_str = None

            if self.surname_checkbox_var.get():
                criteria_value = Criteria.NAME.value
            elif self.address_checkbox_var.get():
                criteria_value = Criteria.ADDRESS.value
            elif self.dob_checkbox_var.get():
                criteria_value = Criteria.BIRTHDATE.value
                dob_str = self.dob_entry.get()
                try:
                    dob = datetime.strptime(dob_str, "%m/%d/%y")
                    dob_str = dob.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
                except ValueError:
                    try:
                        # Try parsing with single digit month and day
                        dob = datetime.strptime(dob_str, "%-m/%-d/%y")
                        dob_str = dob.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
                    except ValueError:
                        messagebox.showerror("Error!", "Incorrect date. Expected: MM/DD/YYYY")
                        self.dob_entry.delete(0, 'end')
                        self.dob_entry.focus_set()
                        return
            elif self.last_visit_checkbox_var.get():
                criteria_value = Criteria.APPDATE.value
                last_visit_str = self.last_visit_entry.get()
                try:
                    # Parse appointment date
                    last_visit = datetime.strptime(last_visit_str, "%m/%d/%y")  # Updated format here
                    last_visit_str = last_visit.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
                except ValueError:
                    try:
                        last_visit = datetime.strptime(last_visit_str, "%-m/%-d/%y")
                        last_visit_str = last_visit.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format
                    except ValueError:
                        messagebox.showerror("Error!", "Incorrect date. Expected: MM/DD/YYYY")
                        self.last_visit_entry.delete(0, 'end')
                        self.last_visit_entry.focus_set()
                        return
            elif self.docname_checkbox_var.get():
                criteria_value = Criteria.DOCNAME.value

            result = self.application.search_result(
                (self.surname_entry.get(), self.address_entry.get(), dob_str,
                 last_visit_str, self.docname_entry.get(), None, 0, 0, criteria_value)
            )

        except (AttributeError, ValueError) as e:
            return







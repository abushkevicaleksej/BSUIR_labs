from __future__ import annotations
import math
from view.DeleteWindow import DeleteWindow
from controller.FileController import FileController
from controller.DbController import DbController
from tkinter import filedialog as fd
from view.AddPatientWindow import AddPatientWindow
from view.AddDoctorWindow import AddDoctorWindow
from view.CreateFileWindow import CreateFileWindow
import tkinter as tk
import tkinter.messagebox as messagebox
import re
from view.SearchWindow import SearchWindow
from controller.SearchController import SearchController
from tkinter import ttk
from view.CenteredWindowHelper import center_window
from model.Patient import Patient
from view.FormSearchResultWindow import FormSearchResultWindow
from tkinter import *


class Application:
    def __init__(self):
        self.search_criteria = SearchController()
        self.delete_criteria = SearchController()
        self.repo = None
        self.patients_page = 0
        self.per_page_entry_patient = 0
        self.number_of_patients_page = 10
        self.doctors_page = 0
        self.per_page_entry_doctor = 0
        self.number_of_doctors_page = 10
        self.main_window = tk.Tk()
        self.main_window.title('Medical Database')
        self.main_window.geometry('800x600')
        self.__tree_view: BooleanVar = BooleanVar(value=False)
        center_window(self.main_window, 800, 600)
        self.create_menu()
        self.create_tabs()
        self.main_window.bind_all('<Control-o>', self.open_file)
        self.main_window.bind_all('<Control-q>', self.quit_program)
        self.main_window.bind_all('<Control-n>', self.create_file)
        self.main_window.bind_all('<Control-p>', self.open_add_patient_window)
        self.main_window.bind_all('<Control-d>', self.open_add_doctor_window)
        self.main_window.mainloop()

    def get_doctor_id_by_name(self, doctor_name):
        doctor_id = self.repo.get_doctor_id_by_name(doctor_name)
        return doctor_id

    def create_menu(self):
        menubar = tk.Menu(self.main_window)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New File', accelerator="Ctrl+N", command=self.create_file)
        file_menu.add_command(label='Open File', accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label='Quit', accelerator="Ctrl+Q", command=self.quit_program)
        add_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Add', menu=add_menu)
        add_menu.add_command(label='Add Patient', accelerator="Ctrl+P",
                             command=self.open_add_patient_window)
        add_menu.add_command(label='Add Doctor', accelerator="Ctrl+D", command=self.open_add_doctor_window)
        delete_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Delete', menu=delete_menu)
        delete_menu.add_command(label='Delete Record', command=self.open_delete_window)
        search_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Search', menu=search_menu)
        search_menu.add_command(label='Search Records', command=self.open_search_window)
        self.main_window.config(menu=menubar)

    def check_doctors_and_open_add_patient_window(self):
        if not self.repo.get_doctors():
            messagebox.showwarning("No Doctors", "There are no doctors. Would you like to add one?")
        else:
            AddPatientWindow(self.main_window, self)

    def _update_all_data(self, a=None, b=None, c=None):
        self.update_doctor_data()
        self.update_patient_data()

    def close_data_source(self):
        self.repo = None

    def quit_program(self, event = None):
        self.main_window.destroy()

    def create_file(self, event = None):
        CreateFileWindow(self.main_window)

    def open_add_patient_window(self, event=None):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
        else:
            self.check_doctors_and_open_add_patient_window()

    def open_add_doctor_window(self, event=None):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
        else:
            AddDoctorWindow(self.main_window, self)

    def open_delete_window(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
        elif not self.repo.get_patients():
            tk.messagebox.showinfo(title='Error', message='Please, fill the patients list')
        else:
            DeleteWindow(self.main_window, self)

    def open_search_window(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
        elif not self.repo.get_patients():
            tk.messagebox.showinfo(title='Error', message='Please, fill the patients list')
        else:
            SearchWindow(self.main_window, self)

    def search_result(self, values) -> None:
        search: SearchController = SearchController(*values)
        result_list: list[Patient] = self.repo.search_patients(search)

        if not result_list:
            messagebox.showinfo("Search", "Records are not found.")
            return

        FormSearchResultWindow(result_list)

    def get_tree_view_value(self):
        return self.__tree_view.get()

    def tree_view_switch(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        if self.__tree_view.get():
            self.patient_tree['show'] = 'tree'
            self.doctor_tree['show'] = 'tree'
        else:
            self.patient_tree['show'] = 'headings'
            self.doctor_tree['show'] = 'headings'
        self._update_all_data()

    def open_file(self, event=None):
        filetypes = [('DB files', '*.db'), ('XML files', '*.xml')]
        filename = fd.askopenfilename(title='Open file', filetypes=filetypes)

        if filename is not None and len(filename) > 0:
            if filename.endswith('.db'):
                self.repo = DbController(filename)
                self._update_all_data()
            elif filename.endswith('.xml'):
                self.close_data_source()
                self.repo = FileController(filename)
                self._update_all_data()

    @staticmethod
    def is_valid_string(name):
        return all(re.match(r'^[А-ЯA-Z][а-яa-z]*$', word) for word in name.split())

    def set_page_size_patients(self, event):
        try:
            value = int(self.per_page_entry_patient.get())
            if value < 1:
                messagebox.showerror("Error!", "Number should be > 0")
            else:
                self.number_of_patients_page = value
                self.patients_page = 0
                self.update_patient_data()
        except ValueError:
            messagebox.showerror("Error!", "Incorrect number format")

    def set_page_size_doctors(self, event):
        try:
            value = int(self.per_page_entry_doctor.get())
            if value < 1:
                messagebox.showerror("Error!", "Number should be > 0")
            else:
                self.number_of_doctors_page = value
                self.doctors_page = 0
                self.update_doctor_data()
        except ValueError:
            messagebox.showerror("Error!", "Incorrect number format")

    def create_tabs(self):
        tab_control = ttk.Notebook()
        tab_control.pack(expand=1, fill='both')
        patients_tab = ttk.Frame(tab_control)
        tab_control.add(patients_tab, text='Patients')
        self.create_patients_table(patients_tab)
        doctors_tab = ttk.Frame(tab_control)
        tab_control.add(doctors_tab, text='Doctors')
        self.create_doctors_table(doctors_tab)

    def create_patients_table(self, parent):
        columns = ['ID', 'Name', 'Address', 'Birth Date', 'Appointment Date', 'Doctor', 'Conclusion']
        tree = ttk.Treeview(parent, columns=columns, show='headings')
        tree.pack(expand=1, fill='both')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        ttk.Checkbutton(parent, text='Show Tree', variable=self.__tree_view, command=self.tree_view_switch).pack()
        self.patients_page = 0
        self.patients_per_page = tk.IntVar(value=10)
        self.patient_tree = tree

        self.per_page_entry_patient = ttk.Entry(parent, textvariable=self.patients_per_page)
        self.per_page_entry_patient.pack()
        self.per_page_entry_patient.bind('<Return>', self.set_page_size_patients)

        ttk.Button(parent, text='First Page', command=self.first_page_patients).pack(side=tk.LEFT)
        ttk.Button(parent, text='Prev', command=self.prev_page_patients).pack(side=tk.LEFT)
        ttk.Button(parent, text='Next', command=self.next_page_patients).pack(side=tk.LEFT)
        ttk.Button(parent, text='Last Page', command=self.last_page_patients).pack(side=tk.LEFT)

        self.load_patient_data()

        self.patient_page_label = ttk.Label(parent, text="")
        self.patient_page_label.pack()
        self.update_page_label_patients()

        self.record_count_label_patients = ttk.Label(parent, text="")
        self.record_count_label_patients.pack()
        self.update_record_count_label_patients()

    def create_doctors_table(self, parent):
        columns = ['ID', 'Name', 'Specialization']
        tree = ttk.Treeview(parent, columns=columns, show='headings')
        tree.pack(expand=1, fill='both')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        ttk.Checkbutton(parent, text='Show Tree', variable=self.__tree_view, command=self.tree_view_switch).pack()
        self.doctors_page = 0
        self.doctors_per_page = tk.IntVar(value=10)
        self.doctor_tree = tree

        self.per_page_entry_doctor = ttk.Entry(parent, textvariable=self.doctors_per_page)
        self.per_page_entry_doctor.pack()
        self.per_page_entry_doctor.bind('<Return>', self.set_page_size_doctors)

        ttk.Button(parent, text='First Page', command=self.first_page_doctors).pack(side=tk.LEFT)
        ttk.Button(parent, text='Prev', command=self.prev_page_doctors).pack(side=tk.LEFT)
        ttk.Button(parent, text='Next', command=self.next_page_doctors).pack(side=tk.LEFT)
        ttk.Button(parent, text='Last Page', command=self.last_page_doctors).pack(side=tk.LEFT)

        self.load_doctor_data()

        self.doctor_page_label = ttk.Label(parent, text="")
        self.doctor_page_label.pack()
        self.update_page_label_doctors()

        self.record_count_label_doctors = ttk.Label(parent, text="")
        self.record_count_label_doctors.pack()
        self.update_record_count_label_doctors()

    def load_patient_data(self, query=None, parameters=None):
        try:
            self.patient_tree.delete(*self.patient_tree.get_children())
            query = """
                SELECT id, name, address, birth_date,
                        appointment_date, doctor_id, conclusion
                FROM Patients
                LIMIT ? OFFSET ?
                """
            parameters = (self.patients_per_page.get(), self.patients_per_page.get() * self.patients_page)
            for record in self.repo.cursor.execute(query, parameters):
                self.patient_tree.insert('', tk.END, values=record)
        except AttributeError:
            pass

    def load_doctor_data(self):
        try:
            self.doctor_tree.delete(*self.doctor_tree.get_children())
            query = """
                SELECT id, name, specialization
                FROM Doctors
                LIMIT ? OFFSET ?
            """
            parameters = (self.doctors_per_page.get(), self.doctors_per_page.get() * self.doctors_page)
            for record in self.repo.cursor.execute(query, parameters):
                self.doctor_tree.insert('', tk.END, values=record)
        except AttributeError:
            pass

    def update_patient_data(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        for item in self.patient_tree.get_children():
            self.patient_tree.delete(item)
        start = self.patients_page * self.number_of_patients_page
        end = start + self.number_of_patients_page
        for patient in self.repo.get_patients()[start:end]:
            if not self.__tree_view.get():
                self.patient_tree.insert("", END, values=patient.tuple())
            else:
                patient_row = self.patient_tree.insert("", tk.END, text='Patient')
                self.patient_tree.insert(patient_row, tk.END, text='Id', values=patient.get_id())
                self.patient_tree.insert(patient_row, tk.END, text='Name', values=patient.get_name())
                self.patient_tree.insert(patient_row, tk.END, text='Address', values=patient.get_address())
                self.patient_tree.insert(patient_row, tk.END, text='Birthdate', values=patient.get_birthdate())
                self.patient_tree.insert(patient_row, tk.END, text='Appdate', values=patient.get_appdate())
                docname_row = self.patient_tree.insert(patient_row, tk.END, text='Docname',
                                                       values=patient.get_docname())
                doctor = self.repo.get_doctor_by_name(patient.get_docname())
                if doctor:
                    self.patient_tree.insert(docname_row, tk.END, text='Id', values=doctor.get_id())
                    self.patient_tree.insert(docname_row, tk.END, text='Specialization',
                                             values=doctor.get_specialization())
                self.patient_tree.insert(patient_row, tk.END, text='Concl', values=patient.get_concl())
        self.update_page_label_patients()
        self.update_record_count_label_patients()

    def update_doctor_data(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        for item in self.doctor_tree.get_children():
            self.doctor_tree.delete(item)
        start = self.doctors_page * self.number_of_doctors_page
        end = start + self.number_of_doctors_page
        for doctor in self.repo.get_doctors()[start:end]:
            if not self.__tree_view.get():
                self.doctor_tree.insert("",END,values=doctor.tuple())
            else:
                doctor_row = self.doctor_tree.insert("", tk.END, text='Doctor')
                self.doctor_tree.insert(doctor_row, tk.END, text='Id', values=doctor.get_id())
                self.doctor_tree.insert(doctor_row, tk.END, text='Docname', values=doctor.get_docname())
                self.doctor_tree.insert(doctor_row, tk.END, text='Specialization', values=doctor.get_specialization())
        self.update_page_label_doctors()
        self.update_record_count_label_doctors()

    def update_record_count_label_patients(self):

        try:
            total_records = self.repo.count_patients_amount()
            start_index = self.patients_page * self.patients_per_page.get()
            end_index = min((self.patients_page + 1) * self.patients_per_page.get(), total_records)
            record_count_text = f"{end_index - start_index} of {total_records} entities on the page"
            self.record_count_label_patients.config(text=record_count_text)
        except AttributeError:
            self.record_count_label_patients.config(text="0 of 0 entities on the page")

    def update_record_count_label_doctors(self):
        try:
            total_records = self.repo.count_doctors_amount()
            start_index = self.doctors_page * self.doctors_per_page.get()
            end_index = min((self.doctors_page + 1) * self.doctors_per_page.get(), total_records)
            record_count_text = f"{end_index - start_index} of {total_records} entities on the page"
            self.record_count_label_doctors.config(text=record_count_text)
        except AttributeError:
            self.record_count_label_doctors.config(text="0 of 0 entities on the page")

    def first_page_patients(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        self.patients_page = 0
        self.update_patient_data()

    def first_page_doctors(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        self.doctors_page = 0
        self.update_doctor_data()

    def last_page_patients(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        self.patients_page = math.ceil(self.repo.count_patients_amount()
                                       / int(self.number_of_patients_page)) - 1
        self.update_patient_data()

    def last_page_doctors(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        self.doctors_page = math.ceil(self.repo.count_doctors_amount()
                                      / int(self.number_of_doctors_page)) - 1
        self.update_doctor_data()

    def next_page_patients(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        total_records = self.repo.count_patients_amount()
        total_pages = (total_records + self.patients_per_page.get() - 1) // self.patients_per_page.get()
        if self.patients_page < total_pages - 1:
            self.patients_page += 1
        else:
            messagebox.showinfo("Info", "No more records to display")
        self.update_patient_data()

    def next_page_doctors(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        total_records = self.repo.count_doctors_amount()
        total_pages = (total_records + self.doctors_per_page.get() - 1) // self.doctors_per_page.get()
        if self.doctors_page < total_pages - 1:
            self.doctors_page += 1
        else:
            messagebox.showinfo("Info", "No more records to display")
        self.update_doctor_data()

    def prev_page_patients(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        if self.patients_page > 0:
            self.patients_page -= 1
        else:
            messagebox.showinfo("Info", "This is the first page")
        self.update_patient_data()

    def prev_page_doctors(self):
        if self.repo is None:
            tk.messagebox.showinfo(title='Error', message='Please, open data source')
            return
        if self.doctors_page > 0:
            self.doctors_page -= 1
        else:
            messagebox.showinfo("Info", "This is the first page")
        self.update_doctor_data()

    def update_page_label_patients(self):
        try:
            total_records = self.repo.count_patients_amount()
            total_pages = (total_records + self.patients_per_page.get() - 1) // self.patients_per_page.get()
            self.patient_page_label.config(text=f"Page {self.patients_page + 1} of {total_pages}")
        except AttributeError:
            self.patient_page_label.config(text="Page 1 of 1")

    def update_page_label_doctors(self):
        try:
            total_records = self.repo.count_doctors_amount()
            total_pages = (total_records + self.doctors_per_page.get() - 1) // self.doctors_per_page.get()
            self.doctor_page_label.config(text=f"Page {self.doctors_page + 1} of {total_pages}")
        except AttributeError:
            self.doctor_page_label.config(text="Page 1 of 1")

    def add_pagination_buttons_patients(self, parent):
        prev_button = ttk.Button(parent, text='Prev', command=self.prev_page_patients)
        prev_button.pack(side=tk.LEFT)
        next_button = ttk.Button(parent, text='Next', command=self.next_page_patients)
        next_button.pack(side=tk.RIGHT)

    def add_pagination_buttons_doctors(self, parent):
        prev_button = ttk.Button(parent, text='Prev', command=self.prev_page_doctors)
        prev_button.pack(side=tk.LEFT)
        next_button = ttk.Button(parent, text='Next', command=self.next_page_doctors)
        next_button.pack(side=tk.RIGHT)


import sqlite3
import tkinter
import tkinter as tk
import xml.sax
from tkinter import ttk, filedialog
import tkinter.messagebox as messagebox
import re
from tkcalendar import DateEntry

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def to_tuple(self):
        return (self.name, self.specialization)

    def __str__(self):
        return f"Doctor Name: {self.name}, Specialization: {self.specialization}"

class Patient:
    def __init__(self, name, address, birth_date, appointment_date, doctor_id, conclusion):
        self.name = name
        self.address = address
        self.birth_date = birth_date
        self.appointment_date = appointment_date
        self.doctor_id = doctor_id
        self.conclusion = conclusion

    def to_tuple(self):
        return (self.name, self.address, self.birth_date, self.appointment_date, self.doctor_id, self.conclusion)

    def __str__(self):
        return (f"Patient Name: {self.name}, Address: {self.address}, "
                f"Birth Date: {self.birth_date}, Appointment Date: {self.appointment_date}, "
                f"Doctor ID: {self.doctor_id}, Conclusion: {self.conclusion}")
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctors (
                id INTEGER PRIMARY KEY,
                name TEXT,
                specialization TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patients (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                birth_date DATE,
                appointment_date DATE,
                doctor_id INTEGER,
                conclusion TEXT,
                FOREIGN KEY (doctor_id) REFERENCES Doctors(id)
            )
        """)
        self.conn.commit()

    def get_cursor(self):
        return self.conn.cursor()

    def add_patient(self, name, address, birth_date, appointment_date, doctor_id, conclusion):
        cursor = self.get_cursor()
        cursor.execute("""
            INSERT INTO Patients (name, address, birth_date, appointment_date, doctor_id, conclusion)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, address, birth_date, appointment_date, doctor_id, conclusion))
        self.conn.commit()
        print("Пациент добавлен")

    def add_doctor(self, name, specialization):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Doctors (name, specialization)
            VALUES (?, ?)
        """, (name, specialization))
        self.conn.commit()
        print("Врач добавлен")

    def edit_patient(self, id, name, address, birth_date, appointment_date, doctor_id, conclusion):
        self.cursor.execute("""
            UPDATE Patients
            SET name = ?, address = ?, birth_date = ?, appointment_date = ?, doctor_id = ?, conclusion = ?
            WHERE id = ?
        """, (name, address, birth_date, appointment_date, doctor_id, conclusion, id))
        self.conn.commit()

    def edit_doctor(self, id, name, specialization):
        self.cursor.execute("""
            UPDATE Doctors
            SET name = ?, specialization = ?
            WHERE id = ?
        """, (name, specialization, id))
        self.conn.commit()

    def get_doctor_name_by_id(self, doctor_id):
        doctor_name = self.cursor.execute('SELECT name FROM Doctors WHERE id = ?', (doctor_id,)).fetchone()
        return doctor_name[0] if doctor_name else None

    def get_doctor_id_by_name(self, doctor_name):
        query = "SELECT id FROM Doctors WHERE name = ?" 

        result = self.cursor.execute(query, (doctor_name,)).fetchone()
        return result[0] if result else None


class MySAXHandler(xml.sax.ContentHandler):
    def __init__(self, db, app):
        self.db = db
        self.app = app  # Store the app reference for UI updates
        self.current_element = ''
        self.current_patient = {}
        self.current_doctor = {}
        self.patients_to_add = []
        self.doctors_to_add = []

    def startElement(self, name, attrs):
        self.current_element = name
        if name == 'patient':
            self.current_patient = {}
        elif name == 'doctor':
            self.current_doctor = {}

    def endElement(self, name):
        if name == 'doctor':
            if 'name' in self.current_doctor and 'specialization' in self.current_doctor:
                self.doctors_to_add.append(self.current_doctor.copy())
            self.current_doctor = {}
        elif name == 'patient':
            if 'doctor' in self.current_patient:
                self.patients_to_add.append(self.current_patient.copy())
            self.current_patient = {}

    def characters(self, content):
        content = content.strip()
        if content:
            if self.current_element in ['name', 'address', 'birth_date', 'appointment_date', 'doctor', 'conclusion']:
                self.current_patient[self.current_element] = content
            elif self.current_element in ['name', 'specialization']:
                self.current_doctor[self.current_element] = content

    def endDocument(self):
        # Add collected doctors to the database
        for doctor in self.doctors_to_add:
            self.db.add_doctor(doctor['name'], doctor['specialization'])

        # Add collected patients to the database
        for patient in self.patients_to_add:
            doctor_id = self.db.get_doctor_id_by_name(patient['doctor'])
            if doctor_id is not None:
                self.db.add_patient(patient['name'], patient['address'],
                                    patient['birth_date'], patient['appointment_date'],
                                    doctor_id, patient['conclusion'])

        # Update the UI here if needed
        self.app.update_table()
        self.app.update()


class Application(tk.Tk):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.title('Medical Database')
        self.geometry('800x600')
        self.create_menu()
        self.create_tabs()
        self.patients_page = 0
        self.doctors_page = 0

    def get_doctor_id_by_name(self, doctor_name):
        doctor_id = self.db.get_doctor_id_by_name(doctor_name)
        return doctor_id

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        view_menu = tk.Menu(menubar, tearoff=0)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New')
        file_menu.add_command(label='Open...')
        file_menu.add_command(label='Save')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)
        add_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Add', menu=add_menu)
        add_menu.add_command(label='Add Patient/Doctor', command=self.open_add_window)
        delete_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Delete', menu=delete_menu)
        delete_menu.add_command(label='Delete Record', command=self.open_delete_window)
        search_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Search', menu=search_menu)
        search_menu.add_command(label='Search Records', command=self.open_search_window)

    def open_add_window(self):
        add_window = tk.Toplevel(self)
        add_window.title("Добавить пациента/врача")
        notebook = ttk.Notebook(add_window)
        notebook.pack(fill='both', expand=True)
        patient_tab = ttk.Frame(notebook)
        notebook.add(patient_tab, text="Пациент")
        self.add_patient_form(patient_tab)
        doctor_tab = ttk.Frame(notebook)
        notebook.add(doctor_tab, text="Врач")
        self.add_doctor_form(doctor_tab)

    def toggle_entry_state(self, entry_widget, checkbox_var):
        state = tk.NORMAL if checkbox_var.get() else tk.DISABLED
        entry_widget.config(state=state)

    def open_delete_window(self):
        delete_window = tk.Toplevel(self)
        delete_window.title("Удалить пациента")
        ttk.Label(delete_window, text="ФИО пациента:").pack()
        name_var = tk.StringVar()
        name_entry = ttk.Entry(delete_window, textvariable=name_var, state=tk.DISABLED)
        name_entry.pack()
        name_checkbox_var = tk.BooleanVar()
        name_checkbox = ttk.Checkbutton(delete_window, text="Удалить по ФИО", variable=name_checkbox_var,
                                        command=lambda: self.toggle_entry_state(name_entry, name_checkbox_var))
        name_checkbox.pack()
        ttk.Label(delete_window, text="Адрес прописки:").pack()
        address_var = tk.StringVar()
        address_entry = ttk.Entry(delete_window, textvariable=address_var, state=tk.DISABLED)
        address_entry.pack()
        address_checkbox_var = tk.BooleanVar()
        address_checkbox = ttk.Checkbutton(delete_window, text="Удалить по адресу", variable=address_checkbox_var,
                                           command=lambda: self.toggle_entry_state(address_entry, address_checkbox_var))
        address_checkbox.pack()
        ttk.Label(delete_window, text="ФИО врача:").pack()
        doctor_name_var = tk.StringVar()
        doctor_name_entry = ttk.Entry(delete_window, textvariable=doctor_name_var, state=tk.DISABLED)
        doctor_name_entry.pack()
        doctor_name_checkbox_var = tk.BooleanVar()
        doctor_name_checkbox = ttk.Checkbutton(delete_window, text="Удалить по ФИО врача",
                                               variable=doctor_name_checkbox_var,
                                               command=lambda: self.toggle_entry_state(doctor_name_entry,
                                                                                       doctor_name_checkbox_var))
        doctor_name_checkbox.pack()
        ttk.Label(delete_window, text="Дата последнего приема (ГГГГ-ММ-ДД):").pack()
        last_appointment_var = tk.StringVar()
        last_appointment_entry = ttk.Entry(delete_window, textvariable=last_appointment_var, state=tk.DISABLED)
        last_appointment_entry.pack()
        last_appointment_checkbox_var = tk.BooleanVar()
        last_appointment_checkbox = ttk.Checkbutton(delete_window, text="Удалить по дате последнего приема",
                                                    variable=last_appointment_checkbox_var,
                                                    command=lambda: self.toggle_entry_state(last_appointment_entry,
                                                                                            last_appointment_checkbox_var))
        last_appointment_checkbox.pack()
        ttk.Button(delete_window, text="Удалить", command=lambda: self.delete_patient(
            name_var.get(), address_var.get(), doctor_name_var.get(), last_appointment_var.get(),
            name_checkbox_var.get(), address_checkbox_var.get(), doctor_name_checkbox_var.get(),
            last_appointment_checkbox_var.get())).pack()

    def search_records(self, surname, address, dob, doctor_or_last_visit, search_by_surname, search_by_address,
                       search_by_dob, search_by_doctor_or_last_visit):
        if not (search_by_surname or search_by_address or search_by_dob or search_by_doctor_or_last_visit):
            messagebox.showwarning("Предупреждение", "Выберите критерий поиска.")
            return
        query_conditions = []
        query_parameters = []
        if search_by_surname:
            query_conditions.append("Patients.name LIKE ?")
            query_parameters.append(f"%{surname}%")
        if search_by_address:
            query_conditions.append("Patients.address LIKE ?")
            query_parameters.append(f"%{address}%")
        if search_by_dob:
            query_conditions.append("Patients.birth_date = ?")
            query_parameters.append(dob)
        if search_by_doctor_or_last_visit:
            query_conditions.append("(Doctors.name LIKE ? OR Patients.appointment_date = ?)")
            query_parameters.extend([f"%{doctor_or_last_visit}%", doctor_or_last_visit])
        query = """
            SELECT Patients.id, Patients.name AS patient_name, Patients.address, Patients.birth_date, 
                   Patients.appointment_date, Doctors.name AS doctor_name, Patients.conclusion
            FROM Patients
            JOIN Doctors ON Patients.doctor_id = Doctors.id
            WHERE """ + " AND ".join(query_conditions)
        self.load_patient_data(query, tuple(query_parameters))

    def delete_patient(self, name, address, doctor_name, last_appointment_date,
                       delete_by_name, delete_by_address, delete_by_doctor_name, delete_by_last_appointment):
        if not (delete_by_name or delete_by_address or delete_by_doctor_name or delete_by_last_appointment):
            messagebox.showwarning("Предупреждение", "Выберите критерий удаления.")
            return
        query_conditions = []
        query_parameters = []
        if delete_by_name:
            query_conditions.append("name LIKE ?")
            query_parameters.append(f"%{name}%")
        if delete_by_address:
            query_conditions.append("address LIKE ?")
            query_parameters.append(f"%{address}%")
        if delete_by_doctor_name:
            query_conditions.append("doctor_id IN (SELECT id FROM Doctors WHERE name LIKE ?)")
            query_parameters.append(f"%{doctor_name}%")
        if delete_by_last_appointment:
            query_conditions.append("appointment_date = ?")
            query_parameters.append(last_appointment_date)
        query = """
            DELETE FROM Patients
            WHERE """ + " AND ".join(query_conditions)
        self.db.cursor.execute(query, tuple(query_parameters))
        self.db.conn.commit()
        self.load_patient_data()
        messagebox.showinfo("Удаление", "Пациенты удалены в соответствии с выбранными критериями.")

    def reset_search_fields(self, *entry_widgets):
        for entry_widget in entry_widgets:
            entry_widget.delete(0, tk.END)
        self.load_doctor_data()

    def open_search_window(self):
        search_window = tk.Toplevel(self)
        search_window.title("Поиск записей")
        ttk.Label(search_window, text="Фамилия пациента:").pack()
        surname_var = tk.StringVar()
        surname_entry = ttk.Entry(search_window, textvariable=surname_var, state=tk.DISABLED)
        surname_entry.pack()
        surname_checkbox_var = tk.BooleanVar()
        surname_checkbox = ttk.Checkbutton(search_window, text="Поиск по фамилии", variable=surname_checkbox_var,
                                           command=lambda: self.toggle_entry_state(surname_entry, surname_checkbox_var))
        surname_checkbox.pack()
        ttk.Label(search_window, text="Адрес прописки:").pack()
        address_var = tk.StringVar()
        address_entry = ttk.Entry(search_window, textvariable=address_var, state=tk.DISABLED)
        address_entry.pack()
        address_checkbox_var = tk.BooleanVar()
        address_checkbox = ttk.Checkbutton(search_window, text="Поиск по адресу", variable=address_checkbox_var,
                                           command=lambda: self.toggle_entry_state(address_entry, address_checkbox_var))
        address_checkbox.pack()
        ttk.Label(search_window, text="Дата рождения (ГГГГ-ММ-ДД):").pack()
        dob_var = tk.StringVar()
        dob_entry = ttk.Entry(search_window, textvariable=dob_var, state=tk.DISABLED)
        dob_entry.pack()
        dob_checkbox_var = tk.BooleanVar()
        dob_checkbox = ttk.Checkbutton(search_window, text="Поиск по дате рождения", variable=dob_checkbox_var,
                                       command=lambda: self.toggle_entry_state(dob_entry, dob_checkbox_var))
        dob_checkbox.pack()
        ttk.Label(search_window, text="ФИО врача или дата последнего приема:").pack()
        doctor_or_last_visit_var = tk.StringVar()
        doctor_or_last_visit_entry = ttk.Entry(search_window, textvariable=doctor_or_last_visit_var, state=tk.DISABLED)
        doctor_or_last_visit_entry.pack()
        doctor_or_last_visit_checkbox_var = tk.BooleanVar()
        doctor_or_last_visit_checkbox = ttk.Checkbutton(search_window,
                                                        text="Поиск по ФИО врача или дате последнего приема",
                                                        variable=doctor_or_last_visit_checkbox_var,
                                                        command=lambda: self.toggle_entry_state(
                                                            doctor_or_last_visit_entry,
                                                            doctor_or_last_visit_checkbox_var))
        doctor_or_last_visit_checkbox.pack()
        ttk.Button(search_window, text="Поиск", command=lambda: self.search_records(
            surname_var.get(), address_var.get(), dob_var.get(), doctor_or_last_visit_var.get(),
            surname_checkbox_var.get(), address_checkbox_var.get(), dob_checkbox_var.get(),
            doctor_or_last_visit_checkbox_var.get())).pack()
        ttk.Button(search_window, text="Сбросить", command=lambda: self.reset_search_fields(
            surname_entry, address_entry, dob_entry, doctor_or_last_visit_entry)).pack()

    def load_patient_data(self, query=None, parameters=None):
        self.patient_tree.delete(*self.patient_tree.get_children())
        if query is None:
            query = """
                SELECT Patients.id, Patients.name AS patient_name, Patients.address, Patients.birth_date, 
                       Patients.appointment_date, Doctors.name AS doctor_name, Patients.conclusion
                FROM Patients
                JOIN Doctors ON Patients.doctor_id = Doctors.id
                LIMIT ? OFFSET ?
            """
        if parameters is None:
            parameters = (self.patients_per_page.get(), self.patients_per_page.get() * self.patients_page)
        for record in self.db.cursor.execute(query, parameters):
            self.patient_tree.insert('', tk.END, values=record)

    def load_doctor_data(self):
        self.doctor_tree.delete(*self.doctor_tree.get_children())
        query = """
            SELECT id, name, specialization
            FROM Doctors
            LIMIT ? OFFSET ?
        """
        parameters = (self.doctors_per_page.get(), self.doctors_per_page.get() * self.doctors_page)
        for record in self.db.cursor.execute(query, parameters):
            self.doctor_tree.insert('', tk.END, values=record)

    def get_doctor_names(self):
        doctor_names = []
        query = "SELECT name FROM Doctors"
        doctors = self.db.cursor.execute(query).fetchall()
        for doctor in doctors:
            doctor_names.append(doctor[0])
        return doctor_names

    @staticmethod
    def is_valid_string(name):
        return all(re.match(r'^[А-ЯA-Z][а-яa-z]*$', word) for word in name.split())

    def add_patient_form(self, parent):
        self.load_doctor_data()
        ttk.Label(parent, text="Имя:").pack()
        patient_name_entry = ttk.Entry(parent)
        patient_name_entry.pack()
        ttk.Label(parent, text="Адрес:").pack()
        patient_address_entry = ttk.Entry(parent)
        patient_address_entry.pack()
        ttk.Label(parent, text="Дата рождения:").pack()
        patient_birthdate_entry = DateEntry(parent)
        patient_birthdate_entry.pack()
        ttk.Label(parent, text="Дата приёма:").pack()
        patient_appdate_entry = DateEntry(parent)
        patient_appdate_entry.pack()
        ttk.Label(parent, text="ФИО врача:").pack()
        doctor_names = self.get_doctor_names()
        patient_doctor_name_var = tk.StringVar()
        patient_doctor_name_combobox = ttk.Combobox(parent, textvariable=patient_doctor_name_var, values=doctor_names, state="readonly")

        patient_doctor_name_combobox.pack()
        ttk.Label(parent, text="Диагноз:").pack()
        patient_conclusion_entry = ttk.Entry(parent)
        patient_conclusion_entry.pack()
        ttk.Button(parent, text="Добавить", command=lambda: self.add_patient(
            patient_name_entry, patient_address_entry, patient_birthdate_entry,
            patient_appdate_entry, patient_doctor_name_combobox,
            patient_conclusion_entry) if self.is_valid_string(patient_name_entry.get()) else messagebox.showwarning(
            "Предупреждение", "Неверный формат имени.")).pack()

    def add_doctor_form(self, parent):
        ttk.Label(parent, text="Имя:").pack()
        doctor_name_entry = ttk.Entry(parent)
        doctor_name_entry.pack()
        ttk.Label(parent, text="Специализация:").pack()
        doctor_specialization_entry = ttk.Entry(parent)
        doctor_specialization_entry.pack()
        ttk.Button(parent, text="Добавить", command=lambda: self.add_doctor(
            doctor_name_entry, doctor_specialization_entry)).pack()

    def add_patient(self, name_entry, address_entry, birth_date_entry, appointment_date_entry, doctor_name_combobox,
                    conclusion_entry):
        name = name_entry.get()
        address = address_entry.get()
        birth_date = birth_date_entry.get()
        appointment_date = appointment_date_entry.get()
        doctor_name = doctor_name_combobox.get()
        conclusion = conclusion_entry.get()
        doctor_id = self.get_doctor_id_by_name(doctor_name)
        if doctor_id is not None:
            patient = Patient(name, address, birth_date, appointment_date, doctor_id, conclusion)
            self.db.add_patient(*patient.to_tuple())  # Распаковываем кортеж аргументов
            self.load_patient_data()
            name_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
            birth_date_entry.delete(0, tk.END)
            appointment_date_entry.delete(0, tk.END)
            doctor_name_combobox.set('')
            conclusion_entry.delete(0, tk.END)
            messagebox.showinfo("Добавление", "Пациент успешно добавлен.")
        else:
            messagebox.showwarning("Ошибка", "Врач не найден.")

    def add_doctor(self, name_entry, specialization_entry):
        name = name_entry.get()
        specialization = specialization_entry.get()
        doctor = Doctor(name, specialization)
        self.db.add_doctor(*doctor.to_tuple())  # Распаковываем кортеж аргументов
        self.load_doctor_data()
        name_entry.delete(0, tk.END)
        specialization_entry.delete(0, tk.END)
        messagebox.showinfo("Добавление", "Врач успешно добавлен.")

    def create_tabs(self):
        tab_control = ttk.Notebook(self)
        tab_control.pack(expand=1, fill='both')

        # Patients tab
        patients_tab = ttk.Frame(tab_control)
        tab_control.add(patients_tab, text='Patients')
        self.create_patients_table(patients_tab)

        # Doctors tab
        doctors_tab = ttk.Frame(tab_control)
        tab_control.add(doctors_tab, text='Doctors')
        self.create_doctors_table(doctors_tab)

    def create_patients_table(self, parent):
        columns = ['ID', 'Name', 'Address', 'Birth Date', 'Appointment Date', 'Doctor', 'Conclusion']
        self.show_mode = tk.StringVar(value='headings')
        tree = ttk.Treeview(parent, columns=columns, show='headings')
        tree.pack(expand=1, fill='both')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.column('#0', width=0, stretch=False)
        ttk.Checkbutton(parent, text='Show Tree', variable=self.show_mode, onvalue='tree', offvalue='headings',
                        command=lambda: tree.config(show=self.show_mode.get())).pack()
        self.patients_page = 0
        self.patients_per_page = tk.IntVar(value=10)
        per_page_entry = ttk.Entry(parent, textvariable=self.patients_per_page)
        per_page_entry.pack()
        ttk.Button(parent, text='First Page', command=self.first_page_patients).pack(side=tk.LEFT)
        ttk.Button(parent, text='Prev', command=self.prev_page_patients).pack(side=tk.LEFT)
        ttk.Button(parent, text='Next', command=self.next_page_patients).pack(side=tk.LEFT)
        ttk.Button(parent, text='Last Page', command=self.last_page_patients).pack(side=tk.LEFT)
        self.patient_tree = tree
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
        self.doctors_page = 0
        self.doctors_per_page = tk.IntVar(value=10)
        per_page_entry = ttk.Entry(parent, textvariable=self.doctors_per_page)
        per_page_entry.pack()
        ttk.Button(parent, text='First Page', command=self.first_page_doctors).pack(side=tk.LEFT)
        ttk.Button(parent, text='Prev', command=self.prev_page_doctors).pack(side=tk.LEFT)
        ttk.Button(parent, text='Next', command=self.next_page_doctors).pack(side=tk.LEFT)
        ttk.Button(parent, text='Last Page', command=self.last_page_doctors).pack(side=tk.LEFT)
        self.doctor_tree = tree
        self.load_doctor_data()
        self.doctor_page_label = ttk.Label(parent, text="")
        self.doctor_page_label.pack()
        self.update_page_label_doctors()
        self.record_count_label_doctors = ttk.Label(parent, text="")
        self.record_count_label_doctors.pack()
        self.update_record_count_label_doctors()

    def update_record_count_label_patients(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Patients").fetchone()[0]
        start_index = self.patients_page * self.patients_per_page.get()
        end_index = min((self.patients_page + 1) * self.patients_per_page.get(), total_records)
        record_count_text = f"{end_index - start_index} of {total_records} entities on the page"
        self.record_count_label_patients.config(text=record_count_text)

    def update_record_count_label_doctors(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Doctors").fetchone()[0]
        start_index = self.doctors_page * self.doctors_per_page.get()
        end_index = min((self.doctors_page + 1) * self.doctors_per_page.get(), total_records)
        record_count_text = f"{end_index - start_index} of {total_records} entities on the page"
        self.record_count_label_doctors.config(text=record_count_text)

    def first_page_patients(self):
        self.patients_page = 0
        self.load_patient_data()
        self.update_page_label_patients()
        self.update_record_count_label_patients()

    def last_page_patients(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Patients").fetchone()[0]
        total_pages = (total_records + self.patients_per_page.get() - 1) // self.patients_per_page.get()
        self.patients_page = total_pages - 1
        self.load_patient_data()
        self.update_page_label_patients()
        self.update_record_count_label_patients()

    def first_page_doctors(self):
        self.doctors_page = 0
        self.load_doctor_data()
        self.update_page_label_doctors()
        self.update_record_count_label_doctors()

    def last_page_doctors(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Doctors").fetchone()[0]
        total_pages = (total_records + self.doctors_per_page.get() - 1) // self.doctors_per_page.get()
        self.doctors_page = total_pages - 1
        self.load_doctor_data()
        self.update_page_label_doctors()
        self.update_record_count_label_doctors()

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

    def next_page_patients(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Patients").fetchone()[0]
        total_pages = (total_records + self.patients_per_page.get() - 1) // self.patients_per_page.get()
        if self.patients_page < total_pages - 1:
            self.patients_page += 1
            self.load_patient_data()
            self.update_page_label_patients()
            self.update_record_count_label_patients()  # Добавлено обновление метки
        else:
            messagebox.showinfo("Info", "No more records to display")

    def prev_page_patients(self):
        if self.patients_page > 0:
            self.patients_page -= 1
            self.load_patient_data()
            self.update_page_label_patients()
            self.update_record_count_label_patients()

    def next_page_doctors(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Doctors").fetchone()[0]
        total_pages = (total_records + self.doctors_per_page.get() - 1) // self.doctors_per_page.get()
        if self.doctors_page < total_pages - 1:
            self.doctors_page += 1
            self.load_doctor_data()
            self.update_page_label_doctors()
            self.update_record_count_label_doctors()
        else:
            messagebox.showinfo("Info", "No more records to display")

    def prev_page_doctors(self):
        if self.doctors_page > 0:
            self.doctors_page -= 1
            self.load_doctor_data()
            self.update_page_label_doctors()
            self.update_record_count_label_doctors()

    def update_page_label_patients(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Patients").fetchone()[0]
        total_pages = (total_records + self.patients_per_page.get() - 1) // self.patients_per_page.get()
        self.patient_page_label.config(text=f"Page {self.patients_page + 1} of {total_pages}")

    def update_page_label_doctors(self):
        total_records = self.db.cursor.execute("SELECT COUNT(*) FROM Doctors").fetchone()[0]
        total_pages = (total_records + self.doctors_per_page.get() - 1) // self.doctors_per_page.get()
        self.doctor_page_label.config(text=f"Page {self.doctors_page + 1} of {total_pages}")

    def add_window(self):
        add_window = tk.Toplevel(self)
        add_window.title("Добавить пациента/врача")
        add_window.mainloop()


db = Database('medical.db')
app = Application(db)
app.mainloop()
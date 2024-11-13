import sqlite3
import uuid
from tkinter import messagebox
from controller.DataController import DataController
from model.Doctor import Doctor
from model.Patient import Patient
from controller.SearchController import SearchController

class DbController(DataController):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Doctors (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    specialization TEXT
                )
            """)

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Patients (
                    id TEXT PRIMARY KEY,
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
        patient_id = str(uuid.uuid4())

        cursor = self.get_cursor()
        cursor.execute("""
            INSERT INTO Patients (id, name, address, birth_date, appointment_date, doctor_id, conclusion)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (patient_id, name, address, birth_date, appointment_date, doctor_id, conclusion))
        self.conn.commit()

    def add_doctor(self, name, specialization):
        doctor_id = str(uuid.uuid4())
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Doctors (id, name, specialization)
            VALUES (?, ?, ?)
        """, (doctor_id, name, specialization))
        self.conn.commit()

    def get_patients(self) -> list[Patient]:
        self.cursor.execute('SELECT * FROM Patients')
        tuple_list: list[tuple] = self.cursor.fetchall()
        patients_list: list[Patient] = []
        for i in tuple_list:
            patients_list.append(Patient(*i))
        return patients_list

    def get_doctors(self) -> list[Doctor]:
        self.cursor.execute('SELECT * FROM Doctors')
        tuple_list: list[tuple] = self.cursor.fetchall()
        doctors_list: list[Doctor] = []
        for i in tuple_list:
            doctors_list.append(Doctor(*i))
        return doctors_list

    def get_doctor_by_name(self, name) -> Doctor:
        self.cursor.execute('SELECT * FROM Doctors WHERE name=?', (name,))
        doctor_tuple = self.cursor.fetchone()
        if doctor_tuple:
            return Doctor(*doctor_tuple)
        else:
            return None

    def get_docname(self):
        doctors = self.get_doctors()
        docnames = [doctor['name'] for doctor in
                    doctors]  # Предполагается, что 'name' - это ключ в словаре каждого врача
        return docnames

    def patient_exists(self, name, address, birth_date, app_date, doctor_name, conclusion):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM Patients
            WHERE name = ? AND address = ? AND birth_date = ? AND appointment_date = ? AND doctor_id = ? AND conclusion = ?
        """, (name, address, birth_date, app_date, doctor_name, conclusion))
        count = cursor.fetchone()[0]
        return count > 0

    def doctor_exists(self, name, specialization):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM Doctors
            WHERE name = ? AND specialization = ? """, (name, specialization))
        count = cursor.fetchone()[0]
        return count > 0

    def search_records(self, surname, address, dob, doctor_or_last_visit, search_by_surname, search_by_address,
                       search_by_dob, search_by_doctor_or_last_visit):
        if not (search_by_surname or search_by_address or search_by_dob or search_by_doctor_or_last_visit):
            messagebox.showwarning("Notice!", "Choose the search criteria.")
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

    def search_patients(self, search: SearchController) -> list[Patient]:
        query = 'SELECT * FROM Patients WHERE'
        params = []
        if search.name:
            query += ' name LIKE ? AND'
            params.append('%' + search.name + '%')
        if search.address:
            query += ' address = ? AND'
            params.append(search.address)
        if search.birthdate:
            query += ' birth_date = ? AND'
            params.append(search.birthdate)
        if search.docname:
            query += ' doctor_id LIKE ? AND'
            params.append('%' + search.docname + '%')
        if search.appdate:
            query += ' appointment_date = ? AND'
            params.append(search.appdate)
        query = query.rstrip(' AND')  # remove the last ' AND'
        self.cursor.execute(query, params)
        search_list: list[tuple] = self.cursor.fetchall()
        search_patient_list: list[Patient] = []
        for i in search_list:
            search_patient_list.append(Patient(*i))
        return search_patient_list

    def delete_patients(self, search: SearchController) -> int:
        # First, find the patients that match the search criteria
        search_results = self.search_patients(search)
        num_of_matched_patients = len(search_results)

        # Then, delete those patients
        query = 'DELETE FROM Patients WHERE'
        params = []
        if search.name:
            query += ' name = ? AND'
            params.append(search.name)
        if search.address:
            query += ' address = ? AND'
            params.append(search.address)
        if search.birthdate:
            query += ' birth_date = ? AND'
            params.append(search.birthdate)
        if search.docname:
            query += ' doctor_id = ? AND'
            params.append(search.docname)
        if search.appdate:
            query += ' appointment_date = ? AND'
            params.append(search.appdate)
        query = query.rstrip(' AND')  # remove the last ' AND'
        self.cursor.execute(query, params)
        self.conn.commit()

        # Finally, return the number of deleted patients
        return num_of_matched_patients

    def get_doctor_name_by_id(self, doctor_id):
        doctor_name = self.cursor.execute('SELECT name FROM Doctors WHERE id = ?', (doctor_id,)).fetchone()
        return doctor_name[0] if doctor_name else None

    def get_doctor_id_by_name(self, doctor_name):
        query = "SELECT id FROM Doctors WHERE name = ?"

        result = self.cursor.execute(query, (doctor_name,)).fetchone()
        return result[0] if result else None

    def count_patients_amount(self) -> int:
        self.cursor.execute('SELECT COUNT(*) FROM Patients')
        return int(self.cursor.fetchone()[0])

    def count_doctors_amount(self)->int:
        self.cursor.execute('SELECT COUNT(*) FROM Doctors')
        return int(self.cursor.fetchone()[0])






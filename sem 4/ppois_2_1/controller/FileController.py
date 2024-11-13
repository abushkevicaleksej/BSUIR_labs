
import xml.sax
from controller.SearchController import SearchController
from model.Patient import Patient
from model.Doctor import Doctor
from controller.sax_handlers.ByCriteria import PatientByCriteriaHandler

import logging
import datetime
from controller.sax_handlers.AnyHandler import DoctorAnyHandler
from controller.sax_handlers.AnyHandler import PatientAnyHandler
from xml.dom.minidom import *
import xml.sax
import uuid
from controller.DataController import DataController


import os
import xml.etree.ElementTree as ET

class FileController(DataController):
    def __init__(self, path: str):
        self.path = path
        if os.path.getsize(self.path) == 0:
            self.__creation()

    def __creation(self):
        doc: Document = getDOMImplementation().createDocument(None, 'root', None)
        patients = doc.createElement('patients')
        doc.documentElement.appendChild(patients)
        doctors = doc.createElement('doctors')
        doc.documentElement.appendChild(doctors)
        self._save_doc(doc)

    def _parse_doc(self) -> Document:
        doc = parse(self.path)
        return doc

    def _save_doc(self, doc):
        with open(self.path, 'w') as file:
            file.write(doc.toxml())

    def delete_patients(self,search: SearchController) -> int:
        doc: Document = parse(self.path)
        deleted_count: int = 0
        patients = doc.getElementsByTagName('patient')
        for i in patients:
            match search.criteria:
                case 'name':
                    if search.name == i.getAttribute('name'):
                        self.delete_patient(i.getAttribute('id'))
                        deleted_count += 1
                case 'address':
                    if search.address == i.getAttribute('address'):
                        self.delete_patient(i.getAttribute('id'))
                        deleted_count += 1
                case 'birthdate':
                    if search.birthdate == i.getAttribute('birthdate'):
                        self.delete_patient(i.getAttribute('id'))
                        deleted_count += 1
                case 'appdate':
                    if search.appdate == i.getAttribute('appdate'):
                        self.delete_patient(i.getAttribute('id'))
                        deleted_count += 1
                case 'docname':
                    if search.docname == i.getAttribute('docname'):
                        self.delete_patient(i.getAttribute('id'))
                        deleted_count += 1
        return deleted_count

    def delete_patient(self, id:str):
        doc: Document = parse(self.path)
        patients = doc.getElementsByTagName('patient')
        for i in patients:
            if i.getAttribute('id') == id:
                parent = i.parentNode
                parent.removeChild(i)
                break
        self._save_doc(doc)

    def search_patients(self, search: SearchController) -> list[Patient]:
        handler = PatientByCriteriaHandler(search)
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(self.path)
        dict_patients: list[dict] = handler.result
        patients: list[Patient] = []
        for dict_patient in dict_patients:
            patients.append(Patient(uuid.UUID(dict_patient['id']), dict_patient['name'],
                                    dict_patient['address'], dict_patient['birthdate'],
                                    dict_patient['appdate'], dict_patient['docname'], dict_patient['concl']))
        return patients

    def get_patients(self, search_criteria: SearchController | None = None) -> list[Patient]:
        if search_criteria is None:
            handler = PatientAnyHandler()
        else:
            handler = PatientByCriteriaHandler(search_criteria)
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(self.path)
        dict_patients: list[dict] = handler.result
        patients: list[Patient] = []

        for dict_patient in dict_patients:
            if 'id' in dict_patient and dict_patient['id']:
                id = uuid.UUID(hex=dict_patient['id'])
                patients.append(Patient(id, dict_patient['name'], dict_patient['address'],
                                        dict_patient['birthdate'], dict_patient['appdate'], dict_patient['docname'],
                                        dict_patient['concl']))
            else:
                logging.error(f"Patient dictionary is missing 'id' or 'id' is empty: {dict_patient}")

        return patients

    def patient_exists(self, name, address, birth_date, app_date, doctor_name, conclusion) -> bool:
        patients = self.get_patients()

        for patient in patients:
            if (patient.get_name() == name and patient.get_address() == address and patient.get_birthdate() == birth_date and
                    patient.get_appdate() == app_date and patient.get_docname() == doctor_name and patient.get_concl() == conclusion):
                return True
        return False

    def doctor_exists(self, name, specialization) -> bool:
        doctors = self.get_doctors()

        for doctor in doctors:
            if (doctor.get_docname() == name and doctor.get_specialization() == specialization):
                return True
        return False

    def add_patient(self, name: str, address: str, birthdate: datetime, appdate: datetime, doctor_name: str, concl: str):
        doc = self._parse_doc()

        patient_element = doc.createElement('patient')
        patient_element.attributes['id'] = uuid.uuid4().__str__()
        patient_element.attributes['name'] = str(name)
        patient_element.attributes['address'] = str(address)
        patient_element.attributes['birthdate'] = str(birthdate)
        patient_element.attributes['appdate'] = str(appdate)
        patient_element.attributes['docname'] = str(doctor_name)
        patient_element.attributes['concl'] = str(concl)

        items_element = doc.getElementsByTagName('patients')[0]
        items_element.appendChild(patient_element)

        self._save_doc(doc)

    def add_doctor(self, docname: str, specialization: str) -> None:
        doc = self._parse_doc()

        doc_element = doc.createElement('doctor')
        doc_element.attributes['id'] = uuid.uuid4().__str__()
        doc_element.attributes['doctorname'] = str(docname)
        doc_element.attributes['specialization'] = str(specialization)

        items_element = doc.getElementsByTagName('doctors')[0]
        items_element.appendChild(doc_element)

        self._save_doc(doc)

    def delete_doc(self, id:uuid.UUID) -> None:
        self._delete_by_id('group',id)

    def get_doctors(self) -> list[Doctor]:
        handler = DoctorAnyHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(self.path)
        dict_doctors: list[dict] = handler.result
        doctors: list[Doctor] = []

        for dict_doctor in dict_doctors:
            if 'id' in dict_doctor and dict_doctor['id']:
                id = uuid.UUID(hex=dict_doctor['id'])
                doctors.append(Doctor(id, dict_doctor['doctorname'], dict_doctor['specialization']))
            else:
                logging.error(f"Doctor dictionary is missing 'id' or 'id' is empty: {dict_doctor}")

        return doctors

    def get_doctor_by_name(self, name) -> Doctor:
        handler = DoctorAnyHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(self.path)
        dict_doctors: list[dict] = handler.result

        for dict_doctor in dict_doctors:
            if 'doctorname' in dict_doctor and dict_doctor['doctorname'] == name:
                id = uuid.UUID(hex=dict_doctor['id'])
                return Doctor(id, dict_doctor['doctorname'], dict_doctor['specialization'])
        return None

    def _delete_by_id(self, tag_name: str, id: uuid.UUID) -> None:
        doc = self._parse_doc()
        items = doc.getElementsByTagName(tag_name)
        for item in items:
            if item.getAttribute('id') == id.__str__():
                parent = item.parentNode
                parent.removeChild(item)
                self._save_doc(doc)
                return

    def count_patients_amount(self) -> int:
        patients = self.get_patients()
        return len(patients)

    def count_doctors_amount(self)->int:
        doctors = self.get_doctors()
        return len(doctors)


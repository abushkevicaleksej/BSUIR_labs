import uuid
import xml.sax
from controller.SearchController import SearchController


class PatientByCriteriaHandler(xml.sax.ContentHandler):
    def __init__(self, search: SearchController):
        self.result = []
        self.current_patient = {}
        self.current_tag = None
        self.search: SearchController = search

    def startElement(self, name, attrs):
        if name == 'patient':
            patient_id = attrs.get('id', str(uuid.uuid4()))
            self.current_patient = {
                'id': patient_id,
                'name': attrs.get('name'),
                'address': attrs.get('address'),
                'birthdate': attrs.get('birthdate'),
                'appdate': attrs.get('appdate'),
                'docname': attrs.get('docname'),
                'concl': attrs.get('concl'),
            }
        else:
            self.current_tag = name

    def characters(self, content):
        pass

    def endElement(self, name):
        if name == 'patient':  # We only check the criteria when we finish processing a patient
            match self.search.criteria:
                case 'name':
                    if self.search.name and self.current_patient['name'] and self.search.name in self.current_patient[
                        'name']:
                        self.result.append(self.current_patient)
                        return
                case 'address':
                    if self.search.address == self.current_patient['address']:
                        self.result.append(self.current_patient)
                        return
                case 'appdate':
                    if self.search.appdate == self.current_patient['appdate']:
                        self.result.append(self.current_patient)
                        return
                case 'docname':
                    if self.search.docname and self.current_patient['docname'] and self.search.docname in \
                            self.current_patient['docname']:
                        self.result.append(self.current_patient)
                        return

                case 'birthdate':
                    if self.search.birthdate == self.current_patient['birthdate']:
                        self.result.append(self.current_patient)
                        return


class DoctorByCriteriaHandler(xml.sax.ContentHandler):
    def __init__(self, search: SearchController):
        self.result = []
        self.current_doctor = {}
        self.current_tag = None
        self.search: SearchController = search

    def startElement(self, name, attrs):
        if name == 'doctor':
            patient_id = attrs.get('id', str(uuid.uuid4()))
            self.current_doctor = {
                'id': patient_id,
                'doctorname': attrs.get('doctorname'),
                'specializatiob': attrs.get('specialization'),
            }
        else:
            self.current_tag = name

    def characters(self, content):
        pass

    def endElement(self, name):
        if name == 'doctor':  # We only check the criteria when we finish processing a patient
            match self.search.criteria:
                case 'doctorname':
                    if self.search.name == self.current_doctor['doctorname']:
                        self.result.append(self.current_doctor)
                        return
                case 'specialization':
                    if self.search.address == self.current_doctor['specialization']:
                        self.result.append(self.current_doctor)
                        return





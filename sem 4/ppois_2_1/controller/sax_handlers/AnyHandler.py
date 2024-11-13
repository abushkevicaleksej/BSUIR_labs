import uuid
import xml.sax


class PatientAnyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.result = []
        self.current_patient = {}
        self.current_tag = None

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
        if self.current_tag is not None and self.current_patient is not None:
            self.current_patient[self.current_tag] = content

    def endElement(self, name):
        if name == 'patient' and self.current_patient is not None:
            self.result.append(self.current_patient)
            self.current_patient = None
        self.current_tag = None

class DoctorAnyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.result = []  # List to store results
        self.current_doctor = {}
        self.current_tag = None
        self.inside_doctors = False  # Flag to indicate if inside <doctors> tag

    def startElement(self, name, attrs):
        if name == 'doctors':
            self.inside_doctors = True
        elif name == 'doctor' and self.inside_doctors:
            doctor_id = attrs.get('id', str(uuid.uuid4()))  # Generate UUID if 'id' is not provided  # Debugging line
            self.current_doctor = {
                'id': doctor_id,
                'doctorname': attrs.get('doctorname'),
                'specialization': attrs.get('specialization')
            }
        else:
            self.current_tag = name

    def characters(self, content):
        if self.current_tag is not None and self.current_doctor:
            self.current_doctor[self.current_tag] = content

    def endElement(self, name):
        if name == 'doctor' and self.inside_doctors:
            # Check if 'id' is missing or empty, generate UUID in that case
            if 'id' not in self.current_doctor or not self.current_doctor['id']:
                self.current_doctor['id'] = str(uuid.uuid4()) # Debugging line
            self.result.append(self.current_doctor)
            self.current_doctor = {}
        elif name == 'doctors':
            self.inside_doctors = False
        self.current_tag = None
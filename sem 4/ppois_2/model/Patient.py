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
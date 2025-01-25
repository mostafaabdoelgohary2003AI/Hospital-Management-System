class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.appointments = []
        self.bills = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def add_bill(self, bill):
        self.bills.append(bill)

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from billing import Bill


class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.bills = {}
        self.patient_id_counter = 1
        self.doctor_id_counter = 1
        self.appointment_id_counter = 1
        self.bill_id_counter = 1

    def add_patient(self, name, age, gender):
        patient = Patient(self.patient_id_counter, name, age, gender)
        self.patients[self.patient_id_counter] = patient
        self.patient_id_counter += 1
        print(f"Patient added successfully. Patient ID: {patient.patient_id}")

    def add_doctor(self, name, specialization):
        doctor = Doctor(self.doctor_id_counter, name, specialization)
        self.doctors[self.doctor_id_counter] = doctor
        self.doctor_id_counter += 1
        print(f"Doctor added successfully. Doctor ID: {doctor.doctor_id}")

    def schedule_appointment(self, patient_id, doctor_id, date, time):
        if patient_id not in self.patients or doctor_id not in self.doctors:
            print("Invalid patient or doctor ID.")
            return

        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]
        appointment = Appointment(self.appointment_id_counter, patient, doctor, date, time)

        self.appointments[self.appointment_id_counter] = appointment
        patient.add_appointment(appointment)
        doctor.add_appointment(appointment)

        self.appointment_id_counter += 1
        print(f"Appointment scheduled successfully. Appointment ID: {appointment.appointment_id}")

    def generate_bill(self, patient_id, amount):
        if patient_id not in self.patients:
            print("Invalid patient ID.")
            return

        patient = self.patients[patient_id]
        bill = Bill(self.bill_id_counter, patient, amount)

        self.bills[self.bill_id_counter] = bill
        patient.add_bill(bill)

        self.bill_id_counter += 1
        print(f"Bill generated successfully. Bill ID: {bill.bill_id}")

    def view_all_patients(self):
        for patient in self.patients.values():
            print(patient)

    def view_all_doctors(self):
        for doctor in self.doctors.values():
            print(doctor)

    def view_all_appointments(self):
        for appointment in self.appointments.values():
            print(appointment)
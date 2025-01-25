from datetime import datetime

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, DateTime: {self.datetime}"
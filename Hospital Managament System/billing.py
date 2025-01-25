from datetime import datetime

class Bill:
    def __init__(self, bill_id, patient, amount):
        self.bill_id = bill_id
        self.patient = patient
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f"Bill ID: {self.bill_id}, Patient: {self.patient.name}, Amount: ${self.amount:.2f}, Date: {self.date}"
import random

from patient import Patient


class Doctor(Patient):
    def __init__(self, name, date_of_birth, address, phone_number, specialization="N/A"):
        super().__init__(name, date_of_birth, address, phone_number)
        self.doctor_id = self.patient_id
        self.specialization = self.check_specialization(specialization)

    @staticmethod
    def check_specialization(specialization):
        list_of_specs = [
            "SURGEON", "MIDWIVES", "GENERAL", "CHEMOTHERAPIST",
            "DENTIST", "PSYCHOTHERAPIST", "OPTICIANS",
            "PHYSIOTHERAPIST", "ONCOLOGIST"
        ]
        specialization = specialization.upper()
        if specialization in list_of_specs:
            return specialization
        raise ValueError("Specialization not available.")

    def generate_id(self):
        initial_string = "DOC"
        random_number = random.randint(10000, 99999)
        return initial_string + str(random_number)

    def get_id(self):
        return self.doctor_id

    def __str__(self):
        return f"Doctor[ID={self.doctor_id}, Name={self.name}, Specialization={self.specialization}]"

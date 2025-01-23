from patient import Patient


class PatientPortal:
    def __init__(self):
        self.patient_list = []

    def register_patient(self, name, date_of_birth, address, phone_number):
        for patient in self.patient_list:
            if patient.phone_number == phone_number:
                raise ValueError("A patient with this phone number is already registered.")
        new_patient = Patient(name, date_of_birth, address, phone_number)
        self.patient_list.append(new_patient)
        return new_patient

    def find_patient(self, patient_id):
        for patient in self.patient_list:
            if patient.get_id() == patient_id:
                return patient
        raise ValueError(f"No patient found with ID {patient_id}.")


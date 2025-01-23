from doctor import Doctor


class DoctorPortal:
    def __init__(self):
        self.doctor_list = []

    def register_doctor(self, name, date_of_birth, address, phone_number, specialization):
        for doctor in self.doctor_list:
            if doctor.phone_number == phone_number:
                raise ValueError("A doctor with this phone number is already registered.")
        new_doctor = Doctor(name, date_of_birth, address, phone_number, specialization)
        self.doctor_list.append(new_doctor)
        return new_doctor

    def find_doctor(self, doctor_id):
        for doctor in self.doctor_list:
            if doctor.get_id() == doctor_id:
                return doctor
        raise ValueError(f"No doctor found with ID {doctor_id}.")
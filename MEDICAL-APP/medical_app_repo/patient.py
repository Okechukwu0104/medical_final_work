from datetime import datetime
import random

appointment_list = []


class Patient:
    def __init__(self, name, date_of_birth, address, phone_number="N/A"):
        self.name = self.verify_name(name)
        self.date_of_birth = self.verify_date(date_of_birth)
        self.address = address
        self.phone_number = self.validate_phone_number(phone_number)
        self.patient_id = self.generate_id()

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) == 11 and phone_number.isdigit():
            return phone_number
        raise ValueError("Phone number must be 11 digits and contain only numbers.")


    @staticmethod
    def verify_name(name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        return name.strip()

    def generate_id(self):
        initial_string = "PAT"
        random_number = random.randint(10000, 99999)
        return initial_string + str(random_number)

    def get_id(self):
        return self.patient_id

    def __str__(self):
        return f"Patient[ID={self.patient_id}, Name={self.name}, Phone={self.phone_number}]"

    def book_appointment(self, appointment_date, appointment_time, doctor_name, reason_for_appointment):
        from appointment import Appointment
        for appointment in appointment_list:
            if (
                appointment.appointment_date == appointment_date
                and appointment.appointment_time == appointment_time
                and appointment.doctor_name == doctor_name
            ):
                raise ValueError("This appointment slot is already booked.")
        appointment = Appointment(appointment_date, appointment_time, doctor_name, reason_for_appointment)
        appointment.is_booking = True
        appointment_list.append(appointment)
        return appointment

    def delete_appointment(self, appointment_index):
        if not appointment_list:
            print("No appointments to delete.")
            return

        if 0 <= appointment_index < len(appointment_list):
            deleted_appointment = appointment_list.pop(appointment_index)
            print(f"Deleted Appointment:\n{deleted_appointment}")
        else:
            raise IndexError("Invalid appointment index. Please provide a valid index.")


    @staticmethod
    def verify_date(date_of_birth):
        if any(char.isalpha() for char in date_of_birth):
            raise ValueError("Date of birth should not contain letters. Use the format YYYY-MM-DD.")
        try:
            datetime.strptime(date_of_birth, "%Y-%m-%d")
            return date_of_birth
        except ValueError:
            raise ValueError("Date of birth must be in the format YYYY-MM-DD.")

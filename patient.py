import random
from appointment import Appointment
appointment_list =[]

class Patient:
    def __init__(self, name, date_of_birth, address, phone_number="N/A"):
        self.phone_number = self.validate_phone_number(phone_number)
        self.name = self.verify_name(name)
        self.date_of_birth = date_of_birth
        self.address = address
        self.generate_id()
        self.patient_id = ""

    def validate_phone_number(self, phone_number):
        if len(phone_number) == 11 and phone_number.isdigit():
            self.phone_number = phone_number
        else:
            raise ValueError("Phone number must be 11 digits and contain only numbers.")

    def verify_name(self, name):
        if not name:
            raise ValueError("First name and last name cannot be empty.")
        self.name = name

    def generate_id(self):
        initial_string = "PAT"
        random_number = random.randint(10000, 99999)
        self.patient_id = initial_string + str(random_number)

    def get_id(self):
        return self.patient_id

    def book_appointment(self,appointment_date, appointment_time, doctor_name):
        book_appointment = Appointment(appointment_date, appointment_time, doctor_name)
        book_appointment.is_booking = True
        appointment_list.append(book_appointment)
        return book_appointment

    def view_appointment(self):
        for appointment in appointment_list:
            print(appointment)

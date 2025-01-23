class Appointment:
    def __init__(self, appointment_date, appointment_time, doctor_name):
        self.is_booking = False
        if not self.is_booking:
            self.appointment_date = appointment_date
            self.appointment_time = appointment_time
            self.doctor_name = doctor_name
        raise ValueError("User has already booked appointment")

    def find_doctor_by_name(self):
        from doctor_portal import doctor_portal
        doctor_portal = doctor_portal()
        the_list = doctor_portal.__init__().doctor_list
        print(the_list)
        # for doctor in the_list:
        #     if doctor.name == name:

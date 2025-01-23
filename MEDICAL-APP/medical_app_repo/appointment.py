class Appointment:
    def __init__(self, appointment_date, appointment_time, doctor_name,reason_for_appointment):
        self.is_booking = False
        if not self.is_booking:
            self.appointment_date = appointment_date
            self.appointment_time = appointment_time
            self.doctor_name = doctor_name
            self.reason_for_appointment = reason_for_appointment
        else:
            raise ValueError("User has already booked appointment")

    def find_doctor_by_name(self,name):
        from doctor_portal import DoctorPortal
        doctor_portal = DoctorPortal()
        the_list = doctor_portal.__init__().doctor_list
        for doctor in the_list:
            if doctor.name == name:
                return name
            raise ValueError("Doctor doesn't exist")
    def __str__(self):
        return f"""
        
        Doctor Name:{self.doctor_name}  
        Appointment Date:{self.appointment_date}
        Appointment Time:{self.appointment_time}
        Appointment Reason:{self.reason_for_appointment}
        """

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from appointment import Appointment
        from patient_portal import patient_portal
        from doctor_portal import doctor_portal

        patient_portal = patient_portal()
        doctor_portal = doctor_portal()
        registered_patient = patient_portal.register_patient("name", "29/10/23", "address", "0803321563")
        registered_doctor = doctor_portal.register_doctor("other name", "29/13/23","address", "0803321563","OPTICIAN")
        appointment = Appointment("33/10/30","5pm","other name")
        print(appointment.find_doctor_by_name())

        self.assertEqual(True, False)



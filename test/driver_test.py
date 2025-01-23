import unittest
from patient_portal import PatientPortal
from doctor_portal import DoctorPortal

class TestPortal(unittest.TestCase):
    def setUp(self):
        self.patient_portal = PatientPortal()
        self.doctor_portal = DoctorPortal()

    def test_register_and_find_patient(self):
        patient = self.patient_portal.register_patient("John Doe", "1990-01-01", "123 Elm Street", "08123456789")
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(patient.phone_number, "08123456789")
        found_patient = self.patient_portal.find_patient(patient.patient_id)
        self.assertEqual(found_patient, patient)

    def test_duplicate_patient(self):
        self.patient_portal.register_patient("John Doe", "1990-01-01", "123 Elm Street", "08123456789")
        with self.assertRaises(ValueError):
            self.patient_portal.register_patient("John Doe", "1990-01-01", "123 Elm Street", "08123456789")

    def test_register_and_find_doctor(self):
        doctor = self.doctor_portal.register_doctor("Jane Smith", "1980-05-05", "456 Pine Street", "08123456789", "SURGEON")
        self.assertEqual(doctor.name, "Jane Smith")
        self.assertEqual(doctor.specialization, "SURGEON")
        found_doctor = self.doctor_portal.find_doctor(doctor.patient_id)
        self.assertEqual(found_doctor, doctor)

    def test_duplicate_doctor(self):
        self.doctor_portal.register_doctor("Jane Smith", "1980-05-05", "456 Pine Street", "08123456789", "SURGEON")
        with self.assertRaises(ValueError):
            self.doctor_portal.register_doctor("Jane Smith", "1980-05-05", "456 Pine Street", "08123456789", "SURGEON")

    def test_invalid_specialization(self):
        with self.assertRaises(ValueError):
            self.doctor_portal.register_doctor("Jane Smith", "1980-05-05", "456 Pine Street", "08123456789", "CARDIOLOGIST")


if __name__ == "__main__":
    unittest.main()

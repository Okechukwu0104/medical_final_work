from patient import appointment_list


def main():
    from patient_portal import PatientPortal
    from doctor_portal import DoctorPortal

    patient_portal_instance = PatientPortal()
    doctor_portal_instance = DoctorPortal()

    while True:
        print("\n--- Medical App Main Menu ---")
        print("1. Register Patient")
        print("2. Register Doctor")
        print("3. Book Appointment")
        print("4. View All Appointments")
        print("5. Delete Appointment")
        print("6. Exit")


        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\n--- Register a New Patient ---")
            name = input("Enter patient name: ")
            dob = input("Enter patient date of birth (YYYY-MM-DD): ")
            address = input("Enter patient address: ")
            phone = input("Enter patient phone number (11 digits): ")

            try:
                patient = patient_portal_instance.register_patient(name, dob, address, phone)
                print(f"Doctor {name} successfully registered with ID: {patient.get_id()}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            print("\n--- Register a Doctor ---")
            name = input("Enter doctor's name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            specialization = input("Enter specialization (e.g., Surgeon, Dentist): ")

            try:
                doctor = doctor_portal_instance.register_doctor(name, date_of_birth, address, phone_number,
                                                                specialization)
                print(f"Doctor {name} successfully registered with ID: {doctor.get_id()}")
            except ValueError as e:
                print(f"Error: {e}")


        elif choice == "3":
            print("\n--- Book an Appointment ---")
            patient_id = input("Enter patient ID: ")
            try:
                patient = patient_portal_instance.find_patient(patient_id)
            except ValueError as e:
                print(f"Error: {e}")
                continue

            doctor_id = input("Enter doctor ID: ")
            try:
                doctor = doctor_portal_instance.find_doctor(doctor_id)
            except ValueError as e:
                print(f"Error: {e}")
                continue

            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            appointment_time = input("Enter appointment time (HH:MM): ")
            reason = input("Enter reason for appointment: ")

            try:
                appointment = patient.book_appointment(appointment_date, appointment_time, doctor.name, reason)
                print(
                    f"Appointment successfully booked with Doctor {doctor.name} on {appointment_date} at {appointment_time}.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("\n--- View All Appointments ---")
            if len(appointment_list) == 0:
                print("No appointments have been booked yet.")
            else:
                for i, appointment in enumerate(appointment_list, start=1):
                    print(f"{i}. {appointment}")

        elif choice == "5":
            print("\n--- Delete an Appointment ---")
            if not appointment_list:
                print("No appointments to delete.")
            else:
                # Display the list of appointments
                for i, appointment in enumerate(appointment_list, start=1):
                    print(f"{i}. {appointment}")

                try:
                    appointment_index = int(input("Enter the appointment number to delete: ")) - 1

                    if 0 <= appointment_index < len(appointment_list):
                        deleted_appointment = appointment_list.pop(appointment_index)
                        print(f"Deleted Appointment:\n{deleted_appointment}")
                    else:
                        print("Invalid appointment number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")


        elif choice == "6":
            print("Exiting our Medical application. Goodbye!")
            break


        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

from hospital import Hospital


def main():
    hospital = Hospital()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. Generate Bill")
        print("5. View All Patients")
        print("6. View All Doctors")
        print("7. View All Appointments")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            hospital.add_patient(name, age, gender)
        elif choice == '2':
            name = input("Enter doctor name: ")
            specialization = input("Enter doctor specialization: ")
            hospital.add_doctor(name, specialization)
        elif choice == '3':
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            hospital.schedule_appointment(patient_id, doctor_id, date, time)
        elif choice == '4':
            patient_id = int(input("Enter patient ID: "))
            amount = float(input("Enter bill amount: "))
            hospital.generate_bill(patient_id, amount)
        elif choice == '5':
            hospital.view_all_patients()
        elif choice == '6':
            hospital.view_all_doctors()
        elif choice == '7':
            hospital.view_all_appointments()
        elif choice == '8':
            print("Thank you for using the Hospital Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
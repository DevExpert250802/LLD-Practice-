# Hospital Appointment System

print("\nWelcome to the Hospital Appointment System!")

doctors = {
    "Dr. Sharma": "Cardiologist",
    "Dr. Verma": "Neurologist",
    "Dr. Mehta": "Pediatrician",
    "Dr. Rao": "Dermatologist",
    "Dr. Iyer": "Orthopedic"
}

patients = {}  
appointments = {}

def register_patient():
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id in patients:
        print("Patient with ID " + patient_id + " is already registered.")
        return
    name = input("Enter Patient Name: ").strip()
    age = input("Enter Patient Age: ").strip()
    if not age.isdigit():
        print("Invalid age. Please enter a number.")
        return
    patients[patient_id] = {"name": name, "age": age}
    appointments[patient_id] = []
    print("Patient " + name + " (ID: " + patient_id + ", Age: " + age + ") registered successfully.")

def view_doctors():
    print("\nAvailable Doctors:")
    for doc in doctors:
        print(doc + " - " + doctors[doc])

def book_appointment():
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id not in patients:
        print("Patient ID " + patient_id + " not registered. Please register first.")
        return
    
    print("\nAvailable Doctors:")
    for doc in doctors:
        print("- " + doc)

    doctor_name = input("Enter Doctor's Name: ").strip()
    if doctor_name in doctors:
        appointments[patient_id].append(doctor_name)
        print("Appointment confirmed with " + doctor_name + ".")
    else:
        print("Invalid doctor name. Try again.")

def view_appointments():
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id not in patients:
        print("Patient ID " + patient_id + " not found.")
        return
    
    print("\nAppointment History for " + patients[patient_id]["name"] + ":")
    if appointments[patient_id]:
        for doc in appointments[patient_id]:
            print("- " + doc)
    else:
        print("No appointments booked.")

def cancel_appointment():
    patient_id = input("Enter Patient ID: ").strip()
    if patient_id not in patients:
        print("Patient ID " + patient_id + " not found.")
        return

    if not appointments[patient_id]:
        print("No appointments to cancel.")
        return

    print("\nYour Appointments:")
    for idx, doc in enumerate(appointments[patient_id], 1):
        print(str(idx) + ". " + doc)

    try:
        cancel_index = int(input("Enter the appointment number to cancel: ")) - 1
        if 0 <= cancel_index < len(appointments[patient_id]):
            removed_doctor = appointments[patient_id].pop(cancel_index)
            print("Appointment with " + removed_doctor + " canceled.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n1. Register Patient")
    print("2. View Doctors")
    print("3. Book Appointment")
    print("4. View Appointment History")
    print("5. Cancel Appointment")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        register_patient()
    elif choice == "2":
        view_doctors()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        view_appointments()
    elif choice == "5":
        cancel_appointment()
    elif choice == "6":
        print("Thank you for using the Hospital Appointment System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

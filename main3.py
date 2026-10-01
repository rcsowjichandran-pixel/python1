import hospital

h = hospital.Hospital()

# Add doctors
h.add_doctor("Meera Sharma", "Cardiologist", "Mon, Wed, Fri")
h.add_doctor("Rajesh Kumar", "Neurologist", "Tue, Thu, Sat")

# Register patients
h.register_patient("Sowjanya", 25, "Fever")
h.register_patient("Arun", 30, "Headache")

# Book appointments
h.book_appointment("Sowjanya", "Meera Sharma")
h.book_appointment("Arun", "Rajesh Kumar")

# Show doctors and appointments
h.show_doctors()
h.show_appointments()

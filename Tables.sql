CREATE TABLE Appointments (
	patient_id serial PRIMARY KEY,
	patient_name VARCHAR ( 50 ) NOT NULL,
	patient_fathername VARCHAR ( 50 ) NOT NULL,
	patient_place VARCHAR ( 50 ) NOT NULL,
	patient_phonenumber VARCHAR ( 255 ) UNIQUE NOT NULL,
	patient_appointment_date TIMESTAMP NOT NULL,
    patient_appointment_fees INT NOT NULL,
	patient_appointment_doctor VARCHAR ( 50 ) NOT NULL
);
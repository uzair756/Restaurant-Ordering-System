# Appointment Program

## Abstract & Introduction

Managing patient records at clinic receptions can be a daunting task without suitable programs. The Appointment Program is designed to empower receptionists in effortlessly handling patient records, including adding, searching, and displaying tables. The primary objective is efficient patient record management.

## Methodology

The program provides four options:

1. **Add an Appointment:** Allows the receptionist to input patient details (ID, name, age, gender, contact, day, and doctor's specialization). The program matches the doctor's specialization with the doctor's name, calculates the appointment time, and saves details in separate CSV files for patient and appointments. It then displays the appointments table containing patient ID, name, consulting doctor's name, and appointment time.

2. **Search an Appointment:** Enables the receptionist to search for a patient's record by entering the patient's ID. If found, the patient's record is displayed; otherwise, the program prompts to add a new record. The program offers options to continue searching or exit, displaying the number of records searched, found, and added.

3. **Print Patient's Table:** Prints the entire patient's table for easy reference.

4. **Exit:** Ends the program with a goodbye message.

The program includes error handling for invalid inputs, checks for duplicate patient IDs, and utilizes the Pandas library, dictionaries, and CSV files for effective data management.

## Specifications

- **Pandas Library:** Utilized for efficient data handling.
- **Dictionaries and CSV Files:** Used for storing patient and appointment records.
- **Data Redundancy Check:** Avoids duplicate patient IDs for accurate record-keeping.
- **Exception Handling:** Ensures valid inputs by checking for string inputs in place of integers for ID, age, and contact number.

## Usage

To run the program, ensure you have Python installed on your system. Simply download the program files and run `appointment_program.py` using your Python interpreter.

## Acknowledgments

Special thanks to [Your Name] for the contribution to this project.

---

Thank you for reviewing the Appointment Program. Feel free to contribute or provide feedback!

User-Friendly Interface: Functions for each option and clear error messages enhance user experience.
Conclusion
This program efficiently manages patient records, storing them in tables saved in separate CSV files. The user-friendly interface, along with error handling and data redundancy checks, ensures accurate and easy data handling for receptionists.
 
 

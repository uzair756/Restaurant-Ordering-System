# Appointment Program

## Abstract & Introduction

Managing patient records at clinic receptions is a challenging task without suitable programs. This program is designed to facilitate receptionists in effortlessly handling patient records, including adding, searching, and displaying tables. The primary objective is efficient patient record management.

## Methodology

A receptionist controls the input, and the program offers four options:

1. **Add an Appointment:** The receptionist inputs patient details (ID, name, age, gender, contact, day, and doctor's specialization). The program matches the doctor's specialization with the doctor's name, calculates the appointment time, and saves details in separate CSV files for patient and appointments. The appointments table, containing patient ID, name, consulting doctor's name, and appointment time, is then displayed.

2. **Search an Appointment:** The receptionist enters the patient's ID, and the program searches the patient's table. If found, the patient's record is displayed; otherwise, the program prompts to add a new record. The program offers options to continue searching or exit, displaying the number of records searched, found, and added.

3. **Print Patient's Table:** This option prints the entire patient's table for easy reference.

4. **Exit:** Entering '4' ends the program with a goodbye message.

The program includes error handling for invalid inputs, checks for duplicate patient IDs, and utilizes the Pandas library, dictionaries, and CSV files for effective data management.

## Specifications

- **Pandas Library:** Utilized for efficient data handling.
- **Dictionaries and CSV Files:** Used for storing patient and appointment records.
- **Data Redundancy Check:** Avoids duplicate patient IDs for accurate record-keeping.
- **Exception Handling:** Ensures valid inputs by checking for string inputs in place of integers for ID, age, and contact number.
- **User-Friendly Interface:** Functions for each option and clear error messages enhance user experience.

## Conclusion

This program efficiently manages patient records, storing them in tables saved in separate CSV files. The user-friendly interface, along with error handling and data redundancy checks, ensures accurate and easy data handling for receptionists.

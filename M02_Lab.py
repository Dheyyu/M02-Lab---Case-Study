# Author: Oladayo David Ayorinde
# File name: M02_Lab.py
# Description: This app determines if a student qualifies for the Dean's list or Honor Roll based on their GPA.

def main():
    print ("Student Qualification App")

    while True:
        print()
        # Asking for the student's last name
        last_name = input("Enter the student's last name: ")
        print()
        # This quits processing student records if the last name entered is 'ZZZ'
        if last_name == 'ZZZ':
            break

        # Asking for the student's first name
        first_name = input("Enter the student's first name: ")
        print()
        
        # Asking for the student's GPA
        gpa = float(input("Enter the student's GPA: "))
        print()

        # Using if...else conditions to check if the student qualifies for the Dean's List or the Honor Roll
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's list!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} does not qualify for any honors.")

    print("Student record processing has ended.")


# This runs the main function
if __name__ == "__main__":
    main()
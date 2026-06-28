def student_database():
    students = {}  

    while True:
        print("\n----- STUDENT DATABASE MENU -----")
        print("1. Add Student")
        print("2. Search Student by Roll No")
        print("3. Display All Students")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number (1-4).")
            continue

        # 1. Add student
        if choice == 1:
            try:
                roll_no = input("Enter roll number: ")

                name = input("Enter name: ")
                age = int(input("Enter age: "))
                city = input("Enter city: ")

                students[roll_no] = {
                    "name": name,
                    "age": age,
                    "city": city
                }

                print("Student added successfully!")

            except ValueError:
                print("Invalid age! Please enter a number.")

        # 2. Search student
        elif choice == 2:
            roll_no = input("Enter roll number to search: ")

            student = students.get(roll_no)

            if student:
                print("\nStudent Found:")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("City:", student["city"])
            else:
                print("Student not found!")

        # 3. Display all students
        elif choice == 3:
            if not students:
                print("No records available!")
            else:
                print("\n--- All Students ---")
                for roll, data in students.items():
                    print("Roll No:", roll)
                    print("Name:", data["name"])
                    print("Age:", data["age"])
                    print("City:", data["city"])
                    print("-------------------")

        # 4. Exit
        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select 1-4.")


# Call the function
student_database()
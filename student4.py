class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []   

   
    def add_mark(self, mark):
        try:
            mark = float(mark)
            if mark < 0 or mark > 100:
                print("Mark should be between 0 and 100")
            else:
                self.marks_list.append(mark)
        except ValueError:
            print("Invalid input! Please enter a number.")

    
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

   
    def display_info(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())



name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

s1 = Student(name, roll_no)


for i in range(5):
    mark = input(f"Enter mark {i+1}: ")
    s1.add_mark(mark)


s1.display_info()
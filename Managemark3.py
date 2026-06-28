def manage_marks():
    marks = []

    print("Enter marks of 5 subjects:")

    for i in range(5):
        try:
            mark = float(input(f"Enter mark {i+1}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid input! Please enter a number.")
            return  
        
    
    avg = sum(marks) / len(marks)
    print("\nAverage marks:", avg)

    
    print("Highest marks:", max(marks))
    print("Lowest marks:", min(marks))

    
    marks.sort(reverse=True)
    print("Marks in descending order:", marks)



manage_marks()
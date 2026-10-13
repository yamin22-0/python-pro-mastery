#TODO: Intialise the dictionary grades = {}
#TODO: Clean name using .strip.lower
#TODO: Validate if name is empty,if its only words an if already exists.
#TODO: Validate for marks if it's numbers,if student exists in grades, and if it's a whole number btwn (0-100).
#TODO: Calculate average
#TODO: Find student with highets marks.
#TODO: print(name,marks average and highest student).

grades = {}

def add_student(grades,name):

    name = name.strip().lower()

    if not name:
        return "Please enter student name!"
    
    elif name in grades:
        return "Student already exists!"
    
    elif not name.replace(" ","").isalpha():
        return "Name can only contain letters or words."
    
    grades[name] = []

    return f"Student {name.title()} added successfully!"

def add_mark(grades,name,mark):

    name = name.strip().lower()

    if name not in grades:
        return f"Student doesn't exist, add student first."

    try:
        mark = int(mark)
    except ValueError:
        return "Marks can only be whole numbers."
    
    if mark < 0 or mark > 100:
        return f"Try a number between (0-100)."
    

    grades[name].append(mark)

    return f"Mark {mark} added for {name.title()}"

def get_average(grades,name):

   name = name.strip().lower()

   if name not in grades:
       return None

   marks = grades[name]

   if not marks:
       return None

   average = sum(marks) / len(marks)

   return average

def best_student(grades):

    best_name = None
    best_avg = None

    for name,avg in grades.items():
        avg = get_average(grades,name)

        if avg is None:
            continue

        if best_avg is None or avg > best_avg:
            best_avg = avg
            best_name = name

    return best_name

while True:

    print("\n#-- Student grade book --#")
    print("1. Add student: ")
    print("2. Add Mark: ")
    print("3. Show average: ")
    print("4.Best student: ")
    print("5.Quit: ")

    choice = input("Choose an option (1-5): ")

    if choice == "1":

        name = input("Add student name: ").strip()
        student = add_student(grades,name)
        print(student)

    elif choice == "2":

        name = input("Enter student name: ")
        mark = input("Enter student marks: ")
        student = add_mark(grades,name,mark)
        print(student)

    elif choice == "3":

        name = input("Enter student name: ").strip()
        average = get_average(grades,name)

        if average is None:
            print("No average yet: the student either has no marks or not added yet.")
        else:
            print(f"Average: {average:.2f}")

    elif choice == "4":

        top_student = best_student(grades)

        if top_student is None:
            print("No student with marks yet!")
        else:
            print(f"The Best student is {top_student.title()}")

    elif choice == "5":

        print("Goodbye")
        break

    else:
        print("Enter a valid option!(1-5)")
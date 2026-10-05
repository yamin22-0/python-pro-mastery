#TODO: Intialise marks_list=[]
#TODO: Ask user to enter marks of 5 students. while len(marks) < 5.
#TODO: Validate if the user tries to send an empty input.
#TODO: Validate if user tries to enter a number below 0 or above 100.
#TODO: Validate if the user tries to enter words or letter.
#TODO: Print the student student marks_list=[].
#TODO: Calculate total_marks. total_marks = sum(marks)
#TODO: Calculate average. average = sum(marks) / len(marks).
#TODO: Print average.
#TODO: Print the highest and lowest student.


def marks_system():

    marks_list = []

    while len(marks_list) < 5:
        try:
            marks = int(input("Enter marks: "))
        
            if marks < 0 or marks > 100:
                print("Enter marks within range: ")
                continue

        except ValueError:
            print("Enter valid marks: ")
            continue
        
        marks_list.append(marks)

        
    print(marks_list)

    total_marks = sum(marks_list)
    average = total_marks / len(marks_list)
    highest_marks = max(marks_list)
    lowest_mark = min(marks_list)

    pass_count = 0

    for marks in marks_list:
        if marks >= 50:
            pass_count += 1

    print(f"Total Marks : {total_marks}")
    print(f"Average: {round(average,2)}")
    print(f"Highest Marks: {highest_marks} ")
    print(f"Lowest Marks: {lowest_mark}")
    print(f"Students who passed: {pass_count}")

marks_system()



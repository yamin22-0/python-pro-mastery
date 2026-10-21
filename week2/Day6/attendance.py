#TODO: PART A
#TODO: Validate for add_student if no name is entered or if trying to add a duplicate student.


def add_student(attendance,name):

    name = name.strip().lower()

    if not name:
        return False, "Please enter name."
    elif name in attendance:
        return False, "Student already exists."
    else:
        attendance[name] = set()
        return True, "student attendance tracked successfully."



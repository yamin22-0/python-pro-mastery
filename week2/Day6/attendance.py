#TODO: PART A
#TODO: Validate for add_student if no name is entered or if trying to add a duplicate student.
#TODO: Validate for mark_present if no date is entered or if tring to add date for student that don't exist.
#TODO: Validate for days_present if no name is entered or if tring to check days present for student that don't exist.


def add_student(attendance,name):

    name = name.strip().lower()

    if not name:
        return False, "Please enter name."
    elif name in attendance:
        return False, "Student already exists."
    else:
        attendance[name] = set()
        return True, "student attendance tracked successfully."

def mark_present(attendance,name,date):

    name = name.strip().lower()
    date = date.strip()

    if not date:
        return False, "Please enter date."
    elif name not in attendance:
        return False, "Confirm if student exists."
    else:
        attendance[name].add(date)
        return True, "Student attendance name and date tracked successfully."

def days_present(attendance,name):

    name = name.strip().lower()

    if name not in attendance:
        return None
    else:
        return len(attendance[name])
        
def best_student(attendance):

    best_name = None
    attended_days = 0

    for name, attended in attendance.items():
        if len(attended) > attended_days:
            attended_days = len(attended)
            best_name = name

    return best_name

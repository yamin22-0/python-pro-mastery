## Student attendance system ##

## What the system does ##

Records the number of students present,count days present for each student and find out who attended the most.

## Data model ##

-Attendance has name and date.
-Name(key) is cleaned using `.strip()` and `.lower()`.

**Example**

attendance = {

    "amina": {"2026-10-01", "2026-10-02"},
    "brian": {"2026-10-01"},
}

## add_student(attendance,name) what it takes,returns and what could go wrong. ## 

**add_student(attendance,name)** returns (True, "message"), or (False, "message").

**What could go wrong**

-User may try to enter an empty name input. `return False, "Please enter name."` *Nothing changes.*

-User may try to add a student that already exists . `return False, "Student already exists."` *Nothing changes.*

On correct details:
    attendance[name] = set()
`return True, "Student attendance tracked successfully."`


## mark_present(attendance,name,date) what it takes,returns and what could go wrong. ## 

**mark_present(attendance,name,date)** returns (True, "message"), or (False, "message").

**What could go wrong**

-User may try to enter an empty date input. `return False, "Please enter date."` *Nothing changes.*

-User may try to add date for a student that doesn't exist exists . `return False, "Confirm if student exists."` *Nothing changes.*

On correct details:
    attendance[name].add(date)
`return True, "Student attendance name and date tracked successfully."`

## days_present(attendance,name) what it takes,returns and what could go wrong. ## 

**days_present(attendance,name)** returns a number of the days a student was present, returns 0 if student exists but has never been present and returns None is student doesn't exist in attendance.

**What could go wrong**

-User may try to enter an empty name input. `return False, "Please enter name."` *Nothing changes.*

-User may try to add date for a student that doesn't exist exists . `return False, "Confirm if student exists."` *Nothing changes.*

On correct details:
`return len(attendance[name])`
## best_attendance(attendance) what it takes,returns and what could go wrong ##

**best_attendance(attendance)** checks the student who has most attendances and returns his name and returns None if dictonary is empty.

**What could go wrong**
-The dictionary is empty (`{}`): Must check for this first and return `None` to prevent errors.
-Ties (two or more students have the exact same highest number of days) (e.g., the first one encountered wins)
-Prints nothing, changes nothing.


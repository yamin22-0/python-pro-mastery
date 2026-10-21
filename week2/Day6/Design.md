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

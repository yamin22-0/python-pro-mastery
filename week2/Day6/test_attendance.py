from attendance import add_student

## Tests for add_student ##

def test_add_student_good():

    attendance = {}

    result = add_student(attendance,"binka")
    assert result[0] == True
    assert result[1] == "student attendance tracked successfully."
    assert attendance["binka"] == set()

def test_add_student_duplicate():

    attendance = {"moha": set()}

    result = add_student(attendance,"moha")
    assert result[0] == False
    assert attendance["moha"] == set()

def test_add_student_empty_name():

    attendance = {}

    result = add_student(attendance," ")
    assert result[0] == False
    assert attendance == {}

def test_add_student_name_cleaning():

    attendance = {}

    result = add_student(attendance," IMRAN ")
    assert result[0] == True
    assert result[1] == "student attendance tracked successfully."
    assert " IMRAN " not in attendance
    assert "imran" in attendance

def test_add_student_two_students():

    attendance = {}

    result1 = add_student(attendance,"ahmed")
    result2 = add_student(attendance,"ali")
    assert result1[0] == True
    assert result1[1] == "student attendance tracked successfully."
    assert result2[0] == True
    assert result2[1] == "student attendance tracked successfully."
    assert len(attendance) == 2



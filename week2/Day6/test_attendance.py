from attendance import add_student,mark_present

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

def test_mark_present_good():

    attendance = {"halima": set()}

    result = mark_present(attendance,"halima","21-10-2026")
    assert result[0] == True
    assert attendance["halima"] == {"21-10-2026"}

def test_mark_present_same_date():

    attendance = {"binyamin" : set()}

    result1 = mark_present(attendance,"binyamin","21-10-2026")
    result2 = mark_present(attendance,"binyamin","21-10-2026")
    assert result1[0] == True
    assert result2[0] == True
    assert len(attendance["binyamin"]) == 1

def test_mark_present_differnt_date():

    attendance = {"binyamin" : set()}

    result1 = mark_present(attendance,"binyamin","21-10-2026")
    result2 = mark_present(attendance,"binyamin","21-11-2026")
    assert result1[0] == True
    assert result2[0] == True
    assert len(attendance["binyamin"]) == 2

def test_mark_present_non_existant_student():

    attendance = {"amish": set()}

    result = mark_present(attendance,"halima","21-10-2026")
    assert result[0] == False
    assert attendance == {"amish" : set()}

def test_mark_present_empty_date():

    attendance = {"halima": set()}

    result = mark_present(attendance,"halima"," ")
    assert result[0] == False
    assert attendance == {"halima": set()}

def test_mark_present_name_cleaning():

    attendance = {"omar": set()}

    result = mark_present(attendance," OMAR ","21-10-2026")
    assert result[0] == True
    assert " OMAR " not in attendance
    assert "21-10-2026" in attendance["omar"]


Day 6: Student Attendance

Write the DESIGN.md this evening, and review it tomorrow morning before you code. Following your cycle, design one function, code it, test it, and then do the next.

The goal: a program that records which students were present each day, and finds who attended the most.

New idea: a set, and a dictionary whose values are sets. A set keeps each item only once, and .add() doesn’t create duplicates. Here it is on different data:

python
visited = set()
visited.add("nairobi")
visited.add("nairobi")          # adding it again changes nothing
visited.add("mombasa")
print(len(visited))             # 2
print("nairobi" in visited)     # True

trips = {"amina": {"nairobi", "mombasa"}, "brian": set()}
trips["brian"].add("kisumu")
print(trips["brian"])           # {'kisumu'}

The data: a dictionary where the key is the student’s name, and the value is a set of dates they were present.

python
attendance = {
    "amina": {"2026-10-01", "2026-10-02"},
    "brian": {"2026-10-01"},
}

Rules for all functions: clean names with .strip().lower(). Functions print nothing. The first two return (True/False, "message").

Part A

add_student(attendance, name): rejects an empty name and a name that already exists. On success, it stores the name with an empty set.
mark_present(attendance, name, date): the student must exist, and the date must not be empty. On success, it adds the date to the student’s set. Marking the same date twice is allowed and changes nothing (the set keeps it once), and it returns True.

Part B
3. days_present(attendance, name): returns the number of days the student was present, or None if the student doesn’t exist.
4. best_attendance(attendance): returns the name of the student with the most days present, or None if there are no students. If two tie, the first one added wins.

Tests (at least these):

Test	Expected
add amina	True, and attendance["amina"] == set()
add amina twice	second call False
add an empty name	False, and nothing stored
mark amina present on "2026-10-01"	True, and the date is in her set
mark the same date twice	both True, and her set has 1 date (the count didn’t grow)
mark a student who doesn’t exist	False
days_present for the example above	amina gives 2, brian gives 1
days_present for a missing student	None
best_attendance for the example	"amina"
best_attendance({})	None
a tie (two students with 1 day each)	the first added

The “same date twice” test is the one that shows why a set is the right tool, and len() is how you count a set.

This evening’s design note: the data model (the example above, and what each part is), one line per function (takes ___, returns ___), and what can go wrong for each. Keep it short, and write each function’s failures right before you code it.

DSA, after the assignment is done: Group the Same Counts, a warm-up on the counting idea. Given a list like ["a", "b", "a", "c", "b", "a"], return a dictionary of how many times each item appears ({"a": 3, "b": 2, "c": 1}), then return the item that appears most often ("a"). Test with a normal list, an empty list ({} and None), and a tie. Predict first, and log two lines in DSA-LOG.md.
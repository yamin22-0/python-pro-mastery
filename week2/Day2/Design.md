# DESIGN.md: Grade Book System

## What the system does
The system is a student grading system where you add a student, give the students marks, and the system calculates the average and returns the highest student marks.

## What info system needs
* **Inputs:** `name, mark`
* **Info saved by program:** `Dictionary`
* **Output:** `Average and the best student`

## Rules of the system
1.**Adding Students:** The system asks for the name of the student first. If empty, returns `Please enter student name!`. The name is cleaned using `.strip()` and `.lower()` (spaces are allowed). Duplicate names are rejected with `Student already exists!`. Non-word characters are rejected with `Name can only contain letters or words.`

2.**Adding Marks:** The system asks for marks, checks if the student exists (if not, returns `Student doesn't exist, add student first.`), ensures marks are whole numbers (decimals like `72.5` passed as numbers are chopped via `int()`, while text words like `"fifty"` trigger `Marks can only be whole numbers.`), and enforces a `0-100` range returning `Try a number between (0-100).`.

3.**Calculations & Ties:** Finds the average. If a student has no marks or doesn't exist, returns `None` (which triggers a `"No average yet"` message in the main block). If multiple students share the exact same highest average, the tie rule dictates that the **first student added wins**.

## What could go wrong

**Duplicate entries:** User tries to add an existing student $\rightarrow$ `Student already exists!`

**Empty types:** User leaves name input empty $\rightarrow$ `Please enter student name!`

**Mistypes:** User enters digits/symbols for name $\rightarrow$ `Name can only contain letters or words.` or words for marks $\rightarrow$ `Marks can only be whole numbers.`

**Invalid types:** User enters marks $< 0$ or $> 100$ $\rightarrow$ `Try a number between (0-100).`

## What each function does

**`add_student(grades, name)`**

*Takes:* Dictionary (`grades`), string (`name`)

*Returns:* Status message string (success or error).
* **`add_mark(grades, name, mark)`**

*Takes:* Dictionary (`grades`), string (`name`), integer/string (`mark`)

*Returns:* Status message string (success or error).

**`get_average(grades, name)`**

*Takes:* Dictionary (`grades`), string (`name`)

*Returns:* Float (average) or `None`. (Automatically cleans the name using `.strip().lower()` before lookup).

**`best_student(grades)`**

*Takes:* Dictionary (`grades`)

*Returns:* String (name of best student) or `None`.

## Data Model
* **What program keeps track of:** Students and their marks.
* **Fields for each data:** Student (`name`), marks (`0-100`).
* **How they are related:** One student can have many marks stored as a list inside dictionary values.
* **What the dictionary looks like:**
  ```python
  {
      "amina": [70, 90],
      "binyamin": [88, 90],
      "khadija": [60]
  }
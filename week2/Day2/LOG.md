## What built today ##

Built a student grading system with four functions and a menu, using a dictionary where the values are lists to store multiple marks per student. The system handles student registration, mark entry with validation (0-100), average calculation, and finding the best student.

## What learnt today ##

Dictionaries with Lists: Learnt how to use a dictionary where each student's name maps to a list of integers, allowing one student to hold multiple marks.

Separation of Concerns (Return vs. Print): Practiced writing functions that handle logic and return values or error messages, while leaving all user input and printing to the main execution loop.

The "Sticky Note" Pattern (best_student): Learnt how to loop through a dictionary while tracking a running best score and name using initial None values to handle empty or uninitialized states.

Breaking Down Complex Logic: Discovered that breaking a tough problem (like finding the best student) into smaller steps or building a simplified practice version first makes it much easier to write in one sitting.

## What confused me ##

Writing best_student: Initially struggled with how to compare averages across dictionary keys and how to structure the initialization of the running maximum variables (None).

Type Management: Noticed that things like float versus string types can behave differently during input validation, reinforcing the importance of explicitly checking types when tests behave unexpectedly.
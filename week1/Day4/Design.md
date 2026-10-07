## What the system does ## 

A student grading system where it asks for the marks of 5 students and stores in a list. The system then adds the marks and prints total,the average,the lowest and the highest marks and checks if student gets above 50 or if they get 50 he/she passed so it prints the number of students who passed.

## Information the system needs ## 

(a).marks(0-100) (b).average (c).Total marks (d).highest mark (e).lowest mark  (f). Count of passing students.

## Rules of the system ## 

1.Students marks must be from (0-100) where if 5 student marks are entered the system calculates total then average. Total = sum(marks)
average = sum(marks) / len(marks)

2.Pass mark is 50 and above and Use built-in functions `sum()`, `max()`, and `min()`.

## What could go wrong ##

1.**Invalid types** - User may input a value thats not a digit(word or letter).(Enter valid marks.)
2.**Out of range types** - User may enter a number thats less than 0 or a number that's above 100.(Enter value within range.)
3.**Empty inputs** - User may leave marks as empty.(Enter valid marks!)



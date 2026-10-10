#TODO: Remember - a list of numbers(finding the largest number).
#TODO: Look at each number in the list.
#TODO: If the current number is bigger than the prevoius(what remebered) update our remembered largest number.
#TODO: Return the largest number at the end.

def find_largest(numbers):

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(find_largest(([2,3,9])))
print(find_largest(([-5,-1,-9])))
print(find_largest(([7])))

numbers = [1,2,3,4,1]

def check_duplicate_numbers(numbers):

    seen = set()

    for number in numbers:
        if number in seen:
            return True
        else:
            seen.add(number)

    return False
            
print(check_duplicate_numbers(numbers))
print(check_duplicate_numbers([1,2,3]))
print(check_duplicate_numbers([]))
print(check_duplicate_numbers([5]))




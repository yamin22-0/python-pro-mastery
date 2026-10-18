numbers = [1,2,3,4,1]

def check_duplicate_numbers(numbers):

    duplicate_num = []

    for number in numbers:
        if number in duplicate_num:
            return True
        else:
            duplicate_num.append(number)

    return False
            
print(check_duplicate_numbers(numbers))
print(check_duplicate_numbers([1,2,3]))
print(check_duplicate_numbers([]))
print(check_duplicate_numbers([5]))




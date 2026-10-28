numbers = [2,7,11,15]

def two_sum(numbers,target):

    seen = {}

    for index,number in enumerate(numbers):
        targeted = target - number

        if targeted in seen:
            return [seen[targeted],index]
        seen[number] = index

    return None

print(two_sum(numbers,9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))
print(two_sum([-1,-2,-3],-5))
print(two_sum([1,2],6))

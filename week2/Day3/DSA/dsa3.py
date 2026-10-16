numbers = [1,2,3,4]

def running_sum(numbers):

    total = 0
    sum_total = []

    for number in numbers:
        total += number
        sum_total.append(total)

    return sum_total

print(running_sum(numbers))
print(running_sum([5]))
print(running_sum([3,-1,2]))
print(running_sum([]))

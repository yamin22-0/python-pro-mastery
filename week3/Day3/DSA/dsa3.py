def balanced_brackets(brackets):

    count = 0

    for bracket in brackets:
        if bracket == "(":
            count += 1
        elif bracket == ")":
            count -= 1

        if count < 0:
            return False

    return count == 0

print(balanced_brackets("(())"))
print(balanced_brackets("(()"))
print(balanced_brackets(")("))
print(balanced_brackets("()()"))
print(balanced_brackets(""))
print(balanced_brackets("((("))
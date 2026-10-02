#TODO: Ask user for number of users.
#TODO: Ask for the bill.
#TODO: Ask or the tip percentage.
#TODO: If number of users is 0,return Users can't be less than 0.
#TODO: If Bill is 0 or negative,return Enter Valid Amount.
#TODO: If tip percentage is negative,return Enter valid tip.
#TODO: Tip of 0 is allowed.
#TODO: Calculate tip_amount,(bill * (tip_percentage / 100)).
#TODO: Calculate total_bill,(bill + tip_amount).
#TODO: Calculate each_person_bill, (total_bill/num_of_persons).
#TODO: Prints the total bill and each persons share.

def calculate_bill_spliter(number_of_persons,bill,tip_percentage):

    if number_of_persons <= 0:
        print("Invalid!,Number of users must be atleast 1.")
        return

    if bill <= 0:
        print("Invalid amount!,Enter amount.")
        return
    
    if tip_percentage < 0:
        print("Invalid tip!,Enter tip percentage.")
        return

    tip_amount = bill * (tip_percentage / 100)
    total_bill = bill + tip_amount
    each_persons_bill = total_bill / number_of_persons

    print(f"The Total bill is ${round(total_bill,2)} and Everyone pays {round(each_persons_bill,2)} and tip is {round(tip_amount,2)}")

try:
    persons = int(input("Enter number of customers: "))
except ValueError:
    print("Persons must be a number.")
    exit()
try:
    amount = float(input("Enter Amount: "))
except ValueError:
    print("Amount must be a number.")
    exit()
try:
    tip = float(input("Enter tip%: "))
except ValueError:
    print("Tip must be number.")
    exit()

calculate_bill_spliter(persons,amount,tip)








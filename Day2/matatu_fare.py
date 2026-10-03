#TODO: Ask user for number_of_passegers.
#TODO: Ask user for location_to.
#TODO: Ask if peak_time.
#TODO: Validate If number_of_passengers = 0 or 
#           is negaitve or words.
#TODO: Validate if Location exists in fare_list,
#         if it was written as number or it's in capital,
#         or spaces have been added between the letters.
#TODO: Validate if peak_time is anything but option(yes/no).
#TODO: Calculate total_fare. total_fare = number_of_passengers * per_person_fare.
#TODO: Calculate per_person_fare. per_person_fare = (total_fare / number_of_passengers).
#TODO: Print (f"The fare to ${location_to} is ${total_fare} and each person pays ${per_persons_fare}").


def matatu_fare(number_of_passengers,location_to,peak_time):

    fare_list = {
        "westlands" : 50,
        "rongai" : 80,
        "thika" : 100,
        "kitengela" : 120
        }    

    if number_of_passengers <= 0:
        print("Invalid! Enter number of passengers.")
        return
    
    location_to = location_to.strip().lower()
    if location_to not in fare_list:
        print("Invalid! Enter Location.")
        return

    per_person_fare = fare_list[location_to]

    peak_time = peak_time.strip().lower()
    if peak_time == "yes":
        per_person_fare += 30
    elif peak_time == "no":
        pass
    else:
        print("Choose 'yes' or 'no'")
        return

    total_fare = number_of_passengers * per_person_fare
    
    print(f"The total fare to {location_to.title()} is Ksh {total_fare} and each person pays Ksh {per_person_fare}")
try:
    passengers = int(input("Enter number of passengers: "))
except ValueError:
    print("Enter valid parameters.")
    exit()
destination = input("Enter destination: ")
peak_fare = input("Choose 'yes' or 'no': ")

matatu_fare(passengers,destination,peak_fare)



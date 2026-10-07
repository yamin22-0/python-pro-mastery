## What the Matatu fare collection system does ##

It's a system that makes it easiers to collect fare for matatus. Eg a passengers enters a matatu and the system asks how many passengers are in the matatu then the system asks to input the location they are goint to eg westlands = 50 , Rongai = 80 etc and then the system asks if it's peak time then if it's peak time the fare gets adds 30 on top of the fare.

## Information this system needs ## 

(a).number_of_passengers (b).location_to (c).Peak_time (d).total_fare 
(e).fare_list (g).per_person_fare.

## Rules of the system 

1.The total_fare is calculated by taking the number of passengers and multiplying it to fare depending on the destination and check if its peak time if peak time is yes add 30 ksh to the fare.

2.per_person_fare is calculated by taking the total_fare and dividing by number_of_passengers.

## What can go wrong ## 

1.User may not type in number of passengers to be 0 or words or number of passengers can't be - number.(Invalid! Enter number of passengers.)

2.User may skip entering the location they are going to or write a location that's not within the system or enter number for location while it's supposed to be in words only.(Invalid! Enter Location.) or may enter location in capital letters or may add spaces between the letters

3.User may type a number for peak time peak time is just yes/no.
(Invalid! Enter valid option.)



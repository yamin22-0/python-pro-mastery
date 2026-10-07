## What the bill spliter system does ##
1.Bill Spliter --> This is a system That is supposed to split bills between people who shared a table at a meal and everyone pays for himself.
## Information the bill system keeps ##
2.This system keeps the - (a).The Bill , (b).Tip percentage. (c).Total (d).Number of people whom the bill is split. (e).Tip amount (f).Each persons share

## Rules  ##
3.(a) --> The total tip will be calculated through percentages and added to everyones bill and everyone will pay their bill plus the tip.
         --> If the bill is 1000ksh and tip is 10% 
              To find the tip = bill * (10 / 100).
              To find The total = bill + tip. 
  (b) --> Each persons share will be calculated through the total being taken and divided by the number of people at the table.
            personal_bill = total / num_of_pple

  (c) --> Tip can be 0

## What can go wrong ##
4. (a) --> A user may enter a (-) negative number or 0.If amount is    negative or 0 the system should return ("Invalid Amount,Enter Amount)
   (b) --> A user may type words instead of Amount.If user enter words instead of number the system should return ("Invalid parameters, Provide correct details.)
   (c) --> Number of people can't be 0.If the number of people is 0 return (Invalid , Users must be atleast 1.)

# print the gretings
print("Welcome to the tip calculator")
#print the bill amount
bill = float(input("What was the total bill? $"))
#print tip amount
tip = int(input("How much tip you would like to give? 10,12 or 15?\t"))
#print no of people
no_of_people = int(input("How many people to split the bill?\t"))
#calculate the total bill
total_bill = round((bill+(bill*tip)/100)/no_of_people,2)
#print final bill amount
print(f"Each person should pay: ${total_bill}")

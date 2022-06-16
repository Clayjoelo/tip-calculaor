
print("Welcome to the tip calculator.")

bill = input("What was the total bill? ")
num_people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

tip = str("1." + tip)



total = round(float(bill) / int(num_people) * float(tip), 2)

print("Each person should pay: " + str(total))
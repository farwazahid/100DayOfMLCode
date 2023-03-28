print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
input("What percentage tip would you like to give? 10, 12, 15? ")
input("How many person to split the bill? ")
tip = (12/100) * bill
total_bill = float(tip) + float(bill)
bill_per_person = round((float(total_bill)/7),2)
print(f"Each person should pay: {bill_per_person}")

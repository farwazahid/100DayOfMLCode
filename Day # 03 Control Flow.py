print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What's your age"))
bill = 0
if height >= 120:
    print("You can Ride roller coaster")
    if age < 12:
        bill += 5
    elif age >= 1 and age <18:
        bill += 7
    elif age >= 45 and age <= 55:
        bill = 0
    else :
        bill +=12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
      bill += 3
    print(f"Your total bill is ${bill}")

else:
    print("SOrry, You can't ride rolleer coaster")


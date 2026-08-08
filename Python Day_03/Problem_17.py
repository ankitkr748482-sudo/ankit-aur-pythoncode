# Electricity Bill calculation by elif statement 

units = int(input("Enter your units:"))
if( units > 0 and units <= 100):
    print("Your bill is:",units * 5, "rupees")
elif( units > 100 and units <= 200):
    print("Your bill is:", units * 7, "rupees")
elif( units > 200):
    print("Your bill is:", units * 10, "rupees")
else:
    print("Invalid units! please enter the positive units")
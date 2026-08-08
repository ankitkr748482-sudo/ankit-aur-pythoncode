# Check if a number is even and also divisible by 5
   
num = int(input("Enter a number:"))

if (num % 2 == 0):
    if (num % 5 == 0):        
        print("This number is even and divisible by 5")
    else:
        print("This number is even but not divisible by 5")
else:
    print("This number is odd") 
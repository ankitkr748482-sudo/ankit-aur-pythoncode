# ATM Security pin 

pin = int(input("Enter your pin:"))
if( pin == 123455):
    amount = int( input("Enter amount:"))
    if( amount <= 5000):
        print("Transaction successful !")
    else:
        print("Your entered amount is cross the trasacation limit,So please entered your amount less than 5000")
else:
    print("Wrong pin! Try again")
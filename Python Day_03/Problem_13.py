# check leap year and century

year = int(input("Enter year:"))
if( year % 100 == 0):
    if( year % 400 == 0):
        print("it is century year and a leap year")
    else:
        print("it is century year but not a leap year")
else:
    if( year % 4 == 0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
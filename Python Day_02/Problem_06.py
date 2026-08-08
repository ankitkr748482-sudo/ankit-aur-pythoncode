# Made voting machine code according to age 

age = int(input("Enter age here:"))
if ( age > 1 and age < 18):
    print("You cannot give vote and you are not able for doing marriage.")
elif( age >= 18 and age <= 30 and age > 30):
    print("You can give vote and now you are able for doing marriage.")
else:
    print("invalid number")
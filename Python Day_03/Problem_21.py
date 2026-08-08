# voting and driving check

age = int(input("Enter here your age:"))
if( age >= 18):
    if( age >= 21):
        print("You can give vote and eligible for driving.")
    else:
        print("You can give vote but not eligible for driving.")
else:
    print("You are not eligible for both driving and voting. ")
# check age and gender eligibility

age = int(input("Enter here your age:"))
gender = input("Enter here your gender (M/F):")
if( gender == "M"):
    if(age >= 18):
        print("You are eligible for male indian team. ")
    else:
        print("You are not eligible for male indian team.")
elif( gender == "F"):
      if(age >= 18):
        print("You are eligible for female indian team.")
      else:
        print("You are not eligible for female indian team.")
else:
    print("Invalid age and gender! Please enter a valid age and gender.")
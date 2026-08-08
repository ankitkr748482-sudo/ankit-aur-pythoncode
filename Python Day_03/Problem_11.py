# check whether a person is eligible for college admission

age = int(input("Enter the student age:"))
marks = int(input("Enter user student marks: "))

if( age == 17 or age > 17 ):
    if( marks == 60 or marks > 60):
        print("This student is eligible for admission")
    else:
        print("This student is not eligible for admission due to low marks")
else:
    print("This student is not eligible due to age")
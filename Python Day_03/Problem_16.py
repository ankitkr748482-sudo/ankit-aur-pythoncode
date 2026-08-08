# Marks se grade

marks = int(input("Enter the marks:"))
if( marks >= 0 and marks <= 100):
    if( marks > 90):
        print("Excellent") 
    else:
        if( marks >= 75):
           print("very good")
        else:
            if( marks >= 60):
               print("Good")
            else:
                 if( marks >= 40):
                    print("Good")
                 else:
                    print("Fail")
else:
   print("Invalid marks! please enter between 0 to 100.")
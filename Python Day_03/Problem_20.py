# Triangle type finder code 

side_01 = int(input("Enter first side here:"))
side_02 = int(input("Enter second side here:"))
side_03 = int(input("Enter third side here:"))
if( side_01 + side_02 > side_03 and side_02 + side_03 > side_01 and side_03 + side_01 > side_02):
    if( side_01 == side_02 and side_02 == side_03):
        print("Equilateral triangle")
    else:
        if( side_01 == side_02 or side_01 == side_03 or side_03 == side_02):
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
else:
    print("These sides are not right for making a valid triangle.")
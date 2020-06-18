#This function will help to find a side of Right triangle
#Just run and input the length of side's
import math as m

def hypotenuse(a_side,hypotenuse_lenght):
    """
    hypotenuse_lenght**2 = a_side**2 + b_side #formula
    """
    b_side = hypotenuse_lenght**2 - a_side**2
    square_root = m.sqrt(b_side)
    rounded = round(square_root,1)
    print("HERE is your lenght : ", rounded)

lenght_of_first_side = float(input("Input one side of triangle: "))
lenght_of_hypotenuse_side  = float(input("Input hypotenuse of triangle: "))

hypotenuse(lenght_of_first_side,lenght_of_hypotenuse_side)

#This is new file to  test if git is working.

import math as m

def hypotenuse(a_side,b_side):
    c_squared = a_side**2 + b_side**2
    square_root = m.sqrt(c_squared)
    rounded = round(square_root,1)
    print(rounded)

lenght_of_first_side = float(input("Input one side of  triangle: "))
lenght_of_second_side  = float(input("Input second side of  triangle: "))

hypotenuse(lenght_of_first_side,lenght_of_second_side)


#sometdfsdf
#Circle or Rectangle calculations
#Jeffrey McCullough
#This program will send 
#February 20, 2023

import math
from Circle import *
from Rectangle import *
pie = round(math.pi, 2)

while True:
    menu = input("\tMenu\n1) Area of a circle\n2) Circumference of a circle\n3) Area of a rectangle\n4) Perimeter of a rectangle\n5) Quit\nEnter your choice: ")
    if menu == "1":
        radius = float(input("Enter the circle's radius: "))
        print(f"The circumference is {circumference(radius, pie)}")
    elif menu == "2":
        radius = float(input("Enter the circle's radius: "))
        print(f"The area is {circle_area(radius, pie)}")
    elif menu == "3":
        length = float(input("Enter the rectangle's length: "))
        width = float(input("Enter the rectangle's width: "))
        print(f"The perimeter is {perimeter(length, width)}")
    elif menu == "4":
        length = float(input("Enter the rectangle's length: "))
        width = float(input("Enter the rectangle's width: "))
        print(f"The area is {rectangle_area(length, width)}")
    elif menu == "5":
        break
    else:
        print("Please enter one of the choices in the menu.")

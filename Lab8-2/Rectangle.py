#Rectangle
#Jeffrey McCullough
#This provides the functions to find the area or perimeter of a rectangle given the width and length.
#February 20, 2023

def perimeter(length, width):
    perim = (length * 2) + (width * 2)
    return perim

def rectangle_area(length, width):
    area = length * width
    return  area
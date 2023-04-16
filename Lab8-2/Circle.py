#Circle
#Jeffrey McCullough
#This provides the functions to be called for finding the area or circumference of a circle given a radius.
#February 20, 2023

def circumference(rad, my_pi):
    circum = (rad * 2.0) * my_pi
    return circum

def circle_area(rad, my_pi):
    area = (rad ** 2) * my_pi
    return area

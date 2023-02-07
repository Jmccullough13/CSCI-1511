#Camping Trip Packing List
#Jeffrey McCullough
#This is a program that will display a list of items to be packed for a camping trip
#January 22, 2023

packing = ["pillow", "sleeping bag", "tent", "tent poles", "camp stove", "fuel", "extra clothes", "marshmallows", "chocolate", "graham crackers", "walking stick", "other food"]
print(f"{len(packing)} items packed in car")
print("Already packed for trip: ")
packing.sort()
for items in packing:
    print(items)

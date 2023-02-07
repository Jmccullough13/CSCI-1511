#Camping Trip Packing List
#Jeffrey McCullough
#This is a program that will display a list of items to be packed for a camping trip. An item unable to be packed is removed from the list and the list is reprinted.
#January 22, 2023

packing = ["pillow", "sleeping bag", "tent", "tent poles", "camp stove", "fuel", "extra clothes", "marshmallows", "chocolate", "graham crackers", "walking stick", "other food"]
print(f"{len(packing)} items packed in car")
print("Already packed for trip: ")
packing.sort()
for items in packing:
    print(items)
packing.append("matches")
print(f"Recently packed: {packing[-1]}\n")
for items in packing:
    print(items)
popped = packing.pop(11)
packing.insert(11, "binoculars")
print(f"\nReplaced {popped} with {packing[11]}")
print(f"{len(packing)} items packed in car")
for items in packing:
    print(items)
del packing[11]
print(f"\n{len(packing)} items packed in car")
for items in packing:
    print(items)

#Car Packing List
#Jeffrey McCullough
#January 16, 2023

packing = []
print("Make a list for packing")
x = int(input("Enter the number of items on the list: "))
for i in range(0, x):
    item = input("Item: ")
    packing.append(item)
for items in packing:
    print(items)
print(f"Number of items in list: {len(packing)}")
packing.reverse()
for items in packing:
    print(items)
#length of array
cars=["bmw","toyota","ford"]
x=len(cars)
print(x)
#Looping array elements
for x in cars:
    print(x)
#add an element to an array
cars.append("honda")
print(cars)   
#Remove element from the array
cars.pop(0)
print(cars)
#also use remove function,remove element from the array
cars.remove("ford")
print(cars)
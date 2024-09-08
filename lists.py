# Adding Elements to a List
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

# add an item to list 
motorcycles.append('ducati')
print(motorcycles)

# inserting elements into a list
motorcyclesInsert = ['honda', 'yamaha', 'suzuki']

motorcyclesInsert.insert(0, 'ducati')

# In this example, the code atuinserts the value 'ducati' 
# at the begin- ning of the list. The insert() method opens
#  a space at position 0 and stores the value 'ducati' at 
# that location. This operation shifts every other value 
# in the list one position to the right:

# removing an Item Using the del Statement

del motorcyclesInsert[3]
print(motorcyclesInsert)

# Pop()Method 
# to use the value of an item after you remove it from a list.


motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)

# removing an Item by Value
# motorcycles.remove('ducati')


# Sorting a List Permanently with the sort() Method
# Python’s sort() method makes it relatively easy to sort a list.

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort()

# reverses order.
cars.sort(reverse=True)

print(cars)

print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)

# Finding the Length of a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# last item in the list no matter its length
print(motorcycles[-1])
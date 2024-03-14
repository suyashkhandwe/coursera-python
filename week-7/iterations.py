"""Module for demo of loops/iterations."""

X = 5
while(X < 10):
    print(X)
    X = X + 1

# Example of collections of integers
for counter in [5,4,3,2,1]:
    print(counter)
print('BlastOff!!')

# Example of collections of strings
for friend in ["foo","bar","baz"]:
    print("hey", friend)

# Largest and smallest numbers
largest = None
smallest = None
for number in [3,41,12,9,74,15]:
    if (largest is None) or number > largest:
        largest = number
    if (smallest is None) or number < smallest:
        smallest = number
print('Smallest:', smallest, 'Largest:', largest)
        
    
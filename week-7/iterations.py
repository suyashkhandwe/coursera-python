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
L = None
S = None
for number in [3,41,12,9,74,15]:
    if (L is None) or number > L:
        L = number
    if (S is None) or number < S:
        S = number
print('Smallest:', S, 'Largest:', L)

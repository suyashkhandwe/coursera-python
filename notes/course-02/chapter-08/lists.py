"""Module for demo of lists."""

STRING_LIST = ['a','b','c']
INTEGER_LIST = [1,2,3]
MIXED_LIST = ['a',2,3.4]
NESTED_LIST = [1,['a',2],3.4]

print(STRING_LIST)

for string in STRING_LIST:
    print(string)

print(INTEGER_LIST)
print(MIXED_LIST)
print(NESTED_LIST)

# Concat
COMBINED_LISTS = STRING_LIST + MIXED_LIST
print(COMBINED_LISTS)

#Slicing
print(STRING_LIST[1:2]) # Upto but not including 2
print(STRING_LIST[0:1]) # Upto but not including 1

friends = [ 'Joseph', 'Glenn', 'Sally' ]
print(friends[2])

print(len(STRING_LIST))

X = list(range(5))
print(X)
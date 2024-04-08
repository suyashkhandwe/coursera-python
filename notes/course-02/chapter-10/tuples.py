"""Module for demo of tuples."""

properties = ('Tuple are list lists', 'Can be 2 3 or more', 'Unmodifiable')
print(properties.index('Tuple are list lists'))
print(properties[0])
print(properties[1])

try:
    properties[0] = 'fail'
except:
    print('Can not modify a tuple')

for prop in properties:
    print(prop)

(example_new, example_tuple) = ('a', 10)
print('Sample tuple 0:', example_new)
print('Sample tuple 1:', example_tuple)

# Tuples can do a value by value comparison for number or strings.
if (1,2,3) < (2,3,4):
    print('Tuple is not less')
else:
    print('Tuple is not more')

# Can help sort dictionaries - by key order
d = {'a':10, 'b': 20, 'c': 30}
d_sorted_by_key = sorted(d.items())
print('Unsorted:', d)
print('Sorted by key:', d_sorted_by_key)

# But you can sort by value as well
tmp = list()
for (k,v) in d.items():
    tmp.append((v,k))

d_sorted_by_value = sorted(tmp) # Reverse=true will sort in the other direction
print('Sorted by value:', d_sorted_by_value)

#Revere the key/value again
for (v,k) in d_sorted_by_value:
    print('k:', k, 'v:', v)

# Read about -List comprehension
# List comprehension shorthand - replaces the following lines -
# tmp = list()
# for (k,v) in d.items():
#   tmp.append((v,k))
# d_sorted_by_value = sorted(tmp) # Reverse=true will sort in the other direction
# print('Sorted by value:', d_sorted_by_value)
print('List comprehension:', sorted([(v,k) for (k,v) in d.items()]))

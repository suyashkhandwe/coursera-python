"""Module for demo of UNICODE characters and string"""

# ord >> ordinal

print('ASCII for H:', ord('H'))
print('ASCII for G:', ord('G'))
print('ASCII for h:', ord('h'))
print('ASCII for \\n:', ord('\n'))
print('Revere ASCII for 108 105 110 101:', chr(108),chr(105),chr(110),chr(101))

print('UTF-8 encoded for H:', 'H'.encode())
print('UTF-8 encoded for h:', 'h'.encode())
print('UTF-8 encoded for \\n:', '\n'.encode())

# Python 2 - Byte string and regular string were the same, while unicode string and regular string were different.
# Python 3 - Byte string and regular string are different, while unicode string and regular string are the same.
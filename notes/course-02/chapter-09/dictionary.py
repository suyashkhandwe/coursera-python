"""Module for demo of dictionary."""

# Basic implementations

cabinet = dict()
cabinet['a'] = 1
cabinet['b'] = 2
cabinet['c'] = 'abc'
print('simple dict:', cabinet)

# Dictionary constants
DICT_CONST = {'a': 10, 'b': 20}
print('dict const:', DICT_CONST)

# Dictionary.get(..)
try:
    print(DICT_CONST['aa'])
except:
    print('Not found key:', 'aa')

print(DICT_CONST.get('aa', 'Not found without traceback'))

print(DICT_CONST.keys(), DICT_CONST.values(), DICT_CONST.items())

for key in DICT_CONST.keys():
    print('dict key:', key)

for value in DICT_CONST.values():
    print('dict value:', value)

for k,v in DICT_CONST.items():
    print('simple item:', k, v)

counts = dict()
counts['a'] = -1
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1

print(counts['a'])
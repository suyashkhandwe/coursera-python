"""Module for demo of RegEx."""
import re

expr = re.compile('^foo.*bar:$')
print(re.findall(expr, 'foo-baz-bar:'))
print(re.search(expr, "foo-baz-bar:"))

# Example of how the findall returns a collection of all matches
print(re.findall('[0-9]+', 'foo 10 this bar 20'))

# EXample of greedy and non-greedy match
print(re.findall('^F.+:', 'From: greedy:match::'))
print(re.findall('^F.+?:', 'From: non-greedy:match::'))

print(re.findall('@(\S+)', 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'))

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

print(re.findall('\S+?@\S+', 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'))
# Python Regular Expression Quick Guide
# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times 
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times 
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end

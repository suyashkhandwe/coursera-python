"""Module for demo of conditionals."""

X = 2
if X < 10:
    print("less than 10")
    # Indentation matters here which is typically 4 spaces and indents indicate where the current conditional starts and ends
else:
    print("more than 2")


# Extension with if..elif..else ladder

if X < 2:
    print("less than 2")
elif X == 2:
    print("2")
else:
    print("greater than 2")

# Except structure -- try...except
A = 10
B = 0
try:
    c = A/B
    print("c =",c)
except:
    print("divide by zero is not allowed")

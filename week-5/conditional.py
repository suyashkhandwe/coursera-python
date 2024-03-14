x = 2
if x < 10:
    print("less than 10")
    # Indentation matters here which is typically 4 spaces and indents indicate where the current conditional starts and ends
else:
    print("more than 2")


# Extension with if..elif..else ladder

if x < 2:
    print("less than 2")
elif x == 2:
    print("2")
else:
    print("greater than 2")

# Except structure -- try...except
a = 10
b = 0
try:
    c = a/b
    print("c =",c)
except:
    print("divide by zero is not allowed")


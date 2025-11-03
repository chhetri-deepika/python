# logical operations(and,or,not)

# truth table for "or"
# print(True or True)   # True
# print(True or False)  # True        
# print(False or True)  # True
# print(False or False) # False

# truth table for "and"
# print(True and True)   # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False) # False

# truth table for "not"
# print(not True)   # False 
# print(not False)  # True

a=10
b=20
if a>5 and b>15:
    print("both conditions are true")

if a>5 or b<15:
    print("at least one condition is true")

mass = int(input("What is the object mass"))
g = int(9.8)
force = mass * int(g)
unit = 'N'
if force > int(1000):
    print("Object is too heavy")
elif force < int(10):
    print("Object is too light")
else:
    print("Object is the right weight")
print(force, str(unit))

# 2
number = int(input('Enter number here'))
if number in range(1, 100):
    print(number)

# 3
Sum = 0

print("Please Enter the total amount of bugs for each day\n")
for i in range(1, 8):
    num = int(input("Day %d = " %i))
    Sum = Sum + num
print("The Sum of bugs for all days      = ", Sum)




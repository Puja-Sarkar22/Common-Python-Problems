a = input ("first number")
b = input ("second number")
a = int(a)
b = int(b)
print("the result is :", a/b)
print("the result is :", a//b)
a = a + b
b = a - b
a = a - b
print("the result is :", a, b)
x = input("Enter mark price")
x = int(x)
y = x -((x * 20)/100)
cost = 2450
cost = cost - y
print("The result is:", cost)
z = 5
for i in range(0,z):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

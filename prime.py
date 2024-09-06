no = int(input("enter the number: "))
for n in range(2, no + 1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)


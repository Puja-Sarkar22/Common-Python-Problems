def is_armstrong(l,num):
    for i in range (l,num + 1):
        sum = 0
        temp = i
        while temp > 0:
        t = temp % 10
        sum += t * t * t
        temp //= 10
        return i == sum
    l = int(input("lower half"))
    num = int(input("upper half"))
print(f"Armstrong numbers within {limit}: {armstrong_nums}")

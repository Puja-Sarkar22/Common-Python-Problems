size = int(input("Enter the size of the list: "))
numbers = []
for i in range(size):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)
numbers.sort(reverse=True)
second_largest = numbers[1]
print(f"The second largest number is: {second_largest}")
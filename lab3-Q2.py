numbers = []

for i in range(10):
    value = int(input("Enter a number: "))
    numbers.append(value)

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("The largest number is:", largest)
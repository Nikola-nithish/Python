07.10 8:20 AM
num_elements = int(input("Enter number of elements in list: "))
numbers = []
for i in range(num_elements):
    value = int(input("Enter the value: "))
    numbers.append(value)

print("Original list:", numbers)

ascending = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i+1]:
        ascending = False
        break

if ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")


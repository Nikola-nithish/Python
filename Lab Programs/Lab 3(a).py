07.10 8:06 AM
def find_occurrences(numbers, target):
    positive_indices = []
    negative_indices = []
    count = 0
    
    for i in range(len(numbers)):
        if numbers[i] == target:
            positive_indices.append(i)
            negative_indices.append(i-len(numbers))
            count += 1
    
    return count, positive_indices, negative_indices


# Read the list of numbers from the user
numbers = input("Enter a list of numbers separated by commas: ").split(',')
numbers = [int(num.strip()) for num in numbers]

# Read the number to be found from the user
target = int(input("Enter the element to be found: "))

# Find the occurrences and indices
occurrences, positive_indices, negative_indices = find_occurrences(numbers, target)

# Display the results
print(f"Element {target} occurs {occurrences} time(s) in the list.")
print("Positive Index:", ', '.join(str(idx) for idx in positive_indices))
print("Negative Index:", ', '.join(str(idx) for idx in negative_indices))


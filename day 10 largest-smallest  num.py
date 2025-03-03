def find_largest_smallest(lst):
    largest = lst[0]
    smallest = lst[0]

    for num in lst:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

numbers = [15, 42, 2, 20, 36, 39, 24]
largest, smallest = find_largest_smallest(numbers)

print("Original List:", numbers)
print("Largest Number:", largest)
print("Smallest Number:", smallest)

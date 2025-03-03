def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

numbers = [1, 2, 3, 4, 2, 7, 8, 8, 3]
duplicates = find_duplicates(numbers)

print("Original List:", numbers)
print("Duplicate Values:", duplicates)

#Write a Python program to calculate the sum of the numbers in a given tuple.
#Input: tuples_list = [(1, 2), (3, 4), (5, 6)]


tuples_list = [(1, 2), (3, 4), (5, 6)]

total_sum = 0

for tup in tuples_list:
    
    total_sum += sum(tup)


print("The sum of the numbers in the tuple is:", total_sum)

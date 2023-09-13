numbers = [95, 95, 85]

# Create a dictionary to store the count of each number
count_dict = {}
for num in numbers:
    if num not in count_dict:
        count_dict[num] = 1
    else:
        count_dict[num] += 1

# Sort the unique numbers in ascending order
unique_numbers = sorted(count_dict.keys())

# Initialize a rank counter
rank = 1

# Print the rank and the numbers with their counts
for num in unique_numbers:
    count = count_dict[num]
    for i in range(count):
        print(f"Rank {rank}: {num}")
    rank += count

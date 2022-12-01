def get_formatted_input():
    """Splits input file into a list of strings, each corresponding to the values of the elf"""
    with open("input.txt") as inputfile:
        values = inputfile.read()
        elves = values.split("\n\n")  # Elves split by a blank line
        return elves


# Part 1
elves = get_formatted_input()
calorie_counts = []
for elf in elves:
    calorie_counts.append(sum([int(food_item) for food_item in elf.split()]))  # Split the string for each elf into lists of ints, sum those, append output to `calorie_counts`
sorted_counts = sorted(calorie_counts, reverse=True)  # Reverse sorting puts in desc order
max_calories = sorted_counts[0]
print(f"Max calorie count: {max_calories}")

# Part 2
top_three_calorie_counts = sum(sorted_counts[:3])  # Sum 0th to 3rd element, not inclusive
print(f"Top 3 Calorie Counts, summed: {top_three_calorie_counts}")

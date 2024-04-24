import re

sum_info_counts = {}

# Regular expression pattern to find the sums, decisions, and outcomes
pattern = r"Player's original sum: (\d+), Decision: (\w+), Outcome: (\w+)"

# Open the text file
with open("blackjack_data.txt", "r") as file:
    # Read the text from the file
    text = file.read()

    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    # Count occurrences of each sum, decision, and outcome
    for match in matches:
        sum_val, decision, outcome = match
        key = (int(sum_val), decision, outcome)  # Convert sum_val to int for sorting
        sum_info_counts[key] = sum_info_counts.get(key, 0) + 1

# Sort the output by sum value
sorted_counts = sorted(sum_info_counts.items(), key=lambda x: x[0])

# Print the sorted counts
for key, count in sorted_counts:
    sum_val, decision, outcome = key
    print(f"Sum: {sum_val}, Decision: {decision}, Outcome: {outcome}, Count: {count}")

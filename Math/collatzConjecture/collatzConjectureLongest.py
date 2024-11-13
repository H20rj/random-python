import matplotlib.pyplot as plt

nums = [7]  # Initialize the list of numbers

longest_sequence = range(1, 1001, 2)  # To store the longest sequence for plotting

# Variables to track the number with the longest sequence
longest_sequence_number = None
longest_sequence_length = 0

for num in nums:  # Iterate through each number in the list
    num_id = int(num)  # Store the original number for printing later

    num_list = [num_id]  # Initialize the list to store the sequence
    current_length = 0  # To track the length of current sequence

    while num != 1:  # Continue the loop until num is 1
        current_length += 1  # Increment the step count
        if num % 2 == 0:  # If num is even
            num /= 2  # Divide num by 2
        else:  # If num is odd
            num = 3 * num + 1  # Set num to 3*num + 1

        num_list.append(int(num))  # Append the current num to the list as an integer

    # Update the longest sequence information if current one is longer
    if current_length > longest_sequence_length:
        longest_sequence_length = current_length
        longest_sequence_number = num_id
        longest_sequence = num_list  # Update the longest sequence

# Print the number with the longest Collatz sequence
print(
    f"The number with the longest Collatz sequence is {longest_sequence_number} with a length of {longest_sequence_length + 1} steps.")

# Plotting the longest Collatz sequence
plt.figure(figsize=(10, 6))
plt.plot(longest_sequence, label=f"Start: {longest_sequence_number}")

plt.xlabel('Iterations')
plt.ylabel('Value')
plt.title('Longest Collatz Conjecture Sequence')
plt.legend()
plt.grid(True)

plt.show()

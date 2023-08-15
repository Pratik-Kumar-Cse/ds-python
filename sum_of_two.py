# Define a function named `two_sum` that takes two integer parameters `a` and `b`
def two_sum(a, b):
    while b != 0:  # Iterate until b becomes 0
        temp = (a & b) << 1  # Calculate the carry and shift it left by 1 position
        a = a ^ b  # Perform bitwise XOR of a and b to get the sum without carry
        b = temp  # Update b with the carry for the next iteration
    return a  # Return the final result after bitwise addition

# The entry point of the program
if __name__ == "__main__":
    result = two_sum(5, 10)  # Call the `two_sum` function with inputs 5 and 10
    print("result:", result)  # Print the result of bitwise addition


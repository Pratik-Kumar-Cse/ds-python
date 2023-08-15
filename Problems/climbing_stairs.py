def climbing_stairs(num):
    if num <= 1:  # Base cases: if there's only one or zero step, return num
        return num

    a, b = 1, 1  # Initialize a and b with the first two Fibonacci numbers

    # Loop starting from 2 up to num (inclusive) to calculate Fibonacci numbers
    for _ in range(2, num + 1):
        a, b = b, a + b  # Update a and b using the Fibonacci sequence logic

    return b  # Return the final Fibonacci number, representing the ways to climb stairs


if __name__ == "__main__":
    number = 5  # Define the input number of stairs to climb
    result = climbing_stairs(number)  # Call the optimized climbing_stairs function
    print("result:", result)  # Print the result of climbing stairs

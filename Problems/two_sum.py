def twoSum(nums, target):
    hash_map = {}  # Create a dictionary to store differences and their indices
    for i, num in enumerate(nums):  # Use enumerate to directly get both index and value
        if num in hash_map:
            return [hash_map[num], i]  # Return the indices if a complement is found
        hash_map[target - num] = i  # Store the difference along with its index
    return []  # Return an empty list if no solution is found

def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 6
    result = twoSum(nums, target)
    print(result)

if __name__ == "__main__":
    main()
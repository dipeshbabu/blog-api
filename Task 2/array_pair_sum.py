def find_pair_with_sum(nums, target):
    """
    Finds a pair of numbers in the given list that sum up to the target value.

    Args:
        nums (list): A list of integers.
        target (int): The target sum.

    Returns:
        str: If a pair is found, returns a string representation of the pair.
             If no pair is found, returns "Pair not found".
    """
    init = set()

    for num in nums:
        complement = target - num
        if complement in init:
            return f"Pair found ({num}, {complement})"
        init.add(num)

    return "Pair not found"


input1 = [8, 7, 2, 5, 3, 1]
target1 = 10
print(find_pair_with_sum(input1, target1))

input2 = [5, 2, 6, 8, 1, 9]
target2 = 12
print(find_pair_with_sum(input2, target2))

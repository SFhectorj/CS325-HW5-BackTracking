def amount(A, S):
    """
    Parameters: A = Amount values, S = target sum
    This function will implement a backtracking algorithm to find
    all unique combinations of numbers that sum up to the target sum (S).
    """
    # Part 1: Sorting
    A.sort()
    result_list = []

    # Part 2: Helper Function
    def combination_helper(remaining_sum, list_of_combos, starting_point):
        """
        :param remaining_sum: The sum needed to be achieved
        :param list_of_combos: amounts of selected amounts
        :param starting_point: Position in A set to begin.
        This is a helper function that stores the main backtracking implementation
        for the amount function.
        """
        # Part 3: Base case
        if remaining_sum == 0:
            # makes a copy and adds to the list of combinations
            result_list.append(list_of_combos)
            return
        # edge case for negative numbers
        elif remaining_sum < 0:
            return

        # Part 4
        # Set the starting point as the index
        i = starting_point
        while i < len(A):
            # Add the element at the current index
            list_of_combos.append(A[i])
            # Recursion to update the remaining sum and move to the next index
            combination_helper(remaining_sum - A[i], list_of_combos, i + 1)
            # Part 5: Backtrack
            list_of_combos.pop()
            








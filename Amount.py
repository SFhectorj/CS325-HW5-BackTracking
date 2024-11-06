def amount(A, S):
    """
    Parameters: A = Amount values, S = target sum
    This function will implement a backtracking algorithm to find
    all unique combinations of numbers that sum up to the target sum (S).
    """
    # Part 1: Sorting
    A.sort()
    result_list = []

    def combination_helper(remaining_sum, list_of_combos, starting_point):
        """
        :param remaining_sum: The sum needed to be achieved
        :param list_of_combos: amounts of selected amounts
        :param starting_point: Position in A set to begin.
        This is a helper function that stores the main backtracking implementation
        for the amount function.
        """
        # Base case
        if remaining_sum == 0:
            # makes a copy and adds to the list of combinations
            result_list.append(list_of_combos)
            return
        # edge case for negative numbers
        elif remaining_sum < 0:
            return

        for i in range(starting_point)






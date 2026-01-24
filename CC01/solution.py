def non_constructible_change(coins):
    sortedCoins = sorted(coins)

    if len(sortedCoins) == 0:
        return 1
    
    if len(sortedCoins) == 1:
        if sortedCoins[0] == 1:
            return 2
        return 1
    
    sum = 0
    target = 1
    for coin in sortedCoins:
        if coin > sum + 1:
            return sum + 1
        else:
            sum += coin

    return sum + 1
    
    
    

    """
    Determines the smallest amount of money (change) that cannot be created
    using any combination of the given coin denominations.

    This function takes an array of positive integers representing coin
    denominations and computes the minimal value that cannot be constructed
    using any subset of the coins.

    The algorithm follows these steps:
    1. Sort the coins array.
    2. Iterate through the coins, keeping track of the maximum constructible
       change so far.
    3. Identify the first gap in constructible change.

    Parameters:
    ----------
    coins : list of int
        A list of positive integers, where each integer represents a coin
        denomination.

    Returns:
    -------
    int
        The smallest amount of money that cannot be constructed using the
        given coin denominations.

    Example:
    --------
    >>> non_constructible_change([1, 2, 5, 10])
    4

    Explanation:
    Given the coins [1, 2, 5, 10], the smallest amount of change that
    cannot be created is 4. This is determined by analyzing combinations
    of the coins and identifying gaps in constructible sums.
    """
    pass

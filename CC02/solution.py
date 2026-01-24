def find_unsorted_subarray(array):
    """
    Finds the shortest subarray that needs to be sorted for the entire
    array to become sorted.

    Args:
        array (list of int): The input array of integers.

    Returns:
        list: A list containing two integers representing the start and
        end indices of the shortest subarray that needs to be sorted.
        If the array is already sorted, returns [-1, -1].

    To Do:
        - Students will implement the logic to find the minimum and maximum
        out-of-order elements and determine the boundaries of the subarray
        that must be sorted.
    """
    start = -1
    end = -1

    pos = 0
    for element in array:
        # see if element is too big or too small
        outOfOrder = is_out_of_order(pos, element, array)

        # if too small, find where it belongs and save that position
        if outOfOrder == 1:
            temp = pos - 1
            while array[temp] > element:
                temp -= 1
            if (start > temp + 1 or start == -1):
                start = temp + 1

        # similarly, if too big, find where it belongs and save that position
        if outOfOrder == 2:
            temp = pos + 1
            while array[temp] < element:
                temp += 1
            if (end < temp - 1  or end == -1):
                end = temp - 1

        pos += 1

    return [start, end]


def is_out_of_order(i, num, array):
    """
    Helper function to determine if an element is out of order in the array.

    Args:
        i (int): The index of the element to check.
        num (int): The element at index i.
        array (list of int): The input array of integers.

    Returns:
        bool: True if the element is out of order, False otherwise.

    This function is a suggestion  to students as a helper function.
    Students are encouraged to implement this function if they find it helpful.
    """
    if (i != 0):
        if (array[i-1] > num):
            return 1
    if (i != len(array) - 1):
        if (array[i+1] < num):
            return 2
    return 0
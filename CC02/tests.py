import unittest
from solution import find_unsorted_subarray





class TestFindUnsortedSubarray(unittest.TestCase):
    # --- Rubric tests ---

    def test_basic_case(self):
        self.assertEqual(
            find_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]),
            [3, 9]
        )

    def test_empty_input(self):
        self.assertEqual(find_unsorted_subarray([]), [-1, -1])

    def test_single_element(self):
        self.assertEqual(find_unsorted_subarray([1]), [-1, -1])

    def test_small_input(self):
        # Small input that is already sorted (your old test_already_sorted)
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4]), [-1, -1])

    def test_unsorted_input(self):
        # Your old test_unsorted_middle, renamed to match rubric
        self.assertEqual(find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]), [1, 5])

    def test_duplicate_values(self):
        # Includes duplicates; subarray [1..3] must be sorted to fix the whole list
        self.assertEqual(find_unsorted_subarray([1, 3, 2, 2, 4]), [1, 3])

    def test_large_input(self):
        # Large case: start sorted, reverse a middle segment
        arr = list(range(2000))
        arr[500:1500] = reversed(arr[500:1500])
        self.assertEqual(find_unsorted_subarray(arr), [500, 1499])


if __name__ == "__main__":
    unittest.main()



# Coding Challenge 2 (CC2)

## Overview

In this coding challenge, you will implement a function that processes a given input and computes a result according to the rules described below.

The goal of CC2 is to reinforce **algorithmic reasoning, careful handling of edge cases, and clarity of thought**, rather than trial-and-error coding.

---



## Smallest Subarray to Sort the Entire Array

### Problem Statement

Write a function that takes an array of at least two integers and returns an array containing the starting and ending indices of the smallest subarray that needs to be sorted in place for the entire input array to be sorted in ascending order.

If the input array is already sorted, the function should return `[-1, -1]`.

---

### Example 1

**Input:**

```python
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
```

**Output:**

```python
[3, 9]
```

---

### Example 2

**Input:**

```python
array = [1, 2, 3, 4]
```

**Output:**

```python
[-1, -1]
```

**Explanation:** The array is already sorted, so no subarray needs to be sorted.

---

### Example 3

**Input:**

```python
array = [2, 6, 4, 8, 10, 9, 15]
```

**Output:**

```python
[1, 5]
```

**Explanation:** Sorting the subarray `[6, 4, 8, 10, 9]` makes the entire array sorted.

---

### Example 4

**Input:**

```python
array = [1]
```

**Output:**

```python
[-1, -1]
```

**Explanation:** Although this is technically a single-element array and not part of the original constraints (at least two integers), we include it as an edge case for completeness.

---

### Example 5

**Input:**

```python
array = [1, 3, 2, 4, 5]
```

**Output:**

```python
[1, 2]
```

**Explanation:** Sorting just `[3, 2]` is enough to make the entire array sorted.

---

### Requirements

- The function should handle arrays of varying lengths but must contain at least two integers.
- Ensure the function can determine if the array is already sorted and handle this case appropriately by returning `[-1, -1]`.

---

### Complexity Goals

- **Expected Runtime Complexity:** `O(n)`
- **Expected Space Complexity:** `O(1)`

---

### Constraints

- The array will contain at least two integers.
- The elements of the array are not guaranteed to be unique.
- The function should aim for optimal time complexity.

---

### Additional Information

- Assume that the input array will contain only integers.
- Focus on writing clean, efficient, and well-documented code.

---

## What to Submit

You must submit **two files**:

1. **`solution.py`**
   - Contains your implementation.
   - Only the required function should be implemented.
   - Do **not** rename functions or change function parameters.

2. **`README.md`**
   - Used to report which tests you passed and which you failed (see below).

No other files will be graded.

---

## How to Approach This Problem

Before writing any code, pause and reason about the problem.

- Think carefully about what the input represents and what the output is expected to capture.
- Consider how the result should evolve as you process the input step by step.
- Ask yourself how your logic behaves for:
  - empty input  
  - very small inputs  
  - inputs that are not in a convenient order  
  - repeated or duplicate values  

A correct solution is not about handling a single example, but about handling **all valid inputs consistently**.

Focus on clarity and correctness before worrying about optimization.

---

## Testing and Self-Check (Required)

You are provided with a test suite in `tests.py`.

Before submitting:
1. Run the tests locally.
2. Identify which tests pass and which fail.

In your **`README.md`**, include a brief self-check section listing your results.

### Required README Format

Your `readme.txt` must list **each test from the provided `tests.py` and the points earned for that test**, using the format below.

**Example format (illustration only):**
Total points for CC2: XX Points

Detailed points for each test:
	1.	test_basic_case: 12
	2.	test_empty_input: 12
	3.	test_single_element: 12
	4.	test_small_input: 12
	5.	test_unsorted_input: 12
	6.	test_duplicate_values: 12
	7.	test_large_input: 28


- Use the **exact test names** from `tests.py`
- This is the **same README format used for both Coding Challenges and Projects**
- Points should reflect whether your solution passed that test  
  (passed = full points for that test, failed = 0 points)

This self-report:
- Helps us understand your reasoning and debugging process
- Encourages honest reflection and disciplined debugging
- Ensures consistency across CCs and Projects

## Grading

Your solution will be evaluated using the following test cases.  
Each test case must pass **completely** to receive credit for that test case.

- `test_basic_case` – 12 points  
- `test_empty_input` – 12 points  
- `test_single_element` – 12 points  
- `test_small_input` – 12 points  
- `test_unsorted_input` – 12 points  
- `test_duplicate_values` – 12 points  
- `test_large_input` – 28 points  

**Total: 100 points**

Partial credit is not awarded within a test case.

---

## Final Notes

- Reason first, code second.
- Use failing tests as feedback, not as a reason to guess.
- Clear thinking will outperform rushed implementation on this challenge.

— **Team 331**

# CC2 – Reasoning Check Questions (Practice Only)

These questions are **not graded** and should **not** be submitted.  
They are provided to help you reason about the problem before (and after) coding.

Focus on *why* an answer is correct, not just *what* the answer is.

---

## Question 1: Meaning of the Output

Suppose the function returns `[i, j]` for a given input array.

In your own words, explain what the indices `i` and `j` represent and why sorting **only** that portion of the array is sufficient to make the entire array sorted.

---

## Question 2: Edge Case Reasoning

For an input array that is already sorted in non-decreasing order (e.g., `[1, 2, 3, 4]`), the function returns `[-1, -1]`.

Explain why returning `[-1, -1]` is a reasonable and meaningful choice for this problem.

---

## Question 3: Duplicate Values

Consider the input:

[1, 3, 2, 2, 4]

Explain why the presence of duplicate values can affect where the unsorted subarray begins or ends, even if the overall issue appears “local.”

---

## Question 4: Large Input Behavior

Why is it important that a solution works correctly for very large inputs, even if it seems to work for small arrays?

Your answer should focus on **logical correctness**, not implementation details.


---

## Suggested Answers (For Self-Check)

Use these answers to reflect on your own reasoning.  
The goal is understanding, not memorization.

---

### Answer to Question 1: Meaning of the Output

The indices `[i, j]` represent the smallest contiguous portion of the array such that **sorting only that subarray** would make the **entire array sorted**.

Elements before index `i` and after index `j` are already in positions that are consistent with the overall sorted order. Any disorder that exists in the array is contained within this interval.

---

### Answer to Question 2: Edge Case Reasoning

If the array is already sorted, there is **no subarray that needs to be fixed**. Returning `[-1, -1]` clearly communicates that no action is required.

This choice avoids ambiguity and provides a consistent signal that the input does not contain any unsorted region.

---

### Answer to Question 3: Duplicate Values

Duplicate values can affect where the unsorted subarray begins or ends because ordering is not determined only by strict inequality.

An element may appear to be in a reasonable position relative to its neighbors but still violate the global ordering when duplicates are considered. As a result, the unsorted region may need to expand to include all values that disrupt the correct ordering.

---

### Answer to Question 4: Large Input Behavior

Testing with large inputs helps confirm that the logic of the solution is **generally correct**, not just correct for small or simple cases.

A solution that works only for small inputs may rely on assumptions that do not hold at scale. Large inputs help expose hidden flaws in reasoning, such as incorrect boundary handling or incomplete conditions.

---

### Final Reflection

If you can explain these answers confidently, you are reasoning about the problem at the right level.  
Strong reasoning leads to simpler, more reliable code.
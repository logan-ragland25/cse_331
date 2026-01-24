# Reasoning Questions: Non-Constructible Change

**Practice Questions - Not Graded**

These questions are designed for **practice only** to help you understand the algorithm, develop critical thinking, and strengthen your reasoning skills. Work through each question thoughtfully to check your understanding. An answer key is provided at the bottom so you can verify your reasoning and learn from any mistakes.

---

## Question 1: Algorithm Logic (Fill in the Blank)

Consider the following partial algorithm for the non-constructible change problem:

```python
def non_constructible_change(coins):
    coins.sort()
    max_constructible = 0
    
    for coin in coins:
        if coin > ___________:
            return ___________
        max_constructible = max_constructible + coin
    
    return ___________
```

**Fill in the three blanks** and **explain your reasoning** for each blank.

---
**Answer Space:**
- Blank 1: max_constructible + 1
- Reasoning: you are seeing if the next value is more than one greater than the current max value

- Blank 2: max_constructible + 1
- Reasoning: if it is greater, you should return it

- Blank 3: max_constructible + 1
- Reasoning: same reasoning as blank 2

---

## Question 2: Why Sorting Matters (Multiple Choice with Explanation)

A student claims that sorting is unnecessary for the non-constructible change problem. They argue: "Since we're just adding up coins, the order shouldn't matter. We can process coins in any order."

**Is this claim correct?** Choose the best answer and explain your reasoning.

A) The claim is correct - sorting is optional because addition is commutative.
B) The claim is incorrect - sorting is necessary because the algorithm relies on processing coins in increasing order.
C) The claim is partially correct - sorting helps but isn't strictly necessary for correctness.
D) The claim is incorrect - sorting is necessary to ensure we don't miss any constructible amounts.

**Your answer:** B

**Your explanation (2-3 sentences):**
If we do not use sorting, we can not easily find the lowest possible value. You will miss gaps that are possible to fill

---

## Question 3: Algorithm Invariant (Short Answer)

The correctness of the non-constructible change algorithm relies on maintaining an important **invariant** (a property that remains true throughout the algorithm's execution).

**State the invariant** that is maintained after processing each coin in the sorted array.

**Your answer:**
It can be used again in every new iteration, but not twice in the same iteration

**Explain why this invariant is crucial for the algorithm's correctness (2-3 sentences):**
It allows you to find every combination of coins, without allowing the creation of unlimited values

---

## Question 4: Edge Case Reasoning (Multiple Choice with Explanation)

Consider the algorithm running on the input `coins = [2, 2, 2, 2]` (four coins, each worth 2).

**What will the algorithm return, and why?**

A) It returns `1` because we cannot construct `1` with only coins of value `2`.
B) It returns `2` because `2` is the smallest coin value.
C) It returns `8` because the sum of all coins is `8`.
D) It returns `9` because `8 + 1 = 9`.

**Your answer:** A

**Trace through the algorithm step-by-step to support your answer:**
- After sorting: [2,2,2,2]
- After processing first coin (2): max_constructible = 1
- After processing second coin (2): max_constructible = 1
- After processing third coin (2): max_constructible = 1
- After processing fourth coin (2): max_constructible = 1
- Final return value: 1

**Your reasoning:**
2 > 1 so one is a gap

---

## Question 5: Complexity and Correctness (Multiple Choice with Explanation)

Consider two different approaches to solve the non-constructible change problem:

**Approach A**: Sort the array, then use a single pass with the greedy algorithm (the approach we learned).

**Approach B**: Use dynamic programming to build a boolean array `dp[i]` where `dp[i] = True` means we can construct amount `i` using a subset of coins.

**Comparing these approaches:**

1. **Time Complexity**: Which approach has better time complexity?
   - A) Approach A: O(n log n) vs Approach B: O(n × S) where S is the sum of all coins
   - B) Approach B: O(n × S) vs Approach A: O(n log n)
   - C) Both have the same time complexity
   - D) It depends on the input

   **Your answer:** A
   **Brief reasoning:** ___________

2. **Space Complexity**: Which approach uses less space?
   - A) Approach A uses O(1) extra space (after sorting), Approach B uses O(S) space
   - B) Approach B uses O(S) space, Approach A uses O(n) space
   - C) Both use the same amount of space
   - D) It depends on the input

   **Your answer:** A
   **Brief reasoning:** you only have to store one more variable for Approach A

3. **Why doesn't the greedy approach (Approach A) work for the classic "coin change" problem (minimum coins needed), but works here?** Explain in 2-3 sentences.

   **Your answer:**
   Approach A finds gaps, the coin change problem wants to use the largest denominations possible.
---

**Note**: These questions are for **practice only** to help you understand the algorithm and prepare for assessments. Answer them thoughtfully to check your understanding, and refer to the answer key at the bottom to verify your reasoning.

---

# Answer Key

## Answer 1: Algorithm Logic (Fill in the Blank)

- **Blank 1**: `max_constructible + 1`
  - **Reasoning**: We check if the current coin is greater than the maximum constructible amount plus 1. If `coin > max_constructible + 1`, then we have a gap and cannot construct `max_constructible + 1`.

- **Blank 2**: `max_constructible + 1`
  - **Reasoning**: When we find a gap (coin > max_constructible + 1), we return `max_constructible + 1` because that's the smallest amount we cannot construct with the coins processed so far.

- **Blank 3**: `max_constructible + 1`
  - **Reasoning**: If we process all coins without finding a gap, we can construct all amounts from 1 to `max_constructible`. Therefore, the smallest non-constructible amount is `max_constructible + 1`.

**Complete code:**
```python
def non_constructible_change(coins):
    coins.sort()
    max_constructible = 0
    
    for coin in coins:
        if coin > max_constructible + 1:
            return max_constructible + 1
        max_constructible = max_constructible + coin
    
    return max_constructible + 1
```

---

## Answer 2: Why Sorting Matters (Multiple Choice with Explanation)

**Correct Answer**: **B** - The claim is incorrect - sorting is necessary because the algorithm relies on processing coins in increasing order.

**Explanation** (key points to look for):
- Sorting is **essential** for the algorithm's correctness, not optional
- The algorithm relies on processing coins in **increasing order** to maintain the invariant that we can construct all amounts from 1 to `max_constructible`
- If we process coins out of order, we might miss gaps or incorrectly update `max_constructible`
- While addition is commutative, the algorithm's logic depends on processing smaller coins first to ensure continuous ranges of constructible amounts

**Example**: If we process `[5, 1, 2]` without sorting:
- After processing 5: max_constructible = 5, but we can't actually construct 1, 2, 3, or 4
- The algorithm would incorrectly think we can construct 1-5, but we can't

---

## Answer 3: Algorithm Invariant (Short Answer)

**Correct Answer**: After processing the first k coins, we can construct all amounts from 1 to `max_constructible` (where `max_constructible` is the sum of the first k coins, assuming no gaps were found).

**More formally**: After processing coins 1 through k in sorted order, if no gaps were found, we can construct every integer from 1 to `max_constructible`, where `max_constructible = coin₁ + coin₂ + ... + coinₖ`.

**Why this invariant is crucial**:
- This invariant allows us to detect gaps efficiently: if the next coin is greater than `max_constructible + 1`, we know we have a gap at `max_constructible + 1`
- It ensures that when we add a coin c where `c ≤ max_constructible + 1`, the new range `[1, max_constructible + c]` is continuous (no gaps)
- Without this invariant, we would need to check all possible subsets, making the algorithm exponential instead of O(n log n)

---

## Answer 4: Edge Case Reasoning (Multiple Choice with Explanation)

**Correct Answer**: **A** - It returns `1` because we cannot construct `1` with only coins of value `2`.

**Step-by-step trace**:
- After sorting: `[2, 2, 2, 2]` (already sorted)
- After processing first coin (2): 
  - Check: `2 > 0 + 1`? Yes! (`2 > 1`)
  - Return: `0 + 1 = 1`
- **Algorithm stops here and returns 1**

**Reasoning**: 
- With `max_constructible = 0` initially, the first coin is `2`
- Since `2 > 0 + 1 = 1`, we immediately detect a gap at 1
- We cannot construct 1 because all coins are worth 2 (or more)
- The algorithm returns 1 without processing the remaining coins

**Key insight**: This edge case demonstrates that if the smallest coin is greater than 1, the answer is always 1.

---

## Answer 5: Complexity and Correctness (Multiple Choice with Explanation)

1. **Time Complexity**: **A** - Approach A: O(n log n) vs Approach B: O(n × S) where S is the sum of all coins
   - **Reasoning**: Approach A sorts in O(n log n) then does one pass in O(n), so O(n log n) total. Approach B uses dynamic programming that checks each amount from 1 to S, and for each amount, considers all n coins, giving O(n × S). Since S can be much larger than n, Approach A is generally better.

2. **Space Complexity**: **A** - Approach A uses O(1) extra space (after sorting), Approach B uses O(S) space
   - **Reasoning**: Approach A only uses a few variables (`max_constructible`, loop variable) beyond the input array, so O(1) extra space. Approach B needs a boolean array of size S (one entry for each amount from 1 to S), so O(S) space.

3. **Why doesn't the greedy approach work for minimum coins needed?**
   - **Key points to look for**:
     - The greedy approach for minimum coins fails because it doesn't always make optimal choices (e.g., with coins [1, 3, 4] and target 6, greedy gives 4+1+1=3 coins, but optimal is 3+3=2 coins)
     - However, for the non-constructible change problem, we're not trying to minimize coins - we're finding the smallest amount we CAN'T construct
     - The greedy approach works here because we maintain a continuous range of constructible amounts, and we can detect gaps efficiently by processing coins in order
     - The problem structure (finding gaps vs. minimizing) is fundamentally different, making greedy appropriate here

**Sample answer**: The greedy approach fails for minimum coins needed because it may choose locally optimal coins that prevent finding the globally optimal solution (e.g., choosing the largest coin first might leave us unable to make change efficiently). However, for non-constructible change, we're not optimizing - we're detecting gaps in constructible amounts. By maintaining a continuous range of constructible amounts and processing coins in order, we can efficiently detect when a gap occurs, making the greedy approach correct for this problem.

---

---

## Notes for Practice

These questions are designed to help you:
- Deepen your understanding of the algorithm logic
- Practice tracing through examples step-by-step
- Understand key concepts like invariants and why sorting matters
- Develop your algorithm analysis skills
- Test your critical thinking about the problem

After working through the questions, compare your answers with the answer key below. Use any differences to identify areas where you need to review the material.

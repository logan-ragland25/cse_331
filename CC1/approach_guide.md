# Problem-Solving Guide: Non-Constructible Change

## How to Approach This Problem

This guide will help you understand the reasoning behind solving the non-constructible change problem step by step.

---

## Step 1: Understand the Problem Deeply

**What are we really asking?**
- We want the **smallest** positive integer that cannot be formed as a sum of any subset of the given coins
- Each coin can be used **at most once** (we're selecting a subset)
- We need to find the first "gap" in the sequence of constructible amounts

**Key Insight**: If we can construct all amounts from `1` to `M`, then the next amount we should check is `M + 1`. If we cannot construct `M + 1`, that's our answer!

---

## Step 2: Build Your Understanding with Examples

### Example Walkthrough: `coins = [1, 2, 5, 10]`

Let's think about what we can construct as we process coins **one by one**:

1. **After processing coin `1` (only this coin processed so far)**:
   - Can construct: `[1]`
   - Maximum constructible: `1`
   - Can we construct `2`? **No** - we haven't processed the `2` coin yet, so we can't construct `2` with just the `1` coin

2. **After processing coin `2` (now we have both `1` and `2`)**:
   - Can construct: `[1, 2, 3]` (using `1`, `2`, or `1+2`)
   - Maximum constructible: `3`
   - Can we construct `4`? **No** (we'd need a `4` coin, or `1+3`, but we don't have `3` as a single coin)

3. **Next coin is `5`**:
   - Since `5 > 3 + 1 = 4`, we **cannot construct `4`**!
   - This means `4` is our answer!

**Wait, why does this work?**

The logic is: If we can construct all amounts from `1` to `M`, and the next coin `c` is greater than `M + 1`, then we have a gap. Specifically, `M + 1` cannot be constructed because:
- We cannot use `c` alone (it's too big: `c > M + 1`)
- We cannot combine `c` with smaller coins (even the largest combination we had was `M`, and `M + c > M + 1` since `c ≥ 1`)
- We cannot use only the previous coins (we already know the maximum we could construct was `M`)

---

## Step 3: Develop the Algorithm

### The Algorithm Logic

1. **Sort the coins** (we need to process them in increasing order)
2. **Track the maximum constructible amount** (`max_constructible`)
3. **Iterate through each coin**:
   - If `coin > max_constructible + 1`, then `max_constructible + 1` is the answer
   - Otherwise, add the coin: `max_constructible += coin`
4. **After processing all coins**, if no gap was found, return `max_constructible + 1`

### Pseudocode

```
function non_constructible_change(coins):
    sort(coins)
    max_constructible = 0
    
    for each coin in coins:
        if coin > max_constructible + 1:
            return max_constructible + 1
        max_constructible = max_constructible + coin
    
    return max_constructible + 1
```

---

## Step 4: Why Does This Algorithm Work?

### The Invariant

**Key Invariant**: After processing the first `k` coins, we can construct all amounts from `1` to `max_constructible`.

### Proof by Induction

**Base Case**: Initially, `max_constructible = 0`. We can construct `0` (by using no coins). For the first coin:
- If the first coin is `1`, then we can construct `[1]`, so `max_constructible = 1` ✓
- If the first coin is greater than `1`, then we cannot construct `1`, so the answer is `1` ✓

**Inductive Step**: Assume we can construct all amounts from `1` to `M` after processing the first `k` coins.

When we see the next coin `c`:
- **Case 1**: `c ≤ M + 1`
  - We can construct all amounts from `1` to `M`
  - By adding coin `c`, we can now construct:
    - All previous amounts: `1` to `M`
    - New amounts: `c`, `c+1`, `c+2`, ..., `c+M`
  - Since `c ≤ M + 1`, these ranges overlap/connect: `M ≥ c - 1`, so `c ≤ M + 1` means we have a continuous range from `1` to `M + c`
  - Therefore, `max_constructible = M + c` ✓

- **Case 2**: `c > M + 1`
  - We can construct `1` to `M`
  - We cannot construct `M + 1` because:
    - We can't use `c` alone (it's too big)
    - We can't combine `c` with previous coins (even the maximum sum was `M`, and `M + c > M + 1`)
    - We can't use only previous coins (maximum was `M`)
  - Therefore, `M + 1` is the answer ✓

---

## Step 5: Complete Example Walkthrough

Let's trace through `coins = [5, 7, 1, 1, 2, 3, 22]`:

**After sorting**: `[1, 1, 2, 3, 5, 7, 22]`

| Step | Coin | Max Constructible Before | Check: coin > max + 1? | Max Constructible After |
|------|------|-------------------------|------------------------|------------------------|
| Start | - | 0 | - | 0 |
| 1 | 1 | 0 | 1 > 0 + 1? No | 1 |
| 2 | 1 | 1 | 1 > 1 + 1? No | 2 |
| 3 | 2 | 2 | 2 > 2 + 1? No | 4 |
| 4 | 3 | 4 | 3 > 4 + 1? No | 7 |
| 5 | 5 | 7 | 5 > 7 + 1? No | 12 |
| 6 | 7 | 12 | 7 > 12 + 1? No | 19 |
| 7 | 22 | 19 | **22 > 19 + 1? YES!** | Return 20 |

**Answer: 20**

Let's verify: Can we construct 20?
- With coins `[1, 1, 2, 3, 5, 7]`, the maximum we can construct is `1 + 1 + 2 + 3 + 5 + 7 = 19`
- To construct 20, we'd need the `22` coin or another coin, but `22` is too big
- Therefore, 20 cannot be constructed ✓

---

## Step 6: Time and Space Complexity Analysis

### Time Complexity: **O(n log n)**
- **Sorting**: O(n log n) where n is the number of coins
- **Single pass through sorted array**: O(n)
- **Overall**: O(n log n) + O(n) = **O(n log n)**

### Space Complexity: **O(1)** (or O(n) if sorting modifies the array in-place)
- **Auxiliary space**: O(1) - we only use a few variables (`max_constructible`)
- **Note**: If the sorting algorithm uses O(1) extra space (like heap sort in-place), then overall space is O(1). If using standard library sort (like Python's Timsort), it may use O(n) space, but we don't count input/output space. In terms of extra space beyond input: **O(1)**

---

## Step 7: Edge Cases to Consider

1. **Empty array**: `[]` → Return `1` (cannot construct 1 with no coins)
2. **Single coin greater than 1**: `[5]` → Return `1` (cannot construct 1)
3. **All coins are the same**: `[2, 2, 2]` → Return `1` (cannot construct 1)
4. **Coins starting from 1**: `[1, 1, 1, 1]` → Can construct `[1, 2, 3, 4]`, return `5`
5. **Unsorted input**: Always sort first!

---

## Step 8: Implementation Tips

1. **Always sort first** - The algorithm depends on processing coins in increasing order
2. **Use descriptive variable names** - `max_constructible` or `current_max` clearly expresses intent
3. **Handle the empty array case** - Initialize `max_constructible = 0`, so if array is empty, return `0 + 1 = 1`
4. **Think about the condition** - The check is `coin > max_constructible + 1`, not `coin > max_constructible`

---

## Step 9: Common Mistakes to Avoid

❌ **Forgetting to sort** - The algorithm only works with sorted input
❌ **Wrong comparison** - Using `coin >= max_constructible + 1` instead of `coin > max_constructible + 1`
❌ **Off-by-one errors** - Remember: if we can construct up to `M`, we check `M + 1`
❌ **Not handling empty array** - Always consider edge cases

---

## Summary: The Key Insight

**If you can construct all amounts from 1 to M, and the next coin c is greater than M + 1, then M + 1 is the smallest non-constructible amount.**

This insight allows us to solve the problem efficiently with a single pass after sorting, making it an O(n log n) time solution with O(1) extra space.

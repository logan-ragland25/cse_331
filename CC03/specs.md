sssssws# Coding Challenge 3 (CC3)

## Overview

In this coding challenge, you will implement an **LRU (Least Recently Used) Cache** data structure.

The goal of CC3 is to reinforce:
- reasoning about **stateful data structures**
- understanding **usage-based eviction policies**
- careful handling of updates, access order, and edge cases

As with previous Coding Challenges, clarity and correctness matter more than cleverness.

---

## Problem Description

## LRU Cache



Implement a class `LRUCache` for a Least Recently Used (LRU) cache. The class should support the following methods:
![alt text](.guides/img/LRUCache.png)

- `insert_key_value_pair(key, value)`: Inserts a key-value pair into the cache.
- `get_value_from_key(key)`: Retrieves the value associated with the provided key.
- `get_most_recent_key()`: Retrieves the most recently used key (either recently inserted or retrieved).

All these methods should run in **O(1)** time complexity.

Additionally, the `LRUCache` class should have a `max_size` attribute, which represents the maximum number of key-value pairs the cache can hold. This value should be passed as an argument when creating an instance of the cache.

When inserting a new key-value pair and the cache has reached its capacity, the least recently used key-value pair should be evicted. Note that if the key already exists, its value should be updated, and this should not trigger an eviction.

If a key that does not exist is queried using `get_value_from_key`, the method should return `None`.

### Method Details

1. **`insert_key_value_pair(key, value)`**:
   - Inserts or updates the given key-value pair in the cache.
   - If the cache is at maximum capacity, it evicts the least recently used key-value pair.

2. **`get_value_from_key(key)`**:
   - Returns the value associated with the given key, or `None` if the key does not exist.

3. **`get_most_recent_key()`**:
   - Returns the most recently used key in the cache.

### Constraints

- The cache should handle keys and values of any data type.
- All operations should have a **O(1)** time complexity.

### Examples

#### Example 1
```python
cache = LRUCache(2)
cache.insert_key_value_pair(1, 'A')
cache.insert_key_value_pair(2, 'B')
print(cache.get_value_from_key(1))  # Output: 'A'
cache.insert_key_value_pair(3, 'C')
print(cache.get_value_from_key(2))  # Output: None (2 was evicted)
print(cache.get_value_from_key(3))  # Output: 'C'
```

#### Example 2
```python
cache = LRUCache(3)
cache.insert_key_value_pair("apple", 10)
cache.insert_key_value_pair("banana", 20)
cache.insert_key_value_pair("cherry", 30)
print(cache.get_most_recent_key())  # Output: 'cherry'
print(cache.get_value_from_key("banana"))  # Output: 20
cache.insert_key_value_pair("date", 40)  # "apple" should be evicted
print(cache.get_value_from_key("apple"))  # Output: None
```

#### Example 3
```python
cache = LRUCache(2)
cache.insert_key_value_pair(1, 100)
cache.insert_key_value_pair(2, 200)
print(cache.get_most_recent_key())  # Output: 2
cache.get_value_from_key(1)  # Accessing key 1
print(cache.get_most_recent_key())  # Output: 1 (key 1 is now the most recent)
cache.insert_key_value_pair(3, 300)  # Evicts key 2
print(cache.get_value_from_key(2))  # Output: None
print(cache.get_value_from_key(3))  # Output: 300
```

---

## What to Submit

You must submit **exactly two files**:

1. **`solution.py`**
   - Must be named **exactly** `solution.py`
   - Implement only what is required
   - Do not change method names or signatures

2. **`readme.txt`**
   - Must be saved as **`readme.txt`**
   - Must follow the required format below

No other files will be graded.

---

## How to Approach This Problem

Before writing code, think carefully about the **behavior** of an LRU cache.

- What does it mean for an item to be “most recently used”?
- How should access (`get`) affect recency?
- What happens when the cache reaches capacity?
- How should updates to existing keys be handled?

A correct solution maintains **consistent ordering** as keys are accessed and updated, and evicts the correct key when capacity is exceeded.

---

## Testing and Self-Check (Required)

You are provided with a test suite in `tests.py`.

Before submitting:
1. Run the tests locally.
2. Identify which tests your solution passes and fails.

You must report this in your `readme.txt` using the required format below.

---

## Required README Format

Your `readme.txt` must list **each test from `tests.py` and the points earned for that test**, using the same format used for **both Coding Challenges and Projects**.

**Example format (illustration only):**
```
Total points for CC3: XX Points

Detailed points for each test:
1) test_basic_operations: 20
2) test_basic_operations_2: 20
3) test_most_recent_key: 20
4) test_eviction: 20
5) test_update_value: 20
```

- Use the **exact test names** from `tests.py`
- Passed test = full points for that test
- Failed test = 0 points for that test

This self-report:
- Helps us understand your reasoning and debugging process
- Encourages honest reflection and disciplined debugging

---

## Grading

Your solution will be evaluated using the following test cases.  
Each test case must pass **completely** to receive credit for that test case.

- `test_basic_operations` – 20 points  
- `test_basic_operations_2` – 20 points  
- `test_most_recent_key` – 20 points  
- `test_eviction` – 20 points  
- `test_update_value` – 20 points  

**Total: 100 points**

Partial credit is not awarded within a test case.

---

## Final Notes

- Reason about behavior before coding.
- Use the tests as feedback, not as a guessing tool.
- Consistency across CCs and Projects matters.

— **Team 331**

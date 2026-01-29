# CC3 – Reasoning Check Questions (Practice Only)

These questions are **not graded** and should **not** be submitted.  
They are provided to help you reason about the problem before (and after) coding.

Focus on *why* certain behaviors are required, not on memorizing steps or syntax.

---

## Question 1: Meaning of “Most Recently Used”

In your own words, explain what it means for a key to be **most recently used** in an LRU cache.

Your explanation should address:
- what actions make a key “recent”
- how recency can change over time
- why recency matters when the cache is full

### Suggested Answer

A key is considered **most recently used** if it was the most recent key to be either accessed or updated.  
Recency is not fixed — it changes every time a key is read or written.

Recency matters because when the cache is full, the cache must decide which key to evict. The LRU policy requires evicting the key that has been unused for the longest time, which makes correct tracking of recency essential.

---

## Question 2: Access vs. Insertion

Consider the difference between:
- inserting a new key into the cache, and  
- accessing an existing key using `get_value_from_key`.

Explain how each of these operations should affect the internal ordering of the cache, and **why treating them differently would lead to incorrect behavior**.

### Suggested Answer

Both inserting a new key and accessing an existing key should update recency and move that key to the “most recent” position.

If access did not update recency, a frequently used key could be incorrectly evicted simply because it was not recently inserted. Treating insertion and access differently would violate the core idea of “use-based” eviction.

---

## Question 3: Eviction Reasoning

Suppose the cache has reached its maximum capacity and a new key is inserted.

Explain:
- how the cache determines *which* key to evict
- why evicting any other key would violate the LRU policy

### Suggested Answer

When the cache is full, the key that has been **least recently used** must be evicted. This is the key that has gone the longest time without being accessed or updated.

Evicting any other key would ignore actual usage patterns and break the guarantee that frequently used data remains available, which defeats the purpose of an LRU cache.

---

## Question 4: Updating an Existing Key

If a key already exists in the cache and its value is updated:

- Should this key be considered recently used?
- Why or why not?

Explain how failing to handle this case correctly could cause subtle bugs.

### Suggested Answer

Yes, updating an existing key should mark it as **recently used**, because an update is a form of access.

If updates do not affect recency, a key could be actively modified yet still treated as “old” and evicted too soon. This can lead to subtle bugs where the cache appears to work for simple cases but fails under more realistic usage patterns.

---

## Question 5: Consistency Over Time

An LRU cache is a **stateful** data structure.

Explain what it means for the cache’s behavior to be consistent over a **sequence** of operations, and why reasoning about sequences is more important than reasoning about single operations.

### Suggested Answer

Consistency over time means that the cache’s internal state (ordering and stored values) correctly reflects the entire history of operations, not just the most recent one.

Reasoning about sequences is important because many errors only appear after multiple operations interact. A cache might behave correctly for a single insert or get, but fail when several inserts, accesses, and evictions occur in combination.

---

## Final Reflection

If you can explain these answers clearly, you are reasoning about the problem at the right level.

Strong reasoning → simpler code → fewer bugs.
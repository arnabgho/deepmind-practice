# 2. LRU Cache

**Difficulty**: Hard
**Category**: Design, Hash Map, Double Linked List
**Similar to**: LeetCode 146

---

## Problem Statement

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`. This operation marks the key as **recently used**.
- `void put(int key, int value)` Update the value of the `key` if it exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity`, **evict** the least recently used key.

**The functions `get` and `put` must each run in `O(1)` average time complexity.**

---

## Examples

### Example 1:
```
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1, cache is {2=2, 1=1} (1 is most recent)
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {3=3, 4=4}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

---

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`

---

## Follow-up Questions

1. Can you implement LFU (Least Frequently Used) cache?
2. How would you implement this in a distributed system?
3. What if we need to support thread-safe operations?

---

## Approach Hints

<details>
<summary>Hint 1 - Data Structure Choice</summary>

We need:
- O(1) lookup → Hash Map
- O(1) insertion/deletion → Doubly Linked List
- Track "recently used" order → DLL maintains access order

Combine: Hash Map + Doubly Linked List
</details>

<details>
<summary>Hint 2 - Double Linked List Structure</summary>

```
Dummy Head ↔ [MRU] ↔ ... ↔ [LRU] ↔ Dummy Tail
```

- Most recently used: right after head
- Least recently used: right before tail
- Dummy nodes simplify edge cases

Operations:
- **Get**: Move node to front (after head)
- **Put (existing)**: Update value, move to front
- **Put (new, not full)**: Add to front
- **Put (new, full)**: Remove tail node, add to front
</details>

<details>
<summary>Hint 3 - Implementation Details</summary>

**Node class:**
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
```

**Helper methods needed:**
- `_remove(node)`: Remove node from DLL
- `_add_to_front(node)`: Add node right after head
- `_move_to_front(node)`: Convenience method
- `_remove_lru()`: Remove node before tail

**Hash Map:**
```python
self.cache = {}  # key -> Node
```
</details>

---

## Key Concepts to Review

1. **Double Linked List**
   - Why not single? Need O(1) deletion
   - Dummy head/tail to avoid null checks
   - Insert/delete operations

2. **Hash Map**
   - Key to node mapping
   - O(1) average lookup

3. **Cache Eviction Policies**
   - LRU: Least Recently Used
   - LFU: Least Frequently Used
   - FIFO: First In First Out

---

## Test Cases to Consider

1. Capacity 1: Continuous evictions
2. Capacity equals number of operations: No evictions
3. Get on non-existent key
4. Put updates existing key (no eviction)
5. Multiple gets on same key
6. Alternating get/put
7. Fill to capacity, then add one more
8. Get after eviction

---

## Common Mistakes

1. ❌ Forgetting to update LRU order on `get`
2. ❌ Not using dummy nodes (complex null handling)
3. ❌ Hash map stores values instead of nodes (can't do O(1) reordering)
4. ❌ Single linked list (O(n) to find previous node)
5. ❌ Not updating key in node (needed when evicting from map)

---

## Related Problems

- LFU Cache (Hard)
- Design HashMap (Easy)
- Design Linked List (Medium)
- All O(1) Data Structure (Hard)

# 6. Design Skip List

**Difficulty**: Hard
**Category**: Design, Linked List, Probabilistic Data Structure
**Similar to**: LeetCode 1206

---

## Problem Statement

Design a **Skip List**. A skip list is a data structure that takes O(log n) time to add, erase and search. (See: https://en.wikipedia.org/wiki/Skip_list)

A skip list is built in several levels. The bottom level is an ordinary ordered linked list. Each higher level acts as an "express lane" for the lists below, where an element in level `i` appears in level `i+1` with some fixed probability `p` (typically 0.5).

Implement the `Skiplist` class:

- `Skiplist()` Initializes the object of the skiplist.
- `bool search(int target)` Returns `true` if the integer `target` exists in the Skiplist or `false` otherwise.
- `void add(int num)` Inserts the value `num` into the SkipList.
- `bool erase(int num)` Removes the value `num` from the Skiplist and returns `true`. If `num` does not exist in the Skiplist, return `false`.

Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

---

## Examples

### Example 1:
```
Input:
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]

Output:
[null, null, null, null, false, null, true, false, true, false]

Explanation:
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // return False
skiplist.add(4);
skiplist.search(1);   // return True
skiplist.erase(0);    // return False, 0 is not in skiplist
skiplist.erase(1);    // return True
skiplist.search(1);   // return False, 1 has already been erased
```

---

## Constraints

- `0 <= num, target <= 2 * 10^4`
- At most `5 * 10^4` calls will be made to `search`, `add`, and `erase`

---

## Follow-up Questions

1. How would you implement this without using random number generation?
2. What if we want to support range queries?
3. How would you make this thread-safe?
4. Compare with balanced BST (AVL, Red-Black tree) - pros/cons?

---

## Approach Hints

<details>
<summary>Hint 1 - Skip List Structure</summary>

**Multi-level linked list:**
```
Level 3:  head --------------------------------> None
Level 2:  head ---------> 3 --------------------> None
Level 1:  head -----> 2 -> 3 ---------> 7 -------> None
Level 0:  head -> 1 -> 2 -> 3 -> 5 -> 7 -> 9 -> None
```

**Key properties:**
- Level 0: Contains all elements (sorted)
- Higher levels: "Express lanes" with fewer elements
- Vertical connections: Same element at different levels
- Probability: Each element promoted to next level with p=0.5

**Node structure:**
```python
class Node:
    def __init__(self, val=-1, levels=1):
        self.val = val
        self.forward = [None] * levels  # forward[i] = next node at level i
```
</details>

<details>
<summary>Hint 2 - Random Level Generation</summary>

**Determine how many levels a new node gets:**
```python
def random_level(self):
    level = 1
    while random.random() < 0.5 and level < MAX_LEVEL:
        level += 1
    return level
```

Expected number of levels: O(log n)

**MAX_LEVEL**: Typically 16 or 32
- log₂(10^4) ≈ 13, so 16 is safe for this problem
</details>

<details>
<summary>Hint 3 - Search Operation</summary>

**Search for target:**
1. Start at top-left (highest level of head)
2. Move right while `next.val < target`
3. Move down one level
4. Repeat until level 0
5. Check if `current.next.val == target`

```python
def search(self, target):
    current = self.head
    for level in range(self.max_level - 1, -1, -1):
        while current.forward[level] and current.forward[level].val < target:
            current = current.forward[level]

    current = current.forward[0]
    return current and current.val == target
```

Time: O(log n) expected
</details>

<details>
<summary>Hint 4 - Add Operation</summary>

**Insert num:**
1. Find insertion position at each level (like search)
2. Determine random level for new node
3. Create node with that many levels
4. Update forward pointers at each level

```python
def add(self, num):
    update = [None] * self.max_level
    current = self.head

    # Find insertion position at each level
    for level in range(self.max_level - 1, -1, -1):
        while current.forward[level] and current.forward[level].val < num:
            current = current.forward[level]
        update[level] = current

    # Create new node
    new_level = self.random_level()
    new_node = Node(num, new_level)

    # Insert at each level
    for level in range(new_level):
        new_node.forward[level] = update[level].forward[level]
        update[level].forward[level] = new_node
```

Time: O(log n) expected
</details>

<details>
<summary>Hint 5 - Erase Operation</summary>

**Remove num:**
1. Find node at each level (like search)
2. If found, update forward pointers to bypass it
3. Return True if found, False otherwise

**Handle duplicates:** Only remove one instance

```python
def erase(self, num):
    update = [None] * self.max_level
    current = self.head

    # Find node at each level
    for level in range(self.max_level - 1, -1, -1):
        while current.forward[level] and current.forward[level].val < num:
            current = current.forward[level]
        update[level] = current

    # Check if found
    current = current.forward[0]
    if not current or current.val != num:
        return False

    # Remove from each level
    for level in range(len(current.forward)):
        if update[level].forward[level] != current:
            break
        update[level].forward[level] = current.forward[level]

    return True
```

Time: O(log n) expected
</details>

---

## Key Concepts to Review

1. **Probabilistic Data Structures**
   - Use randomization for efficiency
   - Expected vs worst-case complexity
   - Simple to implement vs balanced trees

2. **Skip List Properties**
   - Space: O(n) expected
   - Search/Insert/Delete: O(log n) expected
   - Simple to implement (no complex rotations like AVL)

3. **Comparison to Other Structures**
   - **vs Array**: Faster insertion/deletion
   - **vs Linked List**: Faster search
   - **vs BST**: Simpler (no balancing), probabilistic
   - **vs Hash Map**: Maintains order, range queries

---

## Test Cases to Consider

1. Empty skip list operations
2. Add single element, then search
3. Add multiple elements, verify sorted
4. Search for non-existent element
5. Erase non-existent element
6. Add duplicates, erase one instance
7. Add in ascending order
8. Add in descending order
9. Add in random order
10. Large number of operations (5×10^4)

---

## Common Mistakes

1. ❌ Not handling duplicates correctly
2. ❌ Off-by-one errors in level iteration
3. ❌ Not maintaining sorted order
4. ❌ Forgetting to update pointers at all levels
5. ❌ Not using sentinel head node
6. ❌ Wrong direction in search (should be right then down)

---

## Implementation Tips

**Sentinel head node:**
- Value = -infinity (or -1)
- All levels point to head initially
- Simplifies edge cases

**Level array vs individual pointers:**
- Array: `forward[i]` = next at level i
- More cache-friendly
- Easier to implement

**Random level cap:**
- Prevents excessive height
- log₂(n) + constant is typical

---

## Complexity Analysis

**Time Complexity (expected):**
- Search: O(log n)
- Add: O(log n)
- Erase: O(log n)

**Space Complexity:**
- O(n) expected
- Each element has expected 2 levels (geometric series sum)

**Why O(log n)?**
- Expected height: O(log n)
- At each level, expected number of steps: O(1)
- Total steps: O(log n) levels × O(1) steps = O(log n)

---

## Skip List vs Other Data Structures

| Operation | Skip List | Balanced BST | Hash Map | Sorted Array |
|-----------|-----------|--------------|----------|--------------|
| Search | O(log n)* | O(log n) | O(1)* | O(log n) |
| Insert | O(log n)* | O(log n) | O(1)* | O(n) |
| Delete | O(log n)* | O(log n) | O(1)* | O(n) |
| Range Query | O(log n + k) | O(log n + k) | ❌ | O(log n + k) |
| Ordered | ✓ | ✓ | ❌ | ✓ |
| Implementation | Simple | Complex | Simple | Simple |

\* Expected time

---

## Related Problems

- Design Linked List (Medium)
- LRU Cache (Medium)
- Design HashMap (Easy)
- Implement Trie (Medium)

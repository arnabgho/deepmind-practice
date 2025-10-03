# 12. Flatten Nested List Iterator

**Difficulty**: Hard
**Category**: Design, Stack, Iterator Pattern
**Similar to**: LeetCode 341

---

## Problem Statement

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:

- `NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the nested list `nestedList`.
- `int next()` Returns the next integer in the nested list.
- `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

Your code will be tested with the following pseudocode:

```
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
```

If `res` matches the expected flattened list, then your code will be judged as correct.

---

## Examples

### Example 1:
```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].
```

### Example 2:
```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6].
```

### Example 3:
```
Input: nestedList = []
Output: []
```

---

## Constraints

- `1 <= nestedList.length <= 500`
- The values of the integers in the nested list are in the range `[-10^6, 10^6]`

---

## Follow-up Questions

1. What if we need to support a `previous()` method?
2. How would you modify this to iterate in reverse order?
3. Can you implement this without flattening the entire list upfront?
4. What if the nested list is extremely large and we want lazy evaluation?

---

## Approach Hints

<details>
<summary>Hint 1 - Flatten Everything Upfront</summary>

**Easiest approach**: Flatten the entire nested list in constructor.

```python
class NestedIterator:
    def __init__(self, nestedList):
        self.flat_list = []
        self.flatten(nestedList)
        self.index = 0

    def flatten(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                self.flat_list.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self):
        val = self.flat_list[self.index]
        self.index += 1
        return val

    def hasNext(self):
        return self.index < len(self.flat_list)
```

**Pros**: Simple, fast iteration
**Cons**: O(n) space upfront, not lazy

Time: Constructor O(n), next() O(1), hasNext() O(1)
Space: O(n) for flattened list + O(d) recursion depth
</details>

<details>
<summary>Hint 2 - Stack-Based Lazy Evaluation (Optimal)</summary>

**Better approach**: Use a stack, flatten on-demand (lazy evaluation).

**Key Insights**:
1. Store items in reverse order on stack (to maintain left-to-right order)
2. In `hasNext()`, ensure top of stack is an integer
3. If top is a list, flatten it by pushing its elements

**Algorithm**:
```python
class NestedIterator:
    def __init__(self, nestedList):
        # Store in reverse to maintain order when popping
        self.stack = nestedList[::-1]

    def next(self):
        # hasNext guarantees top is integer
        return self.stack.pop().getInteger()

    def hasNext(self):
        # Make sure top of stack is an integer
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            # Top is a list, flatten it
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False
```

**Example walkthrough**: `[[1,1],2,[1,1]]`
```
Initial:  stack = [[1,1], 2, [1,1]] (reversed)

hasNext():
  top = [1,1] (list) → pop, extend [1,1] reversed
  stack = [2, [1,1], 1, 1]
  top = 1 (int) → return True

next(): return 1
  stack = [2, [1,1], 1]

hasNext():
  top = 1 (int) → return True

next(): return 1
  stack = [2, [1,1]]

hasNext():
  top = 2 (int) → return True

next(): return 2
  stack = [[1,1]]

hasNext():
  top = [1,1] (list) → pop, extend
  stack = [1, 1]
  top = 1 (int) → return True

... and so on
```

Time:
  - Constructor: O(1)
  - next(): O(1) amortized
  - hasNext(): O(1) amortized (each element processed once)
Space: O(n) worst case for stack
</details>

<details>
<summary>Hint 3 - Stack with Index Tracking</summary>

Alternative: Store (list, index) pairs on stack:
- Track current position in each list
- More complex but avoids reversing

```python
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = [(nestedList, 0)]

    def next(self):
        self.make_next_available()
        nested_list, i = self.stack[-1]
        self.stack[-1] = (nested_list, i + 1)
        return nested_list[i].getInteger()

    def hasNext(self):
        self.make_next_available()
        return len(self.stack) > 0

    def make_next_available(self):
        while self.stack:
            nested_list, i = self.stack[-1]
            if i == len(nested_list):
                self.stack.pop()
            elif nested_list[i].isInteger():
                return
            else:
                self.stack[-1] = (nested_list, i + 1)
                self.stack.append((nested_list[i].getList(), 0))
```

Slightly more complex but avoids list reversal.
</details>

---

## Key Concepts to Review

1. **Iterator Pattern**
   - Lazy vs eager evaluation
   - hasNext() + next() contract
   - State management

2. **Stack for Tree/Nested Traversal**
   - DFS simulation with explicit stack
   - Maintaining order with reversing

3. **NestedInteger Interface**
   ```python
   class NestedInteger:
       def isInteger(self) -> bool
       def getInteger(self) -> int
       def getList(self) -> List[NestedInteger]
   ```

4. **Amortized Complexity**
   - Each element processed at most once
   - Cost spread across multiple calls

---

## Test Cases to Consider

1. Empty list: `[]`
2. All integers: `[1,2,3]`
3. Single nested: `[[1,2,3]]`
4. Deeply nested: `[[[[[1]]]]]`
5. Mixed: `[[1,1],2,[1,1]]`
6. Empty nested lists: `[[],1,[],2,[]]`
7. Single integer: `[1]`
8. Complex nesting: `[1,[4,[6,[8,[10]]]]]`
9. Multiple top-level items: `[[1],2,[3,4],5,[6,[7,8]]]`
10. Large flat list (500 integers)

---

## Common Mistakes

1. ❌ Not reversing when pushing to stack (wrong order)
2. ❌ Doing work in `next()` instead of `hasNext()` (violates contract)
3. ❌ Not handling empty nested lists: `[[],[],1]`
4. ❌ Flattening in constructor when lazy evaluation is preferred
5. ❌ Stack overflow with deep recursion (use iterative approach)
6. ❌ Not maintaining state properly between calls
7. ❌ Calling `getInteger()` on a list or `getList()` on integer (check first)
8. ❌ Modifying the input nested list

---

## Complexity Analysis

### Stack-Based Lazy Approach (Optimal):
- **Time Complexity**:
  - Constructor: O(1) - just store reference
  - next(): O(1) amortized
  - hasNext(): O(1) amortized
  - Overall: O(n) total for all operations (each element processed once)

- **Space Complexity**: O(n + d)
  - O(n) for stack in worst case (all elements on stack)
  - O(d) for maximum nesting depth
  - Total: O(n)

### Flatten Upfront Approach:
- **Time Complexity**:
  - Constructor: O(n) - flatten everything
  - next(): O(1)
  - hasNext(): O(1)

- **Space Complexity**: O(n + d)
  - O(n) for flattened list
  - O(d) for recursion stack during flattening

---

## Related Problems

- Flatten 2D Vector (Medium)
- Zigzag Iterator (Medium)
- Peeking Iterator (Medium)
- Binary Search Tree Iterator (Medium)
- Implement Iterator for Combination (Medium)
- Design Compressed String Iterator (Easy)
- Flatten a Multilevel Doubly Linked List (Medium)

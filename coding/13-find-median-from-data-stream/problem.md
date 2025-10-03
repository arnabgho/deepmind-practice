# 13. Find Median from Data Stream

**Difficulty**: Hard
**Category**: Design, Heap, Two Pointers
**Similar to**: LeetCode 295

---

## Problem Statement

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

---

## Examples

### Example 1:
```
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

---

## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `findMedian`
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`

---

## Follow-up Questions

1. If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize it?
2. If 99% of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize it?
3. Can you support deletion of numbers as well?
4. What if we need to find the k-th smallest element instead of median?

---

## Approach Hints

<details>
<summary>Hint 1 - Brute Force</summary>

Maintain a sorted list:
- `addNum()`: Insert in sorted position using binary search
- `findMedian()`: Return middle element(s)

Time: O(n) per insertion (shifting elements), O(1) for median
Space: O(n)

Not optimal for frequent insertions.
</details>

<details>
<summary>Hint 2 - Two Heaps (Optimal)</summary>

**Key Insight**: Split numbers into two halves:
- Lower half (max heap): Stores smaller half of numbers
- Upper half (min heap): Stores larger half of numbers

**Invariants**:
1. Max heap size ≥ min heap size (difference ≤ 1)
2. Every element in max heap ≤ every element in min heap
3. Median is either:
   - max_heap.top (if odd total count)
   - (max_heap.top + min_heap.top) / 2 (if even)

**Structure**:
```
Numbers:     [1, 2, 3, 4, 5, 6, 7]
              ↓  ↓  ↓     ↓  ↓  ↓
Max Heap:    [1, 2, 3, 4]  (stores as negatives in Python)
Min Heap:       [5, 6, 7]
Median:         4 (top of max heap)

Numbers:     [1, 2, 3, 4, 5, 6]
              ↓  ↓  ↓     ↓  ↓  ↓
Max Heap:    [1, 2, 3]
Min Heap:       [4, 5, 6]
Median:         (3 + 4) / 2 = 3.5
```

**Algorithm**:
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # lower half (negate for max heap)
        self.min_heap = []  # upper half

    def addNum(self, num):
        # Add to max heap first
        heapq.heappush(self.max_heap, -num)

        # Balance: ensure max_heap top <= min_heap top
        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Balance sizes: max_heap can have at most 1 more element
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
```

Time: addNum() O(log n), findMedian() O(1)
Space: O(n)
</details>

<details>
<summary>Hint 3 - Follow-up: Range [0, 100]</summary>

Use counting array (bucket sort approach):
```python
class MedianFinder:
    def __init__(self):
        self.count = [0] * 101  # for range [0, 100]
        self.total = 0

    def addNum(self, num):
        self.count[num] += 1
        self.total += 1

    def findMedian(self):
        mid = (self.total + 1) // 2
        cumulative = 0
        for i in range(101):
            cumulative += self.count[i]
            if cumulative >= mid:
                if self.total % 2 == 1:
                    return float(i)
                else:
                    # Find second middle
                    if cumulative > mid:
                        return float(i)
                    # Find next non-zero
                    for j in range(i+1, 101):
                        if self.count[j] > 0:
                            return (i + j) / 2.0
```

Time: addNum() O(1), findMedian() O(100) = O(1)
Space: O(100) = O(1)
</details>

<details>
<summary>Hint 4 - Multiset/Tree Approach</summary>

Use balanced BST (like TreeMap in Java, SortedList in Python):
- Maintain sorted order
- Track middle pointer(s)

Time: addNum() O(log n), findMedian() O(1)
Space: O(n)

Language dependent implementation.
</details>

---

## Key Concepts to Review

1. **Heap (Priority Queue)**
   - Min heap vs max heap
   - heappush, heappop operations: O(log n)
   - Python heapq (min heap by default)
   - Simulating max heap with negation

2. **Median Definition**
   - Odd count: middle element
   - Even count: average of two middle elements

3. **Data Structure Design**
   - Maintaining invariants
   - Balancing operations
   - Trade-offs: time vs space

4. **Amortized Analysis**
   - Cost per operation over sequence

---

## Test Cases to Consider

1. Single element: `addNum(1)`, `findMedian()` → 1.0
2. Two elements: `addNum(1)`, `addNum(2)`, `findMedian()` → 1.5
3. Odd count: `[1,2,3]` → 2.0
4. Even count: `[1,2,3,4]` → 2.5
5. All same: `[5,5,5,5]` → 5.0
6. Descending order: `addNum(3)`, `addNum(2)`, `addNum(1)`
7. Ascending order: `addNum(1)`, `addNum(2)`, `addNum(3)`
8. Negative numbers: `[-1, -2, -3, 0, 1]`
9. Large range: `[-10^5, 10^5]`
10. Maximum operations (5 * 10^4 calls)
11. Alternating large and small: `[1, 100, 2, 99, 3, 98]`

---

## Common Mistakes

1. ❌ Using only one heap (doesn't give O(1) median access)
2. ❌ Not handling heap size balancing properly
3. ❌ Forgetting to negate when using max heap in Python
4. ❌ Not checking which heap to return from based on size
5. ❌ Integer division instead of float for median
6. ❌ Not handling edge cases (single element, two elements)
7. ❌ Comparing heap sizes incorrectly in findMedian()
8. ❌ Adding to wrong heap initially
9. ❌ Rebalancing heaps on every operation (unnecessary)

---

## Complexity Analysis

### Two Heaps Approach (Optimal):
- **Time Complexity**:
  - addNum(): O(log n)
    - Heap push: O(log n)
    - Heap pop (if needed): O(log n)
    - Constant number of operations
  - findMedian(): O(1)
    - Just access heap tops

- **Space Complexity**: O(n)
  - Store all n numbers in heaps

### Sorted Array Approach:
- **Time Complexity**:
  - addNum(): O(n)
    - Binary search: O(log n)
    - Insertion shift: O(n)
  - findMedian(): O(1)

- **Space Complexity**: O(n)

### Counting Array (for range [0, 100]):
- **Time Complexity**:
  - addNum(): O(1)
  - findMedian(): O(100) = O(1)

- **Space Complexity**: O(1) - fixed 101 elements

---

## Related Problems

- Sliding Window Median (Hard)
- Find Median from Large File (System Design)
- Kth Largest Element in a Stream (Easy)
- IPO (Hard)
- Find the Kth Smallest Sum of a Matrix With Sorted Rows (Hard)
- Median of Two Sorted Arrays (Hard)
- Data Stream as Disjoint Intervals (Hard)
- Moving Average from Data Stream (Easy)

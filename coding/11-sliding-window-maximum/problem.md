# 11. Sliding Window Maximum

**Difficulty**: Hard
**Category**: Sliding Window, Monotonic Deque, Queue
**Similar to**: LeetCode 239

---

## Problem Statement

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

---

## Examples

### Example 1:
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```

### Example 3:
```
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

### Example 4:
```
Input: nums = [9,11], k = 2
Output: [11]
```

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

---

## Follow-up Questions

1. Can you solve it in linear time?
2. What if we need the minimum instead of maximum?
3. How would you handle updates to the array dynamically?
4. Can you solve this without using extra space proportional to k?

---

## Approach Hints

<details>
<summary>Hint 1 - Brute Force</summary>

For each window, find the maximum:
```python
result = []
for i in range(len(nums) - k + 1):
    window_max = max(nums[i:i+k])
    result.append(window_max)
return result
```

Time: O(n*k) - for each window, scan k elements
Space: O(1) excluding output
</details>

<details>
<summary>Hint 2 - Max Heap / Priority Queue</summary>

Use a max heap to track maximum in current window:
1. Add first k elements to heap with their indices
2. For each new element:
   - Add to heap
   - Remove elements outside window (check index)
   - Current max is heap top

**Problem**: Heap doesn't efficiently remove elements outside window
- Need to store (value, index) pairs
- Check if top element is still in window

Time: O(n log k) - each insertion/deletion is O(log k)
Space: O(k) for heap
</details>

<details>
<summary>Hint 3 - Monotonic Deque (Optimal)</summary>

**Key Insight**: We only care about elements that could potentially be the maximum.

**Monotonic Decreasing Deque**:
- Store indices (not values) in deque
- Maintain decreasing order of values
- Front of deque is always the maximum

**Why it works**:
- If we see a larger element, all smaller elements before it are useless
- Remove them from back of deque
- Remove elements outside window from front

**Algorithm**:
```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()  # stores indices
    result = []

    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (they're useless)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Add to result starting from first window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

**Deque State Example** (nums = [1,3,-1,-3,5,3,6,7], k = 3):
```
i=0: dq=[0]           nums[0]=1
i=1: dq=[1]           nums[1]=3 (removed 0, added 1)
i=2: dq=[1,2]         nums[1]=3, nums[2]=-1 → max=3
i=3: dq=[1,2,3]       nums[1]=3 → max=3
i=4: dq=[4]           nums[4]=5 (removed all, added 4) → max=5
i=5: dq=[4,5]         nums[4]=5, nums[5]=3 → max=5
i=6: dq=[6]           nums[6]=6 → max=6
i=7: dq=[7]           nums[7]=7 → max=7
```

Time: O(n) - each element added and removed at most once
Space: O(k) for deque
</details>

<details>
<summary>Hint 4 - Block/Bucket Approach</summary>

Divide array into blocks of size k:
- Compute left max for each block (left to right)
- Compute right max for each block (right to left)
- Window max = max(right[window_start], left[window_end])

Time: O(n)
Space: O(n)

Less practical but interesting approach.
</details>

---

## Key Concepts to Review

1. **Monotonic Deque**
   - Maintaining monotonic property (increasing/decreasing)
   - When to add/remove elements
   - Storing indices vs values

2. **Deque Operations**
   - appendleft() / append() - O(1)
   - popleft() / pop() - O(1)
   - Access front/back - O(1)

3. **Amortized Analysis**
   - Each element added once, removed once
   - Total operations: O(n)

4. **Sliding Window Pattern**
   - Fixed size windows
   - Maintaining invariants as window slides

---

## Test Cases to Consider

1. Single element: `nums = [1], k = 1`
2. Window size equals array: `nums = [1,2,3], k = 3`
3. Strictly increasing: `nums = [1,2,3,4,5], k = 3`
4. Strictly decreasing: `nums = [5,4,3,2,1], k = 3`
5. All same elements: `nums = [7,7,7,7], k = 2`
6. Negative numbers: `nums = [-1,-2,-3], k = 2`
7. Alternating high/low: `nums = [1,100,1,100,1], k = 2`
8. Maximum at beginning: `nums = [10,1,2,3], k = 3`
9. Maximum at end: `nums = [1,2,3,10], k = 3`
10. Large array (10^5 elements)

---

## Common Mistakes

1. ❌ Storing values instead of indices in deque (can't check window bounds)
2. ❌ Wrong window boundary check (off-by-one errors)
3. ❌ Maintaining increasing instead of decreasing deque
4. ❌ Not removing elements outside window from front
5. ❌ Starting to add results too early (before first complete window)
6. ❌ Using heap without handling stale elements properly
7. ❌ Comparing indices instead of values when maintaining monotonic property
8. ❌ Not handling edge cases (k=1, k=n)

---

## Complexity Analysis

### Monotonic Deque (Optimal):
- **Time Complexity**: O(n)
  - Each element is added to deque exactly once: O(n)
  - Each element is removed from deque at most once: O(n)
  - All deque operations are O(1)
  - Total: O(n)

- **Space Complexity**: O(k)
  - Deque stores at most k elements
  - Output array not counted: O(n-k+1)

### Max Heap Approach:
- **Time Complexity**: O(n log k)
  - Each insertion: O(log k)
  - n insertions total
  - Heap size maintained at ~k

- **Space Complexity**: O(k)
  - Heap size

### Brute Force:
- **Time Complexity**: O(n*k)
  - n-k+1 windows
  - Each window: O(k) to find max

- **Space Complexity**: O(1)

---

## Related Problems

- Sliding Window Median (Hard)
- Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (Medium)
- Shortest Subarray with Sum at Least K (Hard)
- Jump Game VI (Medium)
- Constrained Subsequence Sum (Hard)
- Minimum Window Substring (Hard)
- Max Sum of Rectangle No Larger Than K (Hard)

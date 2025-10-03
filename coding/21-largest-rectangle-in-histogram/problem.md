# 21. Largest Rectangle in Histogram

**Difficulty**: Hard
**Category**: Monotonic Stack, Array
**Similar to**: LeetCode 84

---

## Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

---

## Examples

### Example 1:
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
       6
     5 █
     █ █
     █ █   3
 2   █ █ 2 █
 █ 1 █ █ █ █
```

### Example 2:
```
Input: heights = [2,4]
Output: 4
```

### Example 3:
```
Input: heights = [1]
Output: 1
```

### Example 4:
```
Input: heights = [2,2,2,2]
Output: 8
```

---

## Constraints

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

---

## Follow-up Questions

1. What if bars have different widths?
2. Can you solve a 2D version (Maximal Rectangle in Matrix)?
3. How would you find the K largest rectangles?
4. What if you need to support dynamic updates to the histogram?

---

## Approach Hints

<details>
<summary>Hint 1 - Brute Force</summary>

For each bar, expand left and right to find the largest rectangle with that bar's height:
```python
max_area = 0
for i in range(len(heights)):
    left = i
    while left > 0 and heights[left-1] >= heights[i]:
        left -= 1

    right = i
    while right < len(heights)-1 and heights[right+1] >= heights[i]:
        right += 1

    width = right - left + 1
    area = heights[i] * width
    max_area = max(max_area, area)
```

- Time: O(n²)
- Space: O(1)
</details>

<details>
<summary>Hint 2 - Divide and Conquer</summary>

Similar to merge sort:
1. Find the minimum height in current range
2. The answer is maximum of:
   - Area with minimum height: min_height × width
   - Largest rectangle in left subarray
   - Largest rectangle in right subarray

- Time: O(n log n) average, O(n²) worst case
- Space: O(log n) for recursion
</details>

<details>
<summary>Hint 3 - Monotonic Stack (Optimal)</summary>

Use a stack to maintain bars in increasing order of height:
1. If current bar is higher than stack top, push it
2. If current bar is lower, pop bars and calculate area:
   - For each popped bar, it's the minimum height
   - Width: current_index - stack_top_after_pop - 1
3. Process remaining bars in stack at the end

Key insight: When we pop a bar, we know the boundaries where it was the minimum height.

- Time: O(n)
- Space: O(n)
</details>

<details>
<summary>Hint 4 - Detailed Stack Algorithm</summary>

```python
def largest_rectangle(heights):
    stack = []  # Stores indices
    max_area = 0
    heights = heights + [0]  # Add sentinel to process all bars

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            # Pop and calculate area
            height_index = stack.pop()
            height = heights[height_index]

            # Width calculation
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = height * width
            max_area = max(max_area, area)

        stack.append(i)

    return max_area
```

Why this works:
- Stack maintains increasing heights
- When we pop, the popped bar is bounded by:
  - Left: previous bar in stack (first bar smaller on left)
  - Right: current bar (first bar smaller on right)
- Width is the span where popped bar is minimum

- Time: O(n) - each element pushed and popped once
- Space: O(n) - stack size
</details>

<details>
<summary>Hint 5 - Alternative: Precompute Boundaries</summary>

For each bar, precompute:
- `left[i]`: index of first bar to left with height < heights[i]
- `right[i]`: index of first bar to right with height < heights[i]

Then: `area[i] = heights[i] * (right[i] - left[i] - 1)`

This is essentially what the stack does implicitly.

- Time: O(n)
- Space: O(n)
</details>

---

## Key Concepts to Review

1. **Monotonic Stack**
   - Maintaining increasing/decreasing order
   - When to push vs pop
   - What information to store (values vs indices)
   - Using sentinel values

2. **Area Calculation**
   - Height × Width
   - Finding boundaries for each bar
   - Handling edge cases (first/last bar)

3. **Stack Operations**
   - Push: O(1)
   - Pop: O(1)
   - Peek/Top: O(1)
   - Each element processed once

4. **Optimization Techniques**
   - Amortized analysis
   - Sentinel values to simplify logic
   - Two-pass vs one-pass algorithms

---

## Test Cases to Consider

1. Single bar: `heights = [5]`
2. Increasing: `heights = [1,2,3,4,5]`
3. Decreasing: `heights = [5,4,3,2,1]`
4. All same: `heights = [3,3,3,3]`
5. With zeros: `heights = [2,0,2]`
6. Valley shape: `heights = [4,2,1,2,4]`
7. Peak shape: `heights = [1,2,3,2,1]`
8. Large array: 10^5 elements
9. Maximum heights: All bars have height 10^4
10. Multiple equal peaks

### Example Walkthrough:
```
heights = [2,1,5,6,2,3]
Stack operations:

i=0, h=2: stack=[] -> push 0 -> stack=[0]
i=1, h=1: heights[0]=2 > 1 -> pop 0
          height=2, width=1, area=2
          push 1 -> stack=[1]
i=2, h=5: 5 > 1 -> push 2 -> stack=[1,2]
i=3, h=6: 6 > 5 -> push 3 -> stack=[1,2,3]
i=4, h=2: heights[3]=6 > 2 -> pop 3
          height=6, width=1, area=6
          heights[2]=5 > 2 -> pop 2
          height=5, width=2 (from i=2 to i=3), area=10 <- Maximum!
          2 > 1 -> push 4 -> stack=[1,4]
i=5, h=3: 3 > 2 -> push 5 -> stack=[1,4,5]
i=6, h=0 (sentinel): pop all and calculate...

Answer: 10
```

---

## Related Problems

- Maximal Rectangle (Hard) - 2D version
- Trapping Rain Water (Hard)
- Container With Most Water (Medium)
- Maximum Score of a Good Subarray (Hard)
- Sum of Subarray Minimums (Medium)
- Number of Visible People in a Queue (Hard)

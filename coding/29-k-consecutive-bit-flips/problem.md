# Problem 29: Grumpy Bookstore Owner (Sliding Window + Difference Array)

## Difficulty: Hard

## Tags: Array, Sliding Window, Prefix Sum, Greedy

## Problem Description

You are given a binary array `nums` and an integer `k`.

A k-bit flip is choosing a subarray of length `k` from `nums` and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return `-1`.

A subarray is a contiguous part of an array.

## Examples

### Example 1:

```
Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
```

### Example 2:

```
Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
```

### Example 3:

```
Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation:
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= k <= nums.length`

## Key Insights

1. **Greedy Strategy**: Process array from left to right; whenever we see a 0, we must flip starting there
2. **No Choice**: Once we reach position i with a 0, we MUST flip starting at i (or earlier flips must have covered i)
3. **Overlapping Flips**: A position might be affected by multiple overlapping flips
4. **Flip Tracking**: Need efficient way to track which positions are currently "flipped"
5. **Difference Array**: Use difference array technique to track flip ranges in O(1)
6. **Current State**: Need to determine current bit value after all flips affecting it
7. **Impossible Cases**: If we need to flip but not enough positions remain (i + k > n)

## Problem Analysis

### Naive Approach (TLE)

```python
def minKBitFlips(nums, k):
    n = len(nums)
    flips = 0

    for i in range(n):
        if nums[i] == 0:
            if i + k > n:
                return -1
            # Flip range [i, i+k)
            for j in range(i, i + k):
                nums[j] ^= 1
            flips += 1

    return flips
```

**Time Complexity**: O(N * K) - too slow for large inputs
**Space Complexity**: O(1)

### Why Naive Approach Fails

With N = 10^5 and K potentially large, O(N * K) can be up to 10^10 operations.

## Approach

### Solution: Sliding Window + Difference Array

**Key Idea**: Instead of actually flipping bits, track whether each position has been flipped odd/even times.

**Data Structures:**
- `flip_count`: Running count of active flips affecting current position
- `flipped`: Array marking where flips start (or use difference array concept)

**Algorithm:**

1. **Iterate Left to Right**:
   - Track how many active flips are affecting current position
   - Determine current bit value: `original_value XOR (flip_count % 2)`
   - If current value is 0, must flip starting at this position
   - Track flip ranges efficiently using sliding window

2. **Sliding Window Technique**:
   - Use queue or difference array to track active flip ranges
   - When we move beyond position `i + k`, the flip started at `i` no longer affects us
   - Maintain count of active flips in O(1) per position

**Time Complexity**: O(N)
**Space Complexity**: O(N) or O(K) depending on implementation

## Implementation Details

### Solution 1: Using Difference Array

```python
def minKBitFlips(nums, k):
    n = len(nums)
    flipped = [0] * n  # difference array
    flip_count = 0  # current number of active flips
    result = 0

    for i in range(n):
        # Update flip count based on flips ending at this position
        if i >= k:
            flip_count -= flipped[i - k]

        # Current value after all flips
        current_val = nums[i] if flip_count % 2 == 0 else 1 - nums[i]

        if current_val == 0:
            # Need to flip starting at position i
            if i + k > n:
                return -1

            flipped[i] = 1
            flip_count += 1
            result += 1

    return result
```

### Solution 2: Using Queue (More Memory Efficient)

```python
from collections import deque

def minKBitFlips(nums, k):
    n = len(nums)
    flip_positions = deque()  # positions where flips start
    result = 0

    for i in range(n):
        # Remove flips that no longer affect position i
        if flip_positions and flip_positions[0] + k == i:
            flip_positions.popleft()

        # Current value after all active flips
        current_val = nums[i] if len(flip_positions) % 2 == 0 else 1 - nums[i]

        if current_val == 0:
            # Need to flip starting at position i
            if i + k > n:
                return -1

            flip_positions.append(i)
            result += 1

    return result
```

### Solution 3: In-Place Using nums Array

```python
def minKBitFlips(nums, k):
    n = len(nums)
    flip_count = 0
    result = 0

    for i in range(n):
        # Check if flip from position i-k is ending
        if i >= k and nums[i - k] > 1:
            flip_count -= 1

        # Determine current bit value (0 or 1)
        current_val = (nums[i] + flip_count) % 2

        if current_val == 0:
            if i + k > n:
                return -1

            # Mark that flip starts at position i
            nums[i] += 2  # use bit manipulation to mark
            flip_count += 1
            result += 1

    return result
```

## Visual Example

```
nums = [0,0,0,1,0,1,1,0], k = 3

Step 1: i=0, current_val=0, flip [0,1,2]
nums = [1,1,1,1,0,1,1,0]
flips = 1

Step 2: i=1, current_val=1 (flipped from 0), continue

Step 3: i=2, current_val=1 (flipped from 0), continue

Step 4: i=3, current_val=1, continue

Step 5: i=4, current_val=0, flip [4,5,6]
nums = [1,1,1,1,1,0,0,0]
flips = 2

Step 6: i=5, current_val=0 (flipped from 1), flip [5,6,7]
nums = [1,1,1,1,1,1,1,1]
flips = 3

Result: 3
```

## Edge Cases

1. k = 1 (can always flip individual bits)
2. k = n (single flip of entire array)
3. All bits already 1 (return 0)
4. All bits are 0
5. Impossible case where last few positions are 0 but k > remaining length
6. Alternating bits
7. k > n (impossible if any 0 exists)

## Common Mistakes

1. **Actual Flipping**: Actually flipping bits in O(K) per flip leads to TLE
2. **Not Tracking Active Flips**: Forgetting that multiple overlapping flips can affect a position
3. **Incorrect State Calculation**: Not properly computing current bit value after flips
4. **Off-by-One Errors**: Incorrectly determining when flips start/end affecting positions
5. **Modifying Input**: Not properly restoring input array if required
6. **Boundary Checks**: Not checking if i + k > n before attempting flip
7. **Even/Odd Flips**: Forgetting that even number of flips = no change, odd = flipped

## Optimization Techniques

1. **Difference Array**: Track flip ranges without actually flipping
2. **Sliding Window**: Maintain active flips in O(1) per position
3. **In-Place Marking**: Use high bits of array elements to mark flip starts
4. **Queue vs Array**: Queue saves memory but difference array might be faster
5. **XOR Properties**: Use XOR for toggling: `x XOR 1` flips bit

## Why This Problem Is Hard

1. **Efficiency Requirement**: Naive O(N*K) is too slow, need O(N)
2. **State Tracking**: Must efficiently track overlapping flip ranges
3. **Greedy Proof**: Not immediately obvious that greedy left-to-right works
4. **Implementation Details**: Multiple ways to track flips, each with subtleties
5. **Off-by-One Errors**: Easy to make mistakes with range boundaries

## Time Complexity Summary

- **Naive**: O(N * K) - TLE
- **Optimized**: O(N)

## Space Complexity

- **Difference Array**: O(N)
- **Queue**: O(K) in worst case
- **In-Place**: O(1) if modifying input is allowed

## Related Problems

- LeetCode 995: Minimum Number of K Consecutive Bit Flips (this problem)
- LeetCode 1004: Max Consecutive Ones III
- LeetCode 1109: Corporate Flight Bookings (difference array)
- LeetCode 370: Range Addition (difference array)
- LeetCode 48: Rotate Image (in-place array manipulation)
- Problems involving range updates and difference arrays
- Greedy problems with overlapping ranges

# 23. Race Car

**Difficulty**: Hard
**Category**: BFS, DP, State Space Search
**Similar to**: LeetCode 818

---

## Problem Statement

Your car starts at position `0` and speed `+1` on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions `'A'` (accelerate) and `'R'` (reverse).

- When you get an instruction `'A'`, your car does the following:
  - `position += speed`
  - `speed *= 2`

- When you get an instruction `'R'`, your car does the following:
  - If your speed is positive then `speed = -1`
  - Otherwise `speed = 1`
  - Your position stays the same.

For example, after commands "AAR", your car goes to positions `0 → 1 → 3 → 3`, and your speed goes to `1 → 2 → 4 → -1`.

Given a target position `target`, return the length of the shortest sequence of instructions to get there.

---

## Examples

### Example 1:
```
Input: target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0 → 1 → 3.
```

### Example 2:
```
Input: target = 6
Output: 5
Explanation:
The shortest instruction sequence is "AAARA".
Your position goes from 0 → 1 → 3 → 7 → 7 → 6.
```

### Example 3:
```
Input: target = 4
Output: 5
Explanation:
One shortest sequence is "AAARA" or "AARRA".
0 → 1 → 3 → 7 → 7 → 6 → 4 (AAARRA)
```

---

## Constraints

- `1 <= target <= 10^4`

---

## Follow-up Questions

1. What if the car has a maximum speed limit?
2. How would you handle obstacles on the line?
3. Can you find all shortest sequences?
4. What if there's a cost associated with each instruction?

---

## Approach Hints

<details>
<summary>Hint 1 - BFS Approach</summary>

Use BFS to explore all possible states:
- State: (position, speed)
- From each state, try both 'A' and 'R' instructions
- First time we reach target position, return the number of steps

```python
queue = [(0, 1, 0)]  # (position, speed, moves)
visited = {(0, 1)}

while queue:
    pos, speed, moves = queue.pop(0)

    if pos == target:
        return moves

    # Try 'A'
    new_pos = pos + speed
    new_speed = speed * 2
    if (new_pos, new_speed) not in visited:
        visited.add((new_pos, new_speed))
        queue.append((new_pos, new_speed, moves + 1))

    # Try 'R'
    new_speed = -1 if speed > 0 else 1
    if (pos, new_speed) not in visited:
        visited.add((pos, new_speed))
        queue.append((pos, new_speed, moves + 1))
```

- Time: O(target × log(target))
- Space: O(target × log(target))
</details>

<details>
<summary>Hint 2 - State Space Pruning</summary>

Key optimizations to avoid exploring too many states:
1. Don't go too far beyond target (e.g., 2 × target)
2. Don't go too far in negative direction
3. Speed is always a power of 2: -2^k or 2^k

Bounds:
- Position: Generally stay within [-target, 2×target]
- Speed: Limited by log(target) since speed doubles

- Time: O(target × log(target))
- Space: O(target × log(target))
</details>

<details>
<summary>Hint 3 - Dynamic Programming</summary>

Define `dp[pos][speed_power]` = minimum instructions to reach position `pos` with speed `2^speed_power` (negative for reverse).

Transitions:
1. From (pos, speed), do 'A' → (pos + speed, speed × 2)
2. From (pos, speed), do 'R' → (pos, -1 or 1)

Can use memoization with recursion.

- Time: O(target × log(target))
- Space: O(target × log(target))
</details>

<details>
<summary>Hint 4 - Mathematical Insight</summary>

Think about the problem mathematically:
- After k 'A's: position = 2^k - 1, speed = 2^k
- To reach position p, we might:
  1. Go past p, then reverse and come back
  2. Go to some position before p, reverse, overshoot backward, reverse again

Optimal strategy often involves:
- Finding the smallest k where 2^k - 1 >= target
- If 2^k - 1 == target, answer is k
- Otherwise, try different combinations of overshooting and reversing

```python
def racecar(target):
    # Find k such that 2^k - 1 >= target
    k = target.bit_length()

    # Case 1: 2^k - 1 == target
    if 2**k - 1 == target:
        return k

    # Case 2: Go to 2^k - 1, reverse, come back
    # Result: k A's + R + racecar(2^k - 1 - target)
    result = k + 1 + racecar(2**k - 1 - target)

    # Case 3: Go to 2^(k-1) - 1, reverse, go back j steps, reverse again
    for j in range(k - 1):
        # Position after: 2^(k-1) - 1 - (2^j - 1)
        result = min(result,
                    (k-1) + 1 + j + 1 + racecar(target - (2**(k-1) - 1) + (2**j - 1)))

    return result
```

With memoization:
- Time: O(target × log²(target))
- Space: O(target)
</details>

<details>
<summary>Hint 5 - BFS with Optimized Bounds</summary>

Refined BFS with better pruning:
```python
def racecar(target):
    queue = deque([(0, 1, 0)])  # (pos, speed, steps)
    visited = {(0, 1)}

    while queue:
        pos, speed, steps = queue.popleft()

        if pos == target:
            return steps

        # Action 'A': Accelerate
        new_pos = pos + speed
        new_speed = speed * 2

        # Pruning: Don't go too far
        if abs(new_pos - target) < target and (new_pos, new_speed) not in visited:
            visited.add((new_pos, new_speed))
            queue.append((new_pos, new_speed, steps + 1))

        # Action 'R': Reverse
        new_speed = -1 if speed > 0 else 1
        new_state = (pos, new_speed)

        # Only reverse if it makes sense
        if new_state not in visited:
            visited.add(new_state)
            queue.append((pos, new_speed, steps + 1))

    return -1
```

- Time: O(target × log(target))
- Space: O(target × log(target))
</details>

---

## Key Concepts to Review

1. **BFS for Shortest Path**
   - State space representation
   - Visited set to avoid cycles
   - Level-by-level exploration

2. **State Space Pruning**
   - Identifying bounds on states
   - Avoiding unnecessary exploration
   - Balance between pruning and correctness

3. **Dynamic Programming with Memoization**
   - Recursive formulation
   - Caching subproblem results
   - State representation

4. **Mathematical Optimization**
   - Powers of 2
   - Geometric sequences
   - Bit manipulation for powers

5. **Trade-offs**
   - BFS: Simpler, guaranteed shortest path
   - DP: More complex, potentially faster with memoization

---

## Test Cases to Consider

1. Powers of 2 minus 1: `target = 1, 3, 7, 15, 31` (optimal: just A's)
2. Powers of 2: `target = 2, 4, 8, 16` (need reversal)
3. Just above power of 2: `target = 5, 9, 17`
4. Just below power of 2: `target = 6, 14, 30`
5. Small targets: `target = 1, 2, 3`
6. Large targets: `target = 9999, 10000`
7. Middle range: `target = 100, 500, 1000`

### Example Walkthrough:
```
target = 6

BFS exploration:
Start: (pos=0, speed=1, moves=0)

Move 1 (A): (1, 2, 1)
Move 2 (A): (3, 4, 2)
Move 3 (A): (7, 8, 3) - overshot
Move 3 (R): (3, -1, 3) - from (3, 4, 2)

From (3, -1, 3):
Move 4 (A): (2, -2, 4)
Move 4 (R): (3, 1, 4)

From (7, 8, 3):
Move 4 (R): (7, -1, 4)
From (7, -1, 4):
Move 5 (A): (6, -2, 5) - TARGET!

Or another path: AAARA
0 → 1 → 3 → 7 → 7 → 6

Answer: 5
```

---

## Related Problems

- Minimum Jumps to Reach Home (Medium)
- Reach a Number (Medium)
- Broken Calculator (Medium)
- Minimum Number of Increments on Subarrays to Form a Target Array (Hard)
- Minimum Cost to Reach Destination in Time (Hard)

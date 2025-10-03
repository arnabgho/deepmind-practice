# 22. Maximum Students Taking Exam

**Difficulty**: Hard
**Category**: Bitmask DP, State Validation
**Similar to**: LeetCode 1349

---

## Problem Statement

Given a `m × n` matrix `seats` that represent seats distributions in a classroom. If a seat is broken, it is denoted by `'#'` character otherwise it is denoted by a `'.'` character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the **maximum** number of students that can take the exam together without any cheating being possible.

Students must be placed in seats in good condition.

---

## Examples

### Example 1:
```
Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.
One possible configuration:
    #  X  #  #  .  #
    .  #  #  #  #  X
    #  X  #  #  .  #
Where X represents a student.
```

### Example 2:
```
Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats.
    X  #
    #  #
    #  X
    #  #
    X  #
```

### Example 3:
```
Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in the following way:
    #  X  .  X  #
    .  #  X  #  .
    X  .  #  .  X
    .  #  X  #  .
    #  X  .  X  #
```

---

## Constraints

- `seats` contains only characters `'.'` and `'#'`
- `m == seats.length`
- `n == seats[i].length`
- `1 <= m <= 8`
- `1 <= n <= 8`

---

## Follow-up Questions

1. What if students can see diagonally behind as well?
2. How would you handle a much larger grid (20x20)?
3. Can you find all optimal configurations?
4. What if different positions have different weights?

---

## Approach Hints

<details>
<summary>Hint 1 - Understanding Constraints</summary>

Students can cheat if they sit:
- Directly next to each other (left or right)
- Upper-left diagonal
- Upper-right diagonal

Valid placement rules:
- No two students in the same row can be adjacent
- No student can be in upper-left or upper-right of another

With m, n ≤ 8, we can use bitmask to represent each row's configuration.

- Time: O(m × 2^n × 2^n)
- Space: O(m × 2^n)
</details>

<details>
<summary>Hint 2 - Bitmask Row Validation</summary>

For each row, represent student placement as a bitmask:
- Bit i = 1 means student at position i
- Bit i = 0 means no student at position i

Valid row configuration:
```python
def is_valid_row(mask, seats_row):
    for i in range(n):
        if mask & (1 << i):  # Student at position i
            # Check if seat is broken
            if seats_row[i] == '#':
                return False
            # Check if student to the left
            if i > 0 and (mask & (1 << (i-1))):
                return False
    return True
```

- Time: O(2^n) to validate all masks for one row
- Space: O(1)
</details>

<details>
<summary>Hint 3 - DP State Definition</summary>

Define `dp[row][mask]` = maximum students in first `row` rows, where `mask` represents the configuration of current row.

Transition:
```python
for prev_mask in valid_masks[row-1]:
    if compatible(prev_mask, current_mask):
        dp[row][current_mask] = max(dp[row][current_mask],
                                    dp[row-1][prev_mask] + count_bits(current_mask))
```

Where `compatible` checks:
- No student in upper-left diagonal
- No student in upper-right diagonal

- Time: O(m × 2^n × 2^n)
- Space: O(m × 2^n)
</details>

<details>
<summary>Hint 4 - Detailed Algorithm</summary>

```python
def maxStudents(seats):
    m, n = len(seats), len(seats[0])

    # Generate valid masks for each row
    valid_masks = []
    for row in seats:
        masks = []
        for mask in range(1 << n):
            if is_valid_row(mask, row):
                masks.append(mask)
        valid_masks.append(masks)

    # DP
    dp = [[-1] * (1 << n) for _ in range(m)]

    # Initialize first row
    for mask in valid_masks[0]:
        dp[0][mask] = count_bits(mask)

    # Fill DP table
    for row in range(1, m):
        for curr_mask in valid_masks[row]:
            for prev_mask in valid_masks[row-1]:
                if compatible(prev_mask, curr_mask, n):
                    if dp[row-1][prev_mask] != -1:
                        dp[row][curr_mask] = max(
                            dp[row][curr_mask],
                            dp[row-1][prev_mask] + count_bits(curr_mask)
                        )

    return max(dp[m-1])

def compatible(prev_mask, curr_mask, n):
    for i in range(n):
        if curr_mask & (1 << i):  # Student at position i in current row
            # Check upper-left
            if i > 0 and (prev_mask & (1 << (i-1))):
                return False
            # Check upper-right
            if i < n-1 and (prev_mask & (1 << (i+1))):
                return False
    return True

def is_valid_row(mask, row):
    for i in range(len(row)):
        if mask & (1 << i):
            if row[i] == '#':
                return False
            if i > 0 and (mask & (1 << (i-1))):
                return False
    return True

def count_bits(mask):
    return bin(mask).count('1')
```

- Time: O(m × 2^n × 2^n × n) ≈ O(m × 4^n × n)
- Space: O(m × 2^n)
</details>

<details>
<summary>Hint 5 - Space Optimization</summary>

Since we only need the previous row's DP values:
```python
prev_dp = [0] * (1 << n)
curr_dp = [0] * (1 << n)

for row in range(m):
    curr_dp = [0] * (1 << n)
    for curr_mask in valid_masks[row]:
        if row == 0:
            curr_dp[curr_mask] = count_bits(curr_mask)
        else:
            for prev_mask in valid_masks[row-1]:
                if compatible(prev_mask, curr_mask, n):
                    curr_dp[curr_mask] = max(
                        curr_dp[curr_mask],
                        prev_dp[prev_mask] + count_bits(curr_mask)
                    )
    prev_dp = curr_dp

return max(prev_dp)
```

- Time: O(m × 2^n × 2^n × n)
- Space: O(2^n)
</details>

---

## Key Concepts to Review

1. **Bitmask Techniques**
   - Representing states as integers
   - Bit manipulation operations
   - Checking individual bits
   - Counting set bits

2. **State Validation**
   - Row validity checking
   - Row compatibility checking
   - Constraint satisfaction

3. **Dynamic Programming on Bitmasks**
   - State definition with masks
   - Transition between mask states
   - Optimization with valid state precomputation

4. **Complexity Analysis**
   - Understanding 2^n state space
   - Why constraints limit problem size
   - Trade-offs between time and space

---

## Test Cases to Consider

1. Minimum size: `seats = [["."]]` -> Output: 1
2. All broken: `seats = [["#","#"],["#","#"]]` -> Output: 0
3. All available: `seats = [[".",".","."],[".",".","."]]`
4. Single row: `seats = [[".",".",".",".","."]`
5. Single column: `seats = [["."],["."],["."],["."]`
6. Checkerboard pattern
7. Maximum size: 8x8 grid
8. Alternating broken seats
9. No valid placement possible
10. Only one valid configuration

### Example Walkthrough:
```
seats = [["#",".","#","#",".","#"],
         [".","#","#","#","#","."],
         ["#",".","#","#",".","#"]]

Row 0: Available seats at indices 1, 4
  Valid masks: 010000 (student at 1), 000010 (student at 4), 010010 (both)
  But 010010 invalid (checking diagonals later)

Row 1: Available seats at indices 0, 5
  Valid masks: 100000, 000001, 100001

Row 2: Available seats at indices 1, 4
  Valid masks: 010000, 000010, 010010

Compatibility check between rows...
Maximum configuration: 4 students
```

---

## Related Problems

- N-Queens (Hard)
- Maximum Compatibility Score Sum (Medium)
- Parallel Courses II (Hard)
- Partition to K Equal Sum Subsets (Medium)
- Fair Distribution of Cookies (Medium)
- Find Minimum Time to Finish All Jobs (Hard)

# 17. Cherry Pickup II

**Difficulty**: Hard
**Category**: 3D Dynamic Programming, Grid DP
**Similar to**: LeetCode 1463

---

## Problem Statement

You are given a `rows x cols` matrix `grid` representing a field of cherries where `grid[i][j]` represents the number of cherries that you can collect from the `(i, j)` cell.

You have two robots that can collect cherries for you:
- **Robot #1** is located at the top-left corner `(0, 0)`
- **Robot #2** is located at the top-right corner `(0, cols - 1)`

Return the maximum number of cherries collection using both robots by following the rules below:
- From a cell `(i, j)`, robots can move to cell `(i + 1, j - 1)`, `(i + 1, j)`, or `(i + 1, j + 1)`.
- When any robot passes through a cell, it picks up all cherries, and the cell becomes an empty cell.
- When both robots stay in the same cell, only one takes the cherries.
- Both robots cannot move outside of the grid at any moment.
- Both robots should reach the bottom row in `grid`.

---

## Examples

### Example 1:
```
Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1: (0,0) + (1,1) + (2,2) + (3,2) = 3 + 5 + 5 + 1 = 14
Cherries taken by Robot #2: (0,2) + (1,1) + (2,0) + (3,0) = 1 + 5 + 1 + 2 = 9
Total cherries: 14 + 9 = 24 (Note: (1,1) cherry counted once)
```

### Example 2:
```
Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1: (0,0) -> (1,1) -> (2,2) -> (3,3) -> (4,4)
Path of robot #2: (0,6) -> (1,5) -> (2,4) -> (3,3) -> (4,4)
Total cherries: 1 + 2 + 9 + 0 + 5 + 1 + 3 + 0 + 4 + 3 = 28
```

### Example 3:
```
Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22
```

---

## Constraints

- `rows == grid.length`
- `cols == grid[i].length`
- `2 <= rows, cols <= 70`
- `0 <= grid[i][j] <= 100`

---

## Follow-up Questions

1. What if you have three robots starting at different positions?
2. How would you solve this if robots could move in all 4 directions?
3. Can you optimize the space complexity?

---

## Approach Hints

<details>
<summary>Hint 1 - 3D DP State Definition</summary>

Define `dp[row][col1][col2]` as the maximum cherries when:
- Both robots are at row `row`
- Robot 1 is at column `col1`
- Robot 2 is at column `col2`

For each state, both robots move down simultaneously to the next row.
Each robot has 3 choices: move to column-1, column, or column+1.

- Time: O(rows × cols² × 9)
- Space: O(rows × cols²)
</details>

<details>
<summary>Hint 2 - Transition Formula</summary>

For each row, enumerate all valid positions (col1, col2):
```
cherries = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)

For each of 9 combinations of moves:
    next_col1 = col1 + d1 (where d1 in [-1, 0, 1])
    next_col2 = col2 + d2 (where d2 in [-1, 0, 1])
    if valid positions:
        dp[row][col1][col2] = max(cherries + dp[row+1][next_col1][next_col2])
```

- Time: O(rows × cols² × 9)
- Space: O(rows × cols²)
</details>

<details>
<summary>Hint 3 - Space Optimization</summary>

Since we only need the previous row to compute the current row:
- Use two 2D arrays instead of 3D
- Or use a single 2D array with careful iteration order
- Reduces space from O(rows × cols²) to O(cols²)

- Time: O(rows × cols²)
- Space: O(cols²)
</details>

<details>
<summary>Hint 4 - Top-Down with Memoization</summary>

Use recursion with memoization:
```python
def dfs(row, col1, col2):
    if row == rows:
        return 0
    if memoized:
        return memo[row][col1][col2]

    cherries = grid[row][col1]
    if col1 != col2:
        cherries += grid[row][col2]

    max_future = 0
    for d1 in [-1, 0, 1]:
        for d2 in [-1, 0, 1]:
            if valid next positions:
                max_future = max(max_future, dfs(row+1, col1+d1, col2+d2))

    return cherries + max_future
```

- Time: O(rows × cols² × 9)
- Space: O(rows × cols²)
</details>

---

## Key Concepts to Review

1. **3D Dynamic Programming**
   - State with three dimensions
   - Handling multiple entities simultaneously
   - Avoiding double counting

2. **Grid Traversal**
   - Multiple agents on grid
   - Synchronized movement
   - Boundary checking

3. **State Space Optimization**
   - Reducing dimensions when possible
   - Rolling array technique
   - Space-time tradeoffs

4. **Recurrence Relations**
   - Defining transitions between states
   - Handling multiple choices per state
   - Base cases for DP

---

## Test Cases to Consider

1. Minimum grid: `grid = [[1,1],[1,1]]`
2. Single row: `grid = [[3,1,1,5,1,3]]`
3. Robots never meet: Paths don't intersect
4. Robots always together: Same path
5. All zeros: `grid = [[0,0,0],[0,0,0]]`
6. Maximum grid: 70 x 70
7. All cherries in one corner
8. Diagonal pattern of cherries
9. Robots must cross paths to maximize
10. Large values (100 per cell)

---

## Related Problems

- Cherry Pickup (Hard) - Single robot, round trip
- Unique Paths II (Medium)
- Minimum Path Sum (Medium)
- Dungeon Game (Hard)
- Out of Boundary Paths (Medium)

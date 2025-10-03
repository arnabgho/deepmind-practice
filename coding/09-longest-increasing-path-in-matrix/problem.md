# 9. Longest Increasing Path in Matrix

**Difficulty**: Hard
**Category**: DFS, Memoization, Dynamic Programming
**Similar to**: LeetCode 329

---

## Problem Statement

Given an `m x n` integers matrix, return the length of the longest increasing path in the matrix.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

---

## Examples

### Example 1:
```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

### Example 2:
```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

### Example 3:
```
Input: matrix = [[1]]
Output: 1
```

---

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`

---

## Follow-up Questions

1. Can you optimize the space complexity?
2. What if we want to find all paths with the maximum length?
3. How would you solve this if diagonal moves were allowed?
4. Can you solve this using topological sort instead of DFS?

---

## Approach Hints

<details>
<summary>Hint 1 - Naive DFS</summary>

Start DFS from every cell and explore all increasing paths.
- Try all 4 directions from current cell
- Only move to cells with strictly greater values
- Track the maximum path length

Time: O(2^(m+n)) - exponential due to revisiting cells
Space: O(m*n) for recursion stack
</details>

<details>
<summary>Hint 2 - DFS with Memoization (Optimal)</summary>

The key insight: if we know the longest path starting from cell (i,j), we can reuse this result.

**Algorithm:**
1. Create a memo array `dp[i][j]` = longest path starting from (i,j)
2. For each cell, try DFS in all 4 directions
3. Only move to cells with greater values
4. `dp[i][j] = 1 + max(dp[neighbor])` for all valid neighbors
5. Return the maximum value in dp array

**Why this works:**
- Each cell's result depends only on cells with greater values
- Natural DAG structure (no cycles possible)
- Each cell computed at most once

Time: O(m*n) - each cell visited once
Space: O(m*n) for memoization + O(m*n) worst case recursion
</details>

<details>
<summary>Hint 3 - Topological Sort Approach</summary>

Think of the matrix as a directed acyclic graph (DAG):
- Edges go from smaller to larger values
- Use Kahn's algorithm with BFS
- Process cells in order of their values

**Algorithm:**
1. Calculate out-degree for each cell (count neighbors with greater values)
2. Start BFS from all cells with out-degree 0 (local maxima)
3. Process in reverse topological order
4. Track maximum layers traversed

Time: O(m*n)
Space: O(m*n)
</details>

---

## Key Concepts to Review

1. **DFS with Memoization**
   - Top-down dynamic programming
   - Avoiding redundant calculations
   - When to use vs bottom-up DP

2. **Directed Acyclic Graph (DAG)**
   - Why increasing constraint prevents cycles
   - Topological ordering
   - Longest path in DAG

3. **2D Matrix Traversal**
   - 4-directional movement
   - Boundary checking
   - Direction arrays: `[(0,1), (1,0), (0,-1), (-1,0)]`

4. **Time Complexity Analysis**
   - With vs without memoization
   - Understanding state space

---

## Test Cases to Consider

1. Single cell: `[[1]]`
2. All same values: `[[5,5,5],[5,5,5]]` → returns 1
3. Strictly increasing row: `[[1,2,3,4,5]]` → returns 5
4. Strictly decreasing: `[[5,4,3,2,1]]` → returns 5
5. Spiral pattern
6. Multiple paths with same length
7. Large matrix (200x200) with random values
8. Matrix with negative numbers
9. Path that visits all cells
10. Disconnected increasing regions

---

## Common Mistakes

1. ❌ Forgetting to add 1 to the result (counting cells vs edges)
2. ❌ Not checking boundaries properly
3. ❌ Using visited array (unnecessary - increasing constraint prevents revisiting)
4. ❌ Forgetting the "strictly increasing" constraint (using >= instead of >)
5. ❌ Initializing memo with 0 instead of -1 or None (0 is ambiguous)
6. ❌ Not considering all 4 directions
7. ❌ Modifying input matrix

---

## Complexity Analysis

### DFS with Memoization (Optimal):
- **Time Complexity**: O(m*n)
  - Each cell is computed exactly once
  - Results are cached for reuse
  - Total cells: m*n

- **Space Complexity**: O(m*n)
  - Memoization array: O(m*n)
  - Recursion stack: O(m*n) worst case (entire matrix in path)

### Without Memoization:
- **Time Complexity**: O(2^(m+n))
  - Exponential due to recalculating same cells
  - Each cell may be visited many times

---

## Related Problems

- Longest Increasing Subsequence (Medium)
- Number of Increasing Paths in a Grid (Hard)
- Longest Path in a DAG (Algorithm concept)
- Dungeon Game (Hard)
- Cherry Pickup (Hard)
- Minimum Path Sum (Medium)

# 15. Shortest Path in a Grid with Obstacles Elimination

**Difficulty**: Hard
**Category**: BFS, Shortest Path, State Space Search
**Similar to**: LeetCode 1293

---

## Problem Statement

You are given an `m x n` integer matrix `grid` where each cell is either `0` (empty) or `1` (obstacle). You can move up, down, left, or right from and to an empty cell in **one step**.

Return the **minimum number of steps** to walk from the upper left corner `(0, 0)` to the lower right corner `(m - 1, n - 1)` given that you can eliminate **at most** `k` obstacles. If it is not possible to find such walk return `-1`.

---

## Examples

### Example 1:
```
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6.
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
```

### Example 2:
```
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least 2 obstacles to find such a walk.
```

### Example 3:
```
Input: grid = [[0,0,0],[0,1,0],[0,0,0]], k = 1
Output: 4
Explanation:
Simple path going around the obstacle: (0,0)->(0,1)->(0,2)->(1,2)->(2,2)
Or go through it: (0,0)->(1,0)->(1,1)->(1,2)->(2,2) - eliminates 1 obstacle
```

---

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 40`
- `1 <= k <= m * n`
- `grid[0][0] == grid[m - 1][n - 1] == 0`

---

## Follow-up Questions

1. What if we want to find the path with minimum obstacles eliminated (not minimum steps)?
2. How would you reconstruct the actual path taken?
3. What if obstacles have different costs to eliminate?
4. Can you optimize for very large k (k ≥ m+n)?

---

## Approach Hints

<details>
<summary>Hint 1 - Why Simple BFS Doesn't Work</summary>

Standard BFS tracks only position (x, y), but here:
- Same cell can be reached with different remaining eliminations
- Path with more eliminations remaining might lead to better solution

Example:
```
Grid: [[0,1,0],
       [1,1,0],
       [0,0,0]], k=2

Cell (2,2) can be reached:
- Path 1: 6 steps, 0 eliminations used
- Path 2: 4 steps, 2 eliminations used

Both are valid states!
```

We need to track: (x, y, remaining_eliminations)
</details>

<details>
<summary>Hint 2 - BFS with Extended State (Optimal)</summary>

**Key Insight**: State = (row, col, obstacles_remaining)

**Algorithm**:
```python
from collections import deque

def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])

    # Special case: can go straight through all obstacles
    if k >= m + n - 2:
        return m + n - 2

    # BFS
    queue = deque([(0, 0, k, 0)])  # (row, col, obstacles_left, steps)
    visited = {(0, 0, k)}  # (row, col, obstacles_left)
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while queue:
        row, col, obstacles_left, steps = queue.popleft()

        # Reached destination
        if row == m-1 and col == n-1:
            return steps

        # Try all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds
            if 0 <= new_row < m and 0 <= new_col < n:
                new_obstacles = obstacles_left - grid[new_row][new_col]

                # Can we move here?
                if new_obstacles >= 0 and (new_row, new_col, new_obstacles) not in visited:
                    visited.add((new_row, new_col, new_obstacles))
                    queue.append((new_row, new_col, new_obstacles, steps + 1))

    return -1
```

Time: O(m * n * k)
Space: O(m * n * k)
</details>

<details>
<summary>Hint 3 - Optimization: State Reduction</summary>

**Observation**: If we've reached a cell with more obstacles remaining than before, that's strictly better.

We can optimize visited tracking:
```python
visited = {}  # (row, col) -> max_obstacles_remaining

if (new_row, new_col) not in visited or visited[(new_row, new_col)] < new_obstacles:
    visited[(new_row, new_col)] = new_obstacles
    queue.append((new_row, new_col, new_obstacles, steps + 1))
```

This prunes states where we reached same cell with fewer eliminations remaining.
</details>

<details>
<summary>Hint 4 - Special Case Optimization</summary>

If `k >= m + n - 2`, we can eliminate all obstacles in the shortest path:
- Shortest path in grid (without obstacles) is `m + n - 2`
- If we can eliminate that many obstacles, answer is always `m + n - 2`

This handles large k efficiently without BFS.
</details>

---

## Key Concepts to Review

1. **State Space Search**
   - Augmented state representation
   - When to add dimensions to state
   - State explosion vs necessary information

2. **BFS for Shortest Path**
   - BFS guarantees shortest path in unweighted graphs
   - Level-order traversal
   - Queue-based implementation

3. **Visited State Management**
   - What constitutes a unique state?
   - Pruning dominated states
   - Memory optimization techniques

4. **Grid Traversal**
   - 4-directional movement
   - Boundary checking
   - Direction vectors

---

## Test Cases to Consider

1. No obstacles: `grid = [[0,0],[0,0]], k = 0` → 2
2. All obstacles (except start/end): `grid = [[0,1],[1,0]], k = 0` → -1
3. Must use elimination: `grid = [[0,1],[1,0]], k = 1` → 3
4. Optimal path uses elimination: Example 1
5. Can't reach: Example 2
6. k = 0: Regular shortest path
7. k very large: `k >= m+n-2` → Manhattan distance
8. Single row: `[[0,0,0,0]]` → n-1
9. Single column: `[[0],[0],[0]]` → m-1
10. Start equals end: `[[0]]` → 0
11. Maximum grid size: 40x40

---

## Common Mistakes

1. ❌ Using regular BFS without tracking eliminations remaining
2. ❌ Not handling state (x,y,k) properly in visited set
3. ❌ Marking cell as visited without considering different k values
4. ❌ Not checking if we can eliminate obstacle (new_obstacles >= 0)
5. ❌ Forgetting boundary checks
6. ❌ Not handling the special case where k is very large
7. ❌ Using DFS instead of BFS (won't guarantee shortest path)
8. ❌ Decrementing k for empty cells (only decrement on obstacles)
9. ❌ Not checking grid bounds before accessing grid[new_row][new_col]

---

## Complexity Analysis

### BFS with State (Optimal):
- **Time Complexity**: O(m * n * k)
  - State space size: m * n * k
  - Each state processed at most once
  - Each state checks 4 neighbors: O(1)
  - Total: O(m * n * k)

  With optimization when k >= m+n-2: O(1)

- **Space Complexity**: O(m * n * k)
  - Visited set: O(m * n * k) states
  - Queue: O(m * n * k) worst case

  In practice, much smaller due to:
  - Early termination on reaching goal
  - Many states not reachable

### Without State Tracking:
- Would explore exponential number of paths
- Not feasible

---

## Related Problems

- Shortest Path in Binary Matrix (Medium)
- Minimum Obstacle Removal to Reach Corner (Hard)
- Minimum Cost to Make at Least One Valid Path in a Grid (Hard)
- Trapping Rain Water II (Hard)
- Swim in Rising Water (Hard)
- Path With Minimum Effort (Medium)
- Shortest Path Visiting All Nodes (Hard)
- Shortest Path with Alternating Colors (Medium)

---

## Visual Example

```
Grid: [[0,0,0],
       [1,1,0],
       [0,0,0]]
k = 1

State exploration (BFS):
Level 0: (0,0,k=1,steps=0)
Level 1: (0,1,k=1,s=1), (1,0,k=0,s=1)
Level 2: (0,2,k=1,s=2), (1,1,k=0,s=2), (2,0,k=0,s=2)
Level 3: (1,2,k=1,s=3), (1,2,k=-1,X), (2,1,k=0,s=3)
Level 4: (2,2,k=1,s=4) ← GOAL!, (2,2,k=0,s=4) ← Also valid

Answer: 4
```

**Path**: (0,0) → (1,0) [eliminate] → (2,0) → (2,1) → (2,2)

---

## Edge Cases

1. **k = 0**: Standard shortest path in grid with obstacles
2. **k >= m*n**: Can eliminate all obstacles (if needed)
3. **k >= m+n-2**: Manhattan distance always achievable
4. **Single cell**: `[[0]]` → 0
5. **No path exists**: Return -1
6. **Obstacle at start/end**: Problem states grid[0][0] = grid[m-1][n-1] = 0

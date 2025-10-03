# 16. Minimum Cost to Make Valid Path

**Difficulty**: Hard
**Category**: Dijkstra, 0-1 BFS, Graph, DP
**Similar to**: LeetCode 1368

---

## Problem Statement

Given a `m x n` grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of `grid[i][j]` can be:
- `1` which means go to the cell to the right. (i.e., go from `grid[i][j]` to `grid[i][j + 1]`)
- `2` which means go to the cell to the left. (i.e., go from `grid[i][j]` to `grid[i][j - 1]`)
- `3` which means go to the lower cell. (i.e., go from `grid[i][j]` to `grid[i + 1][j]`)
- `4` which means go to the upper cell. (i.e., go from `grid[i][j]` to `grid[i - 1][j]`)

Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell `(0, 0)`. A valid path in the grid is a path that starts from the upper left cell `(0, 0)` and ends at the bottom-right cell `(m - 1, n - 1)` following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

---

## Examples

### Example 1:
```
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3)
change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1)
--> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1)
--> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
```

### Example 2:
```
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2) without any modifications.
```

### Example 3:
```
Input: grid = [[1,2],[4,3]]
Output: 1
```

---

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `1 <= grid[i][j] <= 4`

---

## Follow-up Questions

1. How would you solve this if you could modify signs multiple times?
2. What if the cost of modification varies by cell?
3. Can you solve this with different graph algorithms and compare their performance?

---

## Approach Hints

<details>
<summary>Hint 1 - 0-1 BFS</summary>

This is a shortest path problem with edge weights of 0 or 1:
- Following the existing arrow costs 0
- Changing direction costs 1

Use a deque for 0-1 BFS:
- Add 0-cost transitions to the front
- Add 1-cost transitions to the back

- Time: O(m × n)
- Space: O(m × n)
</details>

<details>
<summary>Hint 2 - Dijkstra's Algorithm</summary>

Treat each cell as a node in a graph:
1. Start from (0, 0) with cost 0
2. For each cell, you can:
   - Follow the arrow with cost 0
   - Go to any neighbor with cost 1
3. Use min-heap to always process minimum cost state

- Time: O(m × n × log(m × n))
- Space: O(m × n)
</details>

<details>
<summary>Hint 3 - BFS with Layers</summary>

Process cells in layers by modification count:
1. BFS from (0,0) following only existing arrows (cost 0)
2. From all reachable cells, try one modification (cost 1)
3. Continue until reaching destination

- Time: O(m × n)
- Space: O(m × n)
</details>

---

## Key Concepts to Review

1. **0-1 BFS**
   - Using deque for weighted shortest path
   - Adding 0-weight edges to front, 1-weight edges to back
   - Works only when weights are 0 or 1

2. **Dijkstra's Algorithm**
   - Shortest path in weighted graphs
   - Priority queue implementation
   - Relaxation of edges

3. **Graph Modeling**
   - Converting grid to graph
   - Edge weights based on direction match
   - State space representation

4. **BFS Variants**
   - Multi-source BFS
   - Layered BFS
   - Weighted BFS

---

## Test Cases to Consider

1. Path exists with cost 0: `grid = [[1,1,3],[3,2,2],[1,1,4]]`
2. All signs point wrong way: Maximum modifications needed
3. Single cell: `grid = [[1]]`
4. Straight line: `grid = [[1,1,1,1]]`
5. Spiral pattern
6. Large grid (100 x 100)
7. Signs pointing outside grid
8. Multiple paths with same cost

---

## Related Problems

- Shortest Path in Binary Matrix (Medium)
- Minimum Obstacles to Remove (Hard)
- Path with Minimum Effort (Medium)
- Swim in Rising Water (Hard)
- Cheapest Flights Within K Stops (Medium)

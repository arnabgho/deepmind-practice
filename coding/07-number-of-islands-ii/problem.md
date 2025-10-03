# 7. Number of Islands II

**Difficulty**: Hard
**Category**: Union Find, Graph
**Similar to**: LeetCode 305

---

## Problem Statement

You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where `0`s represent water and `1`s represent land. Initially, all the cells of `grid` are water cells (i.e., all the cells are `0`s).

We may perform an add land operation which turns the water at position into a land. You are given an array `positions` where `positions[i] = [ri, ci]` is the position `(ri, ci)` at which we should operate the i^th operation.

Return an array of integers `answer` where `answer[i]` is the number of islands after turning the cell `(ri, ci)` into a land.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---

## Examples

### Example 1:
```
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,2]

Explanation:
Initially, the 2d grid is filled with water (0s):
0 0 0
0 0 0
0 0 0

Operation 1: addLand(0, 0) turns the water at grid[0][0] into land.
1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation 2: addLand(0, 1) turns the water at grid[0][1] into land.
1 1 0
0 0 0   Number of islands = 1 (connected horizontally)
0 0 0

Operation 3: addLand(1, 2) turns the water at grid[1][2] into land.
1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation 4: addLand(2, 1) turns the water at grid[2][1] into land.
1 1 0
0 0 1   Number of islands = 2
0 1 0
```

### Example 2:
```
Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]
```

---

## Constraints

- `1 <= m, n, positions.length <= 10^4`
- `1 <= m * n <= 10^4`
- `positions[i].length == 2`
- `0 <= ri < m`
- `0 <= ci < n`

---

## Follow-up Questions

1. Can you solve each operation in amortized O(1) time?
2. What if we also have "remove land" operations?
3. How would you optimize if positions contain duplicates?

---

## Approach Hints

<details>
<summary>Hint 1 - Why Union Find?</summary>

**Problem characteristics:**
- Dynamic connectivity (islands merging)
- Need to track connected components
- Many operations (up to 10^4)

**Naive approach:** DFS/BFS after each operation
- Time: O(k × m × n) where k = operations
- Too slow for large inputs

**Union Find approach:**
- Time: O(k × α(m × n)) ≈ O(k) amortized
- Perfect for dynamic connectivity!
</details>

<details>
<summary>Hint 2 - Union Find Setup</summary>

**Data structures needed:**
```python
parent = {}     # cell -> parent cell (root)
rank = {}       # cell -> rank for union by rank
count = 0       # current number of islands
```

**Key operations:**
- `find(x)`: Find root of x with path compression
- `union(x, y)`: Merge two components
- Add land: Create new island, try to merge with neighbors

**Cell encoding:**
- Convert (row, col) to single ID: `row * n + col`
- Or use tuple: `(row, col)` directly
</details>

<details>
<summary>Hint 3 - Algorithm</summary>

```python
def numIslands2(m, n, positions):
    result = []
    parent = {}
    rank = {}
    count = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        nonlocal count
        root_x, root_y = find(x), find(y)

        if root_x == root_y:
            return  # Already connected

        # Union by rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

        count -= 1  # Two islands merged into one

    for r, c in positions:
        cell = (r, c)

        if cell in parent:
            # Duplicate position, skip
            result.append(count)
            continue

        # Add new island
        parent[cell] = cell
        rank[cell] = 0
        count += 1

        # Try to connect with adjacent land cells
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if 0 <= nr < m and 0 <= nc < n and neighbor in parent:
                union(cell, neighbor)

        result.append(count)

    return result
```
</details>

<details>
<summary>Hint 4 - Optimizations</summary>

**Path Compression:**
```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # All nodes point directly to root
    return parent[x]
```

**Union by Rank:**
```python
# Attach smaller tree under larger tree
if rank[root_x] < rank[root_y]:
    parent[root_x] = root_y
else:
    parent[root_y] = root_x
    if rank[root_x] == rank[root_y]:
        rank[root_x] += 1
```

**These optimizations give O(α(n)) time, where α is inverse Ackermann function (effectively constant).**
</details>

---

## Key Concepts to Review

1. **Union Find (Disjoint Set Union)**
   - Find operation with path compression
   - Union operation with union by rank
   - Connected components counting

2. **Island Counting**
   - New land → count += 1
   - Merge with neighbor → count -= 1
   - Track count dynamically

3. **Cell Encoding**
   - 2D to 1D: `row * cols + col`
   - Or use tuple as key
   - Consistent encoding important

---

## Algorithm Walkthrough

```
m=3, n=3, positions=[[0,0],[0,1],[1,2],[2,1]]

Initially: empty grid, count=0

Operation 1: (0,0)
- Add land at (0,0)
- count = 1
- No neighbors with land
- result = [1]

Operation 2: (0,1)
- Add land at (0,1)
- count = 2
- Check neighbors: (0,0) is land!
- Union (0,0) and (0,1)
- count = 1
- result = [1, 1]

Operation 3: (1,2)
- Add land at (1,2)
- count = 2
- No neighbors with land
- result = [1, 1, 2]

Operation 4: (2,1)
- Add land at (2,1)
- count = 3
- No neighbors with land
- result = [1, 1, 2, 2]
Wait, expected [1,1,2,2]...

Actually, let me recalculate:
After (0,1): count should still be 2, then union makes it 1.
```

---

## Test Cases to Consider

1. Single cell grid: `m=1, n=1, positions=[[0,0]]`
2. All positions create separate islands
3. All positions merge into one island
4. Duplicate positions in input
5. Large grid with many operations
6. Positions that form a line (horizontal or vertical)
7. Positions in corners and edges
8. Random order positions

---

## Common Mistakes

1. ❌ Not handling duplicate positions
2. ❌ Not updating count correctly during union
3. ❌ Forgetting path compression (leads to O(n) find)
4. ❌ Not checking bounds when looking at neighbors
5. ❌ Incrementing count even when merging
6. ❌ Using DFS/BFS (too slow for many operations)
7. ❌ Wrong cell encoding (row/col confusion)

---

## Complexity Analysis

**Without optimizations:**
- Find: O(n)
- Union: O(n)
- Total: O(k × n) where k = operations

**With path compression only:**
- Find: O(log n)
- Total: O(k × log n)

**With both optimizations (path compression + union by rank):**
- Find: O(α(n)) where α is inverse Ackermann
- α(n) < 5 for all practical values of n
- Total: **O(k × α(n)) ≈ O(k)**

**Space Complexity:**
- O(k) for parent and rank dictionaries (only store land cells)
- O(k) for result array

---

## Why Union Find vs DFS/BFS?

| Approach | Time per Operation | Total Time |
|----------|-------------------|------------|
| DFS/BFS | O(m × n) | O(k × m × n) |
| Union Find | O(α(m × n)) ≈ O(1) | O(k) |

For large inputs with many operations, Union Find is essential!

---

## Union Find Template

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # Already connected

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True  # Successfully merged

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
```

---

## Related Problems

- Number of Islands (Medium) - Static version with DFS/BFS
- Accounts Merge (Medium) - Union Find
- Friend Circles (Medium) - Union Find
- Graph Valid Tree (Medium) - Union Find
- Redundant Connection (Medium) - Union Find

# 5. Trapping Rain Water II

**Difficulty**: Hard
**Category**: Priority Queue, BFS, Matrix
**Similar to**: LeetCode 407

---

## Problem Statement

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

---

## Examples

### Example 1:
```
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4

Explanation: After the rain, water is trapped between the blocks.
```

### Example 2:
```
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Explanation:
    3  3  3  3  3
    3 [2][2][2] 3
    3 [2](1)[2] 3
    3 [2][2][2] 3
    3  3  3  3  3

The cells marked with [] can hold 1 unit of water.
The cell marked with () can hold 2 units of water.
```

---

## Constraints

- `m == heightMap.length`
- `n == heightMap[i].length`
- `1 <= m, n <= 200`
- `0 <= heightMap[i][j] <= 2 * 10^4`

---

## Follow-up Questions

1. What if we need to handle floating point heights?
2. How would you visualize which cells contain water?
3. Can you solve this in O(mn) time?

---

## Approach Hints

<details>
<summary>Hint 1 - Key Insight</summary>

**Water flows from high to low:**
- Water trapped at cell (i,j) is determined by the **minimum barrier height** on the path to the boundary
- Like a container: water level = height of shortest wall

**Key observation:**
- Start from the boundary (walls of the container)
- Process cells from outside to inside
- Water level at interior cells is constrained by the minimum boundary height reached so far
</details>

<details>
<summary>Hint 2 - Priority Queue (Min-Heap) Approach</summary>

Similar to Dijkstra's algorithm:

1. **Initialize**: Add all boundary cells to min-heap (they can't trap water)
2. **Process**: Always pick the cell with minimum height from heap
3. **For each neighbor**:
   - If not visited:
   - Water level = max(current cell height, neighbor's height)
   - Trapped water = water level - neighbor's height
   - Add neighbor to heap with water level as priority

**Why min-heap?** Process lower barriers first (they determine water level).

Time: O(mn log(mn))
Space: O(mn)
</details>

<details>
<summary>Hint 3 - Algorithm Details</summary>

```python
def trapRainWater(heightMap):
    if not heightMap: return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = set()
    heap = []

    # Add all boundary cells to heap
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heappush(heap, (heightMap[i][j], i, j))
                visited.add((i, j))

    water = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while heap:
        height, x, y = heappop(heap)

        # Check all neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                # Water level is at least as high as current boundary
                water += max(0, height - heightMap[nx][ny])

                # Add neighbor with its effective height
                heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                visited.add((nx, ny))

    return water
```
</details>

---

## Key Concepts to Review

1. **Priority Queue**
   - Process elements by priority (height)
   - Min-heap for smallest height first

2. **BFS from Boundary**
   - Start from edges/boundary
   - Work inward
   - Similar to "flood fill" from outside

3. **Water Level Calculation**
   - Water level at cell = max(current_barrier, cell_height)
   - Trapped water = water_level - cell_height

4. **Comparison to 1D Problem**
   - 1D: Two pointers work (left/right max)
   - 2D: Need priority queue (4 directions)

---

## Visual Example

```
Heights:        Water levels:   Trapped:
3  3  3  3  3   3  3  3  3  3   0  0  0  0  0
3  2  2  2  3   3  3  3  3  3   1  1  1  1  0
3  2  1  2  3   3  3  3  3  3   1  1  2  1  0
3  2  2  2  3   3  3  3  3  3   1  1  1  1  0
3  3  3  3  3   3  3  3  3  3   0  0  0  0  0
```

Process order (by height):
1. All 3s (boundary)
2. 2s (next lowest)
3. 1 (center)

---

## Test Cases to Consider

1. Single cell: `heightMap = [[5]]` → 0
2. No water trapped: `heightMap = [[5,5,5],[5,1,5],[5,5,5]]` → 0 (interior open to boundary)
3. All same height: `heightMap = [[2,2],[2,2]]` → 0
4. Increasing heights inward
5. Valley in the middle
6. Multiple valleys
7. Large grid (200 × 200)

---

## Common Mistakes

1. ❌ Using simple max height approach (doesn't work in 2D)
2. ❌ Not processing from boundary inward
3. ❌ Using regular queue instead of priority queue (wrong order)
4. ❌ Not tracking water level separately from cell height
5. ❌ Forgetting to mark cells as visited
6. ❌ Not handling edge/boundary cells correctly

---

## Why Priority Queue?

**Example showing need for min-heap:**
```
Boundary: 3  5  3
          5  1  5
          3  5  3
```

If we process cells in random order:
- Might process high barrier (5) first
- Would think water level is 5
- But actual water level determined by minimum barrier (3)

With min-heap:
- Process 3s first → water level = 3
- Center cell (1) gets water up to level 3
- Trapped water = 3 - 1 = 2 ✓

---

## Complexity Analysis

**Time Complexity: O(mn log(mn))**
- Add all mn cells to heap: O(mn log(mn))
- Each cell processed once

**Space Complexity: O(mn)**
- Heap size: O(mn) in worst case
- Visited set: O(mn)

---

## Related Problems

- Trapping Rain Water (Hard) - 1D version
- Pacific Atlantic Water Flow (Medium)
- Walls and Gates (Medium)
- Shortest Distance from All Buildings (Hard)

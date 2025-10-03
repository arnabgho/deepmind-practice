# 19. Shortest Path Visiting All Nodes

**Difficulty**: Hard
**Category**: BFS, Bitmask DP, Graph
**Similar to**: LeetCode 847

---

## Problem Statement

You have an undirected, connected graph of `n` nodes labeled from `0` to `n - 1`. You are given an array `graph` where `graph[i]` is a list of all the nodes connected with node `i` by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

---

## Examples

### Example 1:
```
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
```

### Example 2:
```
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
```

---

## Constraints

- `n == graph.length`
- `1 <= n <= 12`
- `0 <= graph[i].length < n`
- `graph[i]` does not contain `i`
- If `graph[a]` contains `b`, then `graph[b]` contains `a`
- The input graph is always connected

---

## Follow-up Questions

1. What if the graph is weighted?
2. How would you find all shortest paths, not just the length?
3. What if you must end at a specific node?
4. Can you handle disconnected components?

---

## Approach Hints

<details>
<summary>Hint 1 - BFS with Bitmask State</summary>

Use BFS where state = (current_node, visited_nodes_bitmask):
- Start from all nodes simultaneously (multiple sources)
- State represents: "I'm at node X and have visited these nodes"
- Goal: reach any state where all nodes are visited (bitmask = 2^n - 1)
- Use queue and visited set to avoid revisiting same state

- Time: O(n² × 2^n)
- Space: O(n × 2^n)
</details>

<details>
<summary>Hint 2 - Dynamic Programming with Bitmask</summary>

Define `dp[mask][i]` = minimum steps to visit nodes in mask ending at node i:
```python
dp[1 << start][start] = 0  # Start from each node

For each state (mask, node):
    For each neighbor:
        new_mask = mask | (1 << neighbor)
        dp[new_mask][neighbor] = min(dp[new_mask][neighbor],
                                     dp[mask][node] + 1)
```

Answer: min(dp[(1 << n) - 1][i] for all i)

- Time: O(n² × 2^n)
- Space: O(n × 2^n)
</details>

<details>
<summary>Hint 3 - Multi-Source BFS</summary>

Initialize BFS with all nodes as starting points:
```python
queue = [(node, 1 << node, 0) for node in range(n)]
visited = {(node, 1 << node) for node in range(n)}
target_mask = (1 << n) - 1

while queue:
    node, mask, dist = queue.pop(0)
    if mask == target_mask:
        return dist

    for neighbor in graph[node]:
        new_mask = mask | (1 << neighbor)
        if (neighbor, new_mask) not in visited:
            visited.add((neighbor, new_mask))
            queue.append((neighbor, new_mask, dist + 1))
```

- Time: O(n² × 2^n)
- Space: O(n × 2^n)
</details>

<details>
<summary>Hint 4 - Why Not DFS?</summary>

DFS doesn't guarantee shortest path here because:
- We need the shortest path (minimum edges)
- BFS explores level by level, guaranteeing shortest path
- With bitmask state space, there are 2^n × n states
- DFS would need to explore all paths and compare

BFS is optimal for unweighted shortest path problems.

- Time: O(n² × 2^n)
- Space: O(n × 2^n)
</details>

---

## Key Concepts to Review

1. **Bitmask Techniques**
   - Representing sets as integers
   - Setting bits: `mask | (1 << i)`
   - Checking bits: `mask & (1 << i)`
   - All bits set: `(1 << n) - 1`

2. **BFS for Shortest Path**
   - Multi-source BFS
   - State space BFS (not just coordinates)
   - Visited state tracking

3. **Dynamic Programming with Bitmasks**
   - Traveling Salesman Problem (TSP)
   - Subset enumeration
   - State transitions

4. **Graph Theory**
   - Hamiltonian path (visits all vertices)
   - Connected components
   - Undirected graph traversal

---

## Test Cases to Consider

1. Minimum graph: `n = 1, graph = [[]]`
2. Two nodes: `graph = [[1],[0]]`
3. Complete graph: All nodes connected to all others
4. Linear path: `graph = [[1],[0,2],[1,3],[2]]`
5. Star graph: One center node connected to all
6. Cycle: `graph = [[1],[0,2],[1,3],[2,0]]`
7. Maximum nodes: n = 12
8. Tree structure
9. Disconnected (if constraints allowed)
10. Graph where shortest path requires backtracking

---

## Related Problems

- Traveling Salesman Problem (NP-Hard)
- Minimum Cost to Connect All Points (Medium)
- Find the Shortest Superstring (Hard)
- Shortest Path to Get All Keys (Hard)
- Minimum Number of Work Sessions to Finish Tasks (Medium)
- Distribute Repeating Integers (Hard)

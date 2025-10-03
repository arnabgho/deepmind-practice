# Problem 30: Frog Position After T Seconds

## Difficulty: Hard

## Tags: Tree, DFS, BFS, Graph, Probability, Math

## Problem Description

Given an undirected tree consisting of `n` vertices numbered from `1` to `n`. A frog starts jumping from vertex `1`. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array `edges`, where `edges[i] = [ai, bi]` means that exists an edge connecting the vertices `ai` and `bi`.

Return the probability that after `t` seconds the frog is on the vertex `target`. Answers within `10^-5` of the actual answer will be accepted.

## Examples

### Example 1:

```
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666
Explanation: The figure above shows the given graph. The frog starts at vertex 1,
jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with
1/2 probability to vertex 4 after second 2. Thus the probability for the frog is
on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666.
```

### Example 2:

```
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1,
jumping with 1/3 probability to the vertex 7 after second 1. Thus the probability
for the frog is on the vertex 7 after 1 second is 1/3 = 0.3333333333333333.
```

### Example 3:

```
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output: 0.16666666666666666
```

## Constraints

- `1 <= n <= 100`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `1 <= ai, bi <= n`
- `1 <= t <= 50`
- `1 <= target <= n`

## Key Insights

1. **Tree Structure**: Graph is a tree (n vertices, n-1 edges, connected, acyclic)
2. **Unique Path**: In a tree, there's exactly one path from source (1) to target
3. **Probability Multiplication**: Probability to reach target = product of probabilities along the path
4. **Choice Count**: At each vertex, frog chooses uniformly among unvisited neighbors
5. **Time Constraint**: Must reach target in exactly t seconds (or reach and stay)
6. **Terminal Condition**: If frog reaches target early, it can only stay if no unvisited neighbors
7. **DFS/BFS**: Use DFS or BFS to explore tree and track probability and time

## Problem Analysis

### Understanding the Rules

1. Frog starts at vertex 1 with probability 1.0
2. At each step, if there are k unvisited neighbors, frog jumps to each with probability 1/k
3. If no unvisited neighbors exist, frog stays forever
4. We need probability of being at target after EXACTLY t seconds

### Critical Cases

**Case 1**: Frog reaches target in exactly t steps
- Return accumulated probability

**Case 2**: Frog reaches target in fewer than t steps
- If target has no unvisited children (leaf or all children visited), frog stays → probability valid
- If target has unvisited children, frog must jump away → probability = 0

**Case 3**: Path to target requires more than t steps
- Impossible to reach in time → probability = 0

## Approach

### Solution 1: DFS with Probability Tracking

**Algorithm:**

```
dfs(node, parent, time, probability):
    if time == 0:
        return 1.0 if node == target else 0.0

    if node == target:
        # Reached target - check if we stay or must move
        if has unvisited children:
            return 0.0  # must jump away
        else:
            return probability  # stay forever

    # Calculate unvisited children (excluding parent)
    children = [neighbor for neighbor in graph[node] if neighbor != parent]

    if no children:
        return 0.0  # stuck, can't reach target

    # Try jumping to each child with equal probability
    result = 0.0
    for child in children:
        result += dfs(child, node, time - 1, probability / len(children))

    return result
```

**Time Complexity**: O(N) - visit each node at most once
**Space Complexity**: O(N) - recursion stack for tree height

### Solution 2: BFS with State Tracking

**Algorithm:**

```
1. Build adjacency list from edges
2. BFS starting from vertex 1:
   - State: (current_node, time_remaining, probability)
   - Queue: [(1, t, 1.0)]

3. For each state:
   - If time == 0:
     - If node == target: add probability to result
     - Continue

   - If node == target:
     - Check if it has unvisited children
     - If no children: add probability to result
     - If has children: probability becomes 0 (must jump away)

   - Get unvisited neighbors
   - For each neighbor: add to queue with updated probability
```

**Time Complexity**: O(N * T) in worst case
**Space Complexity**: O(N) for queue and visited set

## Implementation Details

### DFS Implementation

```python
def frogPosition(n, edges, t, target):
    if n == 1:
        return 1.0

    # Build adjacency list
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, parent, time, prob):
        # Get unvisited children
        children = [child for child in graph[node] if child != parent]

        # Base case: time is up
        if time == 0:
            return prob if node == target else 0.0

        # If we're at target
        if node == target:
            # Can only stay if no unvisited children
            return prob if len(children) == 0 else 0.0

        # If stuck (no children to visit)
        if len(children) == 0:
            return 0.0

        # Try each child
        result = 0.0
        for child in children:
            result += dfs(child, node, time - 1, prob / len(children))

        return result

    return dfs(1, -1, t, 1.0)
```

### BFS Implementation

```python
from collections import deque

def frogPosition(n, edges, t, target):
    if n == 1:
        return 1.0 if target == 1 else 0.0

    # Build adjacency list
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # BFS: (node, parent, time, probability)
    queue = deque([(1, -1, 0, 1.0)])

    while queue:
        node, parent, time, prob = queue.popleft()

        # Get unvisited neighbors
        children = [child for child in graph[node] if child != parent]
        num_children = len(children)

        # If we reached target
        if node == target:
            # Must arrive exactly at time t, or arrive early with no way to leave
            if time == t or num_children == 0:
                return prob
            else:
                return 0.0

        # If time is up but not at target
        if time == t:
            continue

        # Jump to each child
        for child in children:
            queue.append((child, node, time + 1, prob / num_children))

    return 0.0
```

## Edge Cases

1. **n = 1**: Only one vertex (start = target = 1)
2. **target = 1**: Target is the starting position
3. **t = 0**: No time to move
4. **Target is leaf**: Frog stays once reached
5. **Target is internal node**: Frog may need to jump away
6. **t very large**: Frog reaches target early and stays
7. **t too small**: Can't reach target in time
8. **Linear tree**: Path vs star-shaped tree

## Common Mistakes

1. **Ignoring Stay Condition**: Not checking if frog stays at target vs jumps away
2. **Counting Parent as Child**: Including parent in available choices
3. **Exact Time vs At Most Time**: Problem asks for probability at exactly time t
4. **Division by Zero**: When node has no children
5. **Visiting Vertices Twice**: Not properly tracking visited nodes
6. **Probability Accumulation**: Not properly multiplying probabilities along path
7. **Early Termination**: Not handling case where frog reaches target early

## Visual Example

```
Tree:
       1
      /|\
     2 3 7
    /|  |
   4 6  5

Target = 4, t = 2

Path from 1 to 4:
1 -> 2 -> 4

Step 1: At vertex 1
- Choices: [2, 3, 7] (3 unvisited neighbors)
- Jump to 2 with probability 1/3

Step 2: At vertex 2 (from 1)
- Choices: [4, 6] (2 unvisited neighbors, excluding parent 1)
- Jump to 4 with probability 1/2

Result: 1/3 * 1/2 = 1/6 ≈ 0.16666666666666666
```

## Why This Problem Is Hard

1. **Multiple Concepts**: Combines graph traversal, probability, and timing
2. **Stay Condition**: Need to determine when frog stays vs continues jumping
3. **Time Constraint**: Must reach target in exactly t seconds (with stay condition)
4. **Parent Tracking**: Must exclude parent from available choices
5. **Probability Calculation**: Need to correctly multiply probabilities along path
6. **Edge Cases**: Many special cases to handle (leaf nodes, early arrival, etc.)

## Mathematical Foundation

**Probability Theory:**
- Independent events: P(A and B) = P(A) × P(B)
- Uniform distribution: Each of k choices has probability 1/k
- Conditional probability: Given at node X, probability of reaching Y

**Tree Properties:**
- Unique path between any two nodes
- No cycles
- n vertices, n-1 edges

## Related Problems

- LeetCode 1377: Frog Position After T Seconds (this problem)
- LeetCode 688: Knight Probability in Chessboard
- LeetCode 837: New 21 Game
- LeetCode 576: Out of Boundary Paths
- LeetCode 1236: Web Crawler
- DFS/BFS problems on trees
- Probability and expected value problems
- Problems with time constraints on graphs

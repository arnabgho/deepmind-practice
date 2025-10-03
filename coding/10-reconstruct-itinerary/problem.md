# 10. Reconstruct Itinerary

**Difficulty**: Hard
**Category**: Graph, DFS, Eulerian Path
**Similar to**: LeetCode 332

---

## Problem Statement

You are given a list of airline tickets where `tickets[i] = [from_i, to_i]` represent the departure and arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets exactly once.

---

## Examples

### Example 1:
```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

### Example 2:
```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]
but it is lexicographically larger.
```

### Example 3:
```
Input: tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
Output: ["JFK","NRT","JFK","KUL"]
```

---

## Constraints

- `1 <= tickets.length <= 300`
- `tickets[i].length == 2`
- `from_i.length == 3`
- `to_i.length == 3`
- `from_i` and `to_i` consist of uppercase English letters
- `from_i != to_i`

---

## Follow-up Questions

1. What if the starting airport is not fixed?
2. How would you handle the case where no valid itinerary exists?
3. Can you identify if this is an Eulerian path or Eulerian circuit?
4. What if some tickets can be used multiple times?

---

## Approach Hints

<details>
<summary>Hint 1 - Graph Representation</summary>

Model this as a directed graph:
- Nodes: airports
- Edges: tickets (directed from departure to arrival)
- Goal: Find Eulerian path starting from "JFK"

Build adjacency list:
```python
graph = {
    "JFK": ["ATL", "SFO"],
    "ATL": ["JFK", "SFO"],
    "SFO": ["ATL"]
}
```

Key insight: Sort destinations for each airport to ensure lexical order.
</details>

<details>
<summary>Hint 2 - Eulerian Path Concept</summary>

**Eulerian Path**: A path that visits every edge exactly once.

**Conditions:**
- Directed graph has Eulerian path if:
  - At most one vertex has out-degree - in-degree = 1 (start)
  - At most one vertex has in-degree - out-degree = 1 (end)
  - All other vertices have equal in-degree and out-degree

**Our problem**: Guaranteed to have valid itinerary (Eulerian path exists).

**Hierholzer's Algorithm**: Efficient way to find Eulerian path.
</details>

<details>
<summary>Hint 3 - DFS with Hierholzer's Algorithm (Optimal)</summary>

**Algorithm:**
1. Build graph with adjacency list (sorted for lexical order)
2. Use DFS to traverse, always choosing smallest lexical neighbor
3. **Key trick**: Add airport to result AFTER visiting all its neighbors (post-order)
4. Reverse the result at the end

**Why post-order?**
```
Consider: JFK -> A -> B -> C
          JFK -> D

If we add JFK first, we might get: JFK, D, ... then stuck
Post-order ensures we explore dead-ends first, then backtrack
Result: C, B, A, D, JFK → Reverse → JFK, D, A, B, C
```

**Implementation:**
```python
def findItinerary(tickets):
    graph = defaultdict(list)
    for src, dst in tickets:
        graph[src].append(dst)

    # Sort for lexical order
    for src in graph:
        graph[src].sort(reverse=True)  # reverse for efficient pop()

    route = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()  # visit smallest
            dfs(next_airport)
        route.append(airport)  # post-order

    dfs("JFK")
    return route[::-1]  # reverse
```

Time: O(E log E) where E is number of tickets (sorting)
Space: O(E) for graph and result
</details>

<details>
<summary>Hint 4 - Alternative: Backtracking DFS</summary>

Try all possible paths using backtracking:
1. Start from "JFK"
2. Try each neighbor in lexical order
3. Mark ticket as used
4. If path uses all tickets, return
5. Otherwise, backtrack and try next neighbor

Time: O(E^d) where d is maximum degree (slower)
Space: O(E)

Less efficient but more intuitive than Hierholzer's algorithm.
</details>

---

## Key Concepts to Review

1. **Eulerian Path and Circuit**
   - Definition and conditions
   - Hierholzer's algorithm
   - Difference between path and circuit

2. **Graph Representation**
   - Adjacency list for directed graphs
   - Multiset/list for multiple edges between nodes

3. **DFS Traversal**
   - Pre-order vs post-order
   - Why post-order works for Eulerian path

4. **Lexicographical Ordering**
   - Sorting destinations
   - Using reverse sort + pop() for efficiency

---

## Test Cases to Consider

1. Simple path: `[["JFK","SFO"],["SFO","ATL"]]`
2. Single ticket: `[["JFK","ATL"]]`
3. Cycle back to JFK: `[["JFK","ATL"],["ATL","JFK"]]`
4. Multiple tickets between same airports
5. Lexical ordering test: `[["JFK","B"],["JFK","A"],["A","JFK"]]`
6. Complex graph with multiple branches
7. Dead-end branches (need backtracking)
8. All tickets from JFK: `[["JFK","A"],["JFK","B"],["JFK","C"]]`
9. Maximum tickets (300)
10. Example with forced specific path due to lexical order

---

## Common Mistakes

1. ❌ Using pre-order DFS instead of post-order (won't handle dead-ends)
2. ❌ Not sorting destinations (wrong lexical order)
3. ❌ Forgetting to reverse final result
4. ❌ Not handling multiple tickets between same airports
5. ❌ Using visited set for airports (can visit same airport multiple times)
6. ❌ Modifying graph during iteration without proper handling
7. ❌ Not considering that graph might not be fully connected
8. ❌ Sorting in wrong direction (not matching with pop/remove strategy)

---

## Complexity Analysis

### Hierholzer's Algorithm (Optimal):
- **Time Complexity**: O(E log E)
  - Building graph: O(E)
  - Sorting each adjacency list: O(E log E) total
  - DFS traversal: O(E) - each edge visited once
  - Overall: O(E log E)

- **Space Complexity**: O(E)
  - Graph adjacency list: O(E)
  - Result array: O(E)
  - Recursion stack: O(E) worst case

### Backtracking DFS:
- **Time Complexity**: O(E^d)
  - Where d is maximum out-degree
  - May explore many invalid paths
  - Much slower in practice

- **Space Complexity**: O(E)
  - Similar space requirements

---

## Related Problems

- Reconstruct Original Digits from English (Medium)
- Valid Arrangement of Pairs (Hard)
- Cracking the Safe (Hard)
- Find Itinerary with Minimum Cost (variation)
- Eulerian Circuit in Undirected Graph
- Chinese Postman Problem

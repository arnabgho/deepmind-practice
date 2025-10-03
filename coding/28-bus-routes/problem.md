# Problem 28: Bus Routes

## Difficulty: Hard

## Tags: Array, Hash Table, BFS, Graph

## Problem Description

You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the `i`th bus repeats forever.

- For example, if `routes[0] = [1, 5, 7]`, this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop `source` (You are not on any bus initially), and you want to go to the bus stop `target`. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from `source` to `target`. Return `-1` if it is not possible.

## Examples

### Example 1:

```
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7,
then take the second bus to the bus stop 6.
```

### Example 2:

```
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
Explanation: It is not possible to travel from 15 to 12.
```

### Example 3:

```
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 1
Output: 0
Explanation: Already at target, no buses needed.
```

## Constraints

- `1 <= routes.length <= 500`
- `1 <= routes[i].length <= 10^5`
- All the values of `routes[i]` are unique.
- `sum(routes[i].length) <= 10^5`
- `0 <= routes[i][j] < 10^6`
- `0 <= source, target < 10^6`

## Key Insights

1. **Graph of Buses, Not Stops**: Model the problem as a graph where nodes are buses (routes), not stops
2. **Bus Connectivity**: Two buses are connected if they share at least one common stop
3. **BFS for Shortest Path**: Use BFS to find minimum number of bus transfers
4. **Stop-to-Buses Mapping**: Build a map from each stop to all buses that visit it
5. **Visited Tracking**: Track visited buses (not stops) to avoid cycles
6. **Early Termination**: If source == target, return 0 immediately

## Problem Transformation

**Wrong Approach**: Graph of stops
- If you model this as a graph of stops with edges between consecutive stops on each route
- This doesn't correctly model the problem because you can board a bus at any stop and get off at any other stop on the same route

**Correct Approach**: Graph of buses (routes)
- Nodes: Bus routes (not individual stops)
- Edges: Two buses are connected if they share at least one stop
- Goal: Find shortest path from any bus containing source to any bus containing target
- Each edge traversal = one bus ride

## Approach

### Solution: BFS on Graph of Bus Routes

**Data Structures:**
- `stop_to_buses`: HashMap mapping each stop to list of buses that visit it
- `visited_buses`: Set of already taken buses
- `queue`: BFS queue storing (bus_index, num_buses_taken)

**Algorithm:**

1. **Preprocessing**:
   - Build stop_to_buses mapping
   - Find all buses that contain source stop
   - Find all buses that contain target stop
   - Time: O(N * M) where N = number of routes, M = average stops per route

2. **Edge Case**:
   - If source == target, return 0

3. **BFS**:
   - Initialize queue with all buses containing source (count = 1)
   - Mark these buses as visited
   - For each bus in queue:
     - Check if bus contains target -> return count
     - For each stop in this bus:
       - For each adjacent bus at this stop:
         - If not visited, add to queue with count+1
   - If queue exhausted, return -1

**Time Complexity:**
- Preprocessing: O(N * M) where N = routes, M = avg stops per route
- BFS: O(N * M) in worst case we visit all routes and all stops
- Overall: O(N * M)

**Space Complexity:**
- O(N * M) for stop_to_buses mapping and visited set

## Implementation Details

### Building Stop-to-Buses Map

```python
from collections import defaultdict, deque

def build_graph(routes):
    stop_to_buses = defaultdict(set)
    for bus_idx, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].add(bus_idx)
    return stop_to_buses
```

### BFS Implementation

```python
def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    # Build stop to buses mapping
    stop_to_buses = defaultdict(set)
    for bus_idx, route in enumerate(routes):
        for stop in route:
            stop_to_buses[stop].add(bus_idx)

    # BFS
    visited_buses = set()
    queue = deque()

    # Start with all buses containing source
    for bus in stop_to_buses[source]:
        queue.append((bus, 1))
        visited_buses.add(bus)

    while queue:
        bus_idx, num_buses = queue.popleft()

        # Check if this bus reaches target
        if target in routes[bus_idx]:
            return num_buses

        # Explore all buses reachable from current bus
        for stop in routes[bus_idx]:
            for next_bus in stop_to_buses[stop]:
                if next_bus not in visited_buses:
                    visited_buses.add(next_bus)
                    queue.append((next_bus, num_buses + 1))

    return -1
```

## Optimizations

### 1. Use Sets for Routes

Convert each route to a set for O(1) membership checking:

```python
routes = [set(route) for route in routes]
```

### 2. Early Stop Set

Build a set of buses containing target for early termination:

```python
target_buses = stop_to_buses[target]
# In BFS:
if bus_idx in target_buses:
    return num_buses
```

### 3. Bidirectional BFS

Search from both source and target simultaneously to reduce search space.

## Edge Cases

1. Source equals target (return 0)
2. Source or target doesn't exist in any route (return -1)
3. Single route containing both source and target (return 1)
4. No connection between source and target buses (return -1)
5. Multiple routes containing same stops
6. Very long routes with many stops
7. Many routes with no shared stops

## Common Mistakes

1. **Wrong Graph Model**: Modeling as graph of stops instead of buses
2. **Not Using Sets**: Using lists for routes causes O(N) membership checks
3. **Visiting Stops Instead of Buses**: Tracking visited stops instead of visited buses leads to infinite loops
4. **Not Handling Source == Target**: Forgetting to return 0 immediately
5. **Off-by-One**: Starting count at 0 instead of 1 (first bus is count=1)
6. **Inefficient Stop Lookup**: Checking if target is in route using linear search
7. **Duplicate Processing**: Not properly marking buses as visited

## Why This Problem Is Hard

1. **Non-Intuitive Graph Model**: Need to realize nodes are buses, not stops
2. **Complex Connectivity**: Two buses connected if they share ANY stop, not just consecutive stops
3. **Optimization Required**: Naive approaches can be too slow given constraints
4. **Multiple Valid Solutions**: Need to find minimum, not just any solution

## Comparison: Stop Graph vs Bus Graph

| Aspect | Stop Graph (Wrong) | Bus Graph (Correct) |
|--------|-------------------|---------------------|
| Nodes | Bus stops | Bus routes |
| Edges | Between consecutive stops | Between buses sharing stops |
| Path length | Number of stops | Number of buses |
| Correctness | Incorrect model | Correct model |
| Why wrong/right | Can't jump between non-consecutive stops on same bus | Correctly models ability to ride bus from any stop to any other stop on same route |

## Related Problems

- LeetCode 815: Bus Routes (this problem)
- LeetCode 127: Word Ladder (similar BFS with transformation)
- LeetCode 752: Open the Lock (BFS shortest path)
- LeetCode 1345: Jump Game IV (BFS with value-based connectivity)
- LeetCode 847: Shortest Path Visiting All Nodes (BFS with state)
- Graph problems requiring shortest path with BFS
- Problems where the graph structure isn't immediately obvious

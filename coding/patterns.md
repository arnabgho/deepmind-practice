# Pattern Recognition Guide

This guide helps you identify which algorithmic patterns apply to different problems. Use this to build intuition for approaching new DeepMind-style problems.

---

## Priority Queue / Heap Patterns

### When to Use
- "K-th largest/smallest" problems
- Merging sorted sequences
- Streaming data with top-K requirements
- Greedy algorithms requiring best choice at each step
- Shortest path with modifications

### Problems Using This Pattern
- **#1: Merge K Sorted Lists** - Merge with min-heap
- **#5: Trapping Rain Water II** - Process boundary inward
- **#8: Course Schedule III** - Greedy scheduling with heap
- **#13: Find Median from Data Stream** - Dual heap balance
- **#24: Design Search Autocomplete** - Top-K with trie

### Key Techniques
- Min-heap vs max-heap selection
- Dual heap for median maintenance
- Heap as priority-based queue
- Lazy deletion in heaps

### Time Complexity
- Insert: O(log n)
- Extract min/max: O(log n)
- Peek: O(1)

---

## Stack Patterns

### When to Use
- Nested structures (parentheses, HTML tags)
- Next greater/smaller element problems
- Depth-first iteration without recursion
- Monotonic stack for range queries
- Expression evaluation

### Problems Using This Pattern
- **#12: Design Iterator for Nested List** - Stack-based iteration
- **#21: Largest Rectangle in Histogram** - Monotonic stack

### Monotonic Stack Specifically
Use when you need to find the next/previous greater/smaller element efficiently.

### Key Techniques
- Monotonic increasing: Stack maintains increasing order
- Monotonic decreasing: Stack maintains decreasing order
- Process elements and maintain invariant
- When to pop vs push

### Time Complexity
- Each element pushed/popped once: O(n) amortized

---

## Double Linked List Patterns

### When to Use
- O(1) insertion and deletion at both ends
- LRU/LFU cache implementations
- Maintain ordered sequence with fast updates
- Need to track position and move elements

### Problems Using This Pattern
- **#2: LRU Cache** - O(1) access and eviction

### Key Techniques
- Dummy head and tail nodes
- Combine with hash map for O(1) access
- Move-to-front operation
- Remove and reinsert patterns

### Time Complexity
- Insert/Delete: O(1)
- Search: O(n) without hash map, O(1) with

---

## Union Find (Disjoint Set Union)

### When to Use
- Connected components in dynamic graphs
- Detect cycles in undirected graphs
- Group elements into disjoint sets
- Problems with merging operations

### Problems Using This Pattern
- **#7: Number of Islands II** - Dynamic connectivity

### Key Techniques
- Path compression: Make tree flat
- Union by rank: Attach smaller tree under larger
- Find with path compression
- Connected components counting

### Time Complexity
- Find/Union: O(α(n)) ≈ O(1) amortized with optimizations

---

## Depth First Search (DFS) Patterns

### When to Use
- Explore all possibilities (backtracking)
- Detect cycles
- Topological sorting
- Path finding (all paths, not shortest)
- Tree/graph traversal

### Problems Using This Pattern
- **#3: Serialize/Deserialize Binary Tree** - Tree traversal
- **#9: Longest Increasing Path in Matrix** - DFS + memo
- **#10: Reconstruct Itinerary** - Eulerian path
- **#14: Alien Dictionary** - Topological sort
- **#23: Race Car** - State space exploration
- **#30: Frog Position After T Seconds** - Tree traversal with constraints

### Key Techniques
- Recursive vs iterative (stack)
- Visited set to avoid cycles
- Backtracking: try, recurse, undo
- Memoization for overlapping subproblems
- Pre-order, in-order, post-order for trees

### Time Complexity
- O(V + E) for graphs
- O(n) for trees

---

## Breadth First Search (BFS) Patterns

### When to Use
- Shortest path in unweighted graphs
- Level-order traversal
- Minimum steps problems
- Find nearest/closest
- State-space exploration with shortest path

### Problems Using This Pattern
- **#4: Word Ladder II** - Shortest transformation + paths
- **#5: Trapping Rain Water II** - BFS from boundary
- **#15: Shortest Path with Obstacles Elimination** - Multi-state BFS
- **#19: Shortest Path Visiting All Nodes** - BFS on state space
- **#28: Bus Routes** - BFS on meta-graph

### Key Techniques
- Queue for level-by-level exploration
- Track distance/level separately
- Multi-source BFS (start from multiple nodes)
- State-space BFS (state = (position, additional_info))
- Bidirectional BFS for optimization

### Time Complexity
- O(V + E) for graphs
- Can be O(states × transitions) for state-space

---

## Dijkstra's Algorithm

### When to Use
- Shortest path in weighted graphs (non-negative weights)
- Minimum cost problems
- Priority-based exploration

### Problems Using This Pattern
- **#16: Minimum Cost to Make Valid Path** - Modified Dijkstra (0-1 BFS)

### Key Techniques
- Priority queue with (distance, node)
- Relaxation: update if better path found
- Distance array initialization
- 0-1 BFS variant for 0/1 edge weights (use deque)

### Time Complexity
- O((V + E) log V) with binary heap
- O(V²) with array (dense graphs)
- O(V + E) for 0-1 BFS variant

---

## Dynamic Programming Patterns

### When to Use
- Optimal substructure (optimal solution contains optimal subsolutions)
- Overlapping subproblems
- Count number of ways
- Minimize/maximize something
- Decision at each step affects future

### Problems Using This Pattern
- **#9: Longest Increasing Path in Matrix** - 2D DP with DFS
- **#16: Minimum Cost Valid Path** - DP on grid
- **#17: Cherry Pickup II** - 3D DP
- **#18: Parallel Courses III** - Topological DP
- **#19: Shortest Path Visiting All Nodes** - Bitmask DP
- **#22: Maximum Students Taking Exam** - Bitmask DP
- **#30: Frog Position After T Seconds** - Tree DP

### Subtypes

#### Grid DP
- 2D array traversal
- Sum/count paths
- **#17: Cherry Pickup II** - Two agents simultaneously

#### Bitmask DP
- State compressed as bitmask
- Subset problems
- Visiting states
- **#19, #22** use this

#### Tree/Graph DP
- DP on tree structure
- Combine results from children
- **#30: Frog Position**

### Key Techniques
- Top-down (memoization) vs bottom-up (tabulation)
- State definition is crucial
- Transition formula
- Base cases
- Space optimization (1D array for 2D DP)

### Time Complexity
- O(states × transitions)
- Common: O(n²), O(n³), O(2ⁿ × n) for bitmask

---

## Backtracking Patterns

### When to Use
- Generate all solutions
- Combinatorial problems
- Constraint satisfaction
- Pruning search space

### Problems Using This Pattern
- **#4: Word Ladder II** - Reconstruct all shortest paths

### Key Techniques
- Try → Recurse → Undo (backtrack)
- Pruning for efficiency
- Keep track of current path/state
- Base case: found solution

### Time Complexity
- Often exponential: O(2ⁿ), O(n!), etc.
- Pruning can significantly reduce

---

## Topological Sort Patterns

### When to Use
- Dependency resolution
- Course scheduling
- Build order
- Directed acyclic graph (DAG) ordering

### Problems Using This Pattern
- **#14: Alien Dictionary** - Derive order from examples
- **#18: Parallel Courses III** - Critical path in DAG

### Key Techniques

#### Kahn's Algorithm (BFS-based)
1. Calculate in-degrees
2. Queue nodes with in-degree 0
3. Process queue, reduce in-degrees
4. Detect cycle if not all nodes processed

#### DFS-based
1. DFS with three states: unvisited, visiting, visited
2. Detect cycle if visiting node encountered
3. Post-order gives reverse topological order

### Time Complexity
- O(V + E)

---

## Monotonic Deque/Stack

### When to Use
- Sliding window maximum/minimum
- Next/previous greater/smaller element
- Maintain ordering property in window

### Problems Using This Pattern
- **#11: Sliding Window Maximum** - Monotonic deque
- **#21: Largest Rectangle in Histogram** - Monotonic stack

### Key Techniques
- Deque stores indices, not values
- Maintain decreasing (for max) or increasing (for min)
- Remove elements that can't be answer
- Front of deque is answer

### Time Complexity
- O(n) - each element added/removed once

---

## Trie Patterns

### When to Use
- Prefix matching
- Word search problems
- Autocomplete
- Dictionary operations
- IP routing

### Problems Using This Pattern
- **#20: Palindrome Pairs** - Reverse trie for efficient lookup
- **#24: Design Search Autocomplete** - Trie with frequency

### Key Techniques
- Node structure: children + metadata
- Insert: traverse and create nodes
- Search: traverse path
- Prefix search: traverse to prefix node, then collect all
- Can store frequency, end markers, etc.

### Time Complexity
- Insert/Search: O(m) where m is key length
- Space: O(ALPHABET_SIZE × m × n) worst case

---

## State-Space Search

### When to Use
- State = (position, additional_information)
- Need to track more than just position
- Multiple dimensions of state
- Constraints affect reachability

### Problems Using This Pattern
- **#15: Shortest Path with Obstacles Elimination** - (x, y, remaining_k)
- **#19: Shortest Path Visiting All Nodes** - (node, visited_set_bitmask)
- **#23: Race Car** - (position, velocity)

### Key Techniques
- Define state carefully
- Use tuple or custom class for state
- Visited set includes full state
- BFS for shortest, DFS for all paths
- Prune impossible/redundant states

### Time Complexity
- O(states × transitions)
- Can be very large; pruning is essential

---

## Custom Data Structure Design

### When to Use
- System design problems
- Need specific operations to be O(1) or O(log n)
- Combine multiple data structures
- Novel requirements

### Problems Using This Pattern
- **#2: LRU Cache** - Hash map + DLL
- **#6: Design Skip List** - Probabilistic structure
- **#24: Design Search Autocomplete** - Trie + heap
- **#25: Design In-Memory File System** - Tree + hash map
- **#26: Snapshot Array** - Versioning with binary search
- **#27: Design Time-Based Key-Value Store** - Hash map + sorted list

### Key Techniques
- Identify required operations and complexity
- Combine data structures
- Trade space for time or vice versa
- Amortized analysis
- Lazy evaluation when possible

---

## Greedy Patterns

### When to Use
- Locally optimal choice leads to global optimum
- Can prove greedy choice property
- Problems with optimal substructure
- Scheduling, interval problems

### Problems Using This Pattern
- **#8: Course Schedule III** - Choose courses greedily
- **#29: K Consecutive Bit Flips** - Flip at earliest opportunity

### Key Techniques
- Sort by some criterion
- Make locally optimal choice
- Prove correctness (exchange argument)
- Often uses heap for "best" choice

### Time Complexity
- Often O(n log n) due to sorting

---

## Pattern Combinations

Many hard problems combine multiple patterns:

### DP + Graph
- **#16: Minimum Cost Valid Path** - Dijkstra + DP
- **#18: Parallel Courses III** - Topological + DP
- **#30: Frog Position** - DFS + DP

### BFS + State Space
- **#15: Shortest Path with Obstacles Elimination**
- **#19: Shortest Path Visiting All Nodes**

### Trie + Other
- **#20: Palindrome Pairs** - Trie + string manipulation
- **#24: Design Search Autocomplete** - Trie + heap + streaming

### Multiple Data Structures
- **#2: LRU Cache** - Hash map + DLL
- **#13: Find Median** - Two heaps

---

## Problem-Solving Framework

When facing a new problem:

1. **Understand the problem**
   - What are we optimizing?
   - What are the constraints?
   - What's the scale (n < 100 vs n < 10⁶)?

2. **Identify patterns**
   - Does it involve shortest path? → BFS/Dijkstra
   - Need to track state? → State-space search
   - Optimal substructure? → DP
   - Dependencies? → Topological sort
   - Next greater element? → Monotonic stack
   - Top-K? → Heap

3. **Consider data structures**
   - What operations do I need?
   - What complexity is required?
   - Can I combine structures?

4. **Start simple, optimize**
   - Brute force first (understand the problem)
   - Identify bottlenecks
   - Apply patterns to optimize

5. **Test and refine**
   - Edge cases
   - Complexity analysis
   - Can it be further optimized?

---

## Complexity Quick Reference

| Pattern | Typical Time | Typical Space |
|---------|-------------|---------------|
| Heap ops | O(log n) | O(n) |
| DFS/BFS | O(V + E) | O(V) |
| Union Find | O(α(n)) | O(n) |
| Dijkstra | O((V+E) log V) | O(V) |
| Trie ops | O(m) | O(ALPHABET×m×n) |
| Bitmask DP | O(2ⁿ × n) | O(2ⁿ) |

See [complexity-reference.md](./complexity-reference.md) for full details.

# Time & Space Complexity Reference

Quick reference for analyzing algorithm complexity during interviews.

---

## Common Time Complexities

### O(1) - Constant
- Array access by index
- Hash map get/set (average)
- Stack push/pop
- Queue enqueue/dequeue
- Linked list insert/delete (with pointer)

### O(log n) - Logarithmic
- Binary search
- Balanced BST operations
- Heap insert/delete
- Finding power (fast exponentiation)

### O(n) - Linear
- Array traversal
- Linked list traversal
- Single loop through data
- Hash map creation
- Finding min/max in unsorted array

### O(n log n) - Linearithmic
- Efficient sorting (merge sort, heap sort, quick sort average)
- Building heap from array
- Divide and conquer (balanced splits)

### O(n²) - Quadratic
- Nested loops over same data
- Bubble sort, insertion sort, selection sort
- Simple graph algorithms (adjacency matrix)
- Comparing all pairs

### O(n³) - Cubic
- Three nested loops
- Floyd-Warshall algorithm
- Some DP problems (matrix chain multiplication)

### O(2ⁿ) - Exponential
- Recursive Fibonacci (naive)
- Generating all subsets
- Solving NP-complete problems (brute force)

### O(n!) - Factorial
- Generating all permutations
- Traveling salesman (brute force)

---

## Data Structure Operations

| Data Structure | Access | Search | Insert | Delete | Space |
|---------------|--------|--------|--------|--------|-------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Dynamic Array** | O(1) | O(n) | O(1)* | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)** | O(1)** | O(n) |
| **Doubly Linked List** | O(n) | O(n) | O(1)** | O(1)** | O(n) |
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Table** | N/A | O(1)* | O(1)* | O(1)* | O(n) |
| **Binary Search Tree** | O(log n)* | O(log n)* | O(log n)* | O(log n)* | O(n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Binary Heap** | N/A | O(n) | O(log n) | O(log n) | O(n) |
| **Trie** | O(m) | O(m) | O(m) | O(m) | O(ALPHABET × m × n) |

\* Amortized or average case
\** With pointer to location

---

## Algorithm Time Complexities

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Tim Sort** | O(n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| **Radix Sort** | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes |

Where:
- k = range of input
- d = number of digits

### Graph Algorithms

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| **DFS** | O(V + E) | O(V) | Recursive: O(V) stack space |
| **BFS** | O(V + E) | O(V) | Queue space |
| **Dijkstra (Binary Heap)** | O((V+E) log V) | O(V) | Non-negative weights |
| **Dijkstra (Fibonacci Heap)** | O(E + V log V) | O(V) | Theoretical |
| **Bellman-Ford** | O(VE) | O(V) | Handles negative weights |
| **Floyd-Warshall** | O(V³) | O(V²) | All-pairs shortest path |
| **Prim's (Binary Heap)** | O((V+E) log V) | O(V) | MST |
| **Kruskal's** | O(E log E) | O(V) | MST with Union-Find |
| **Topological Sort** | O(V + E) | O(V) | DAG only |
| **Tarjan's SCC** | O(V + E) | O(V) | Strongly connected components |
| **Kosaraju's SCC** | O(V + E) | O(V) | Strongly connected components |

### String Algorithms

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| **KMP** | O(n + m) | O(m) | Pattern matching |
| **Rabin-Karp** | O(n + m)* | O(1) | Multiple pattern search |
| **Z-Algorithm** | O(n + m) | O(n + m) | Pattern matching |
| **Manacher's** | O(n) | O(n) | Longest palindrome |
| **Trie Operations** | O(m) | O(ALPHABET × m × n) | Prefix queries |

\* Average case; O(nm) worst case

### Dynamic Programming

| Pattern | Time | Space | Example |
|---------|------|-------|---------|
| **1D DP** | O(n) | O(n) or O(1) | Fibonacci, house robber |
| **2D DP** | O(n²) or O(nm) | O(n²) or O(n) | LCS, edit distance |
| **3D DP** | O(n³) | O(n³) or O(n²) | Matrix chain |
| **Bitmask DP** | O(2ⁿ × n) | O(2ⁿ) | TSP, subset problems |
| **Digit DP** | O(log n × d × 2) | O(log n × d) | Counting numbers with property |
| **Tree DP** | O(n) | O(n) | Subtree problems |

---

## Union Find (Disjoint Set Union)

| Operation | Without Optimization | With Path Compression | With Both* |
|-----------|---------------------|----------------------|------------|
| **Find** | O(n) | O(log n) | O(α(n)) |
| **Union** | O(1) + Find | O(1) + Find | O(α(n)) |

\* Path compression + union by rank
α(n) is the inverse Ackermann function, effectively O(1)

---

## Space Complexity Patterns

### O(1) - Constant Space
- Using only fixed number of variables
- In-place algorithms
- Iterative solutions without stack

### O(log n) - Logarithmic Space
- Recursive divide and conquer (call stack)
- Binary search recursion
- Balanced tree height

### O(n) - Linear Space
- Creating array/list of input size
- Recursion depth of n
- Hash map with n entries

### O(n²) - Quadratic Space
- 2D arrays
- Adjacency matrix
- Full DP table (can often optimize to O(n))

---

## Analyzing Complexity - Step by Step

### 1. Count Operations
```python
# O(n) - single loop
for i in range(n):
    do_constant_work()

# O(n²) - nested loops
for i in range(n):
    for j in range(n):
        do_constant_work()

# O(n log n) - loop with halving
for i in range(n):
    j = n
    while j > 0:
        j //= 2
```

### 2. Recursive Complexity
Use recurrence relations:

**Binary Search:**
```
T(n) = T(n/2) + O(1)
Result: O(log n)
```

**Merge Sort:**
```
T(n) = 2T(n/2) + O(n)
Result: O(n log n)
```

**Fibonacci (naive):**
```
T(n) = T(n-1) + T(n-2) + O(1)
Result: O(2ⁿ)
```

### 3. Master Theorem
For recurrences of the form: T(n) = aT(n/b) + f(n)

- If f(n) = O(n^c) where c < log_b(a): **T(n) = Θ(n^(log_b(a)))**
- If f(n) = Θ(n^c) where c = log_b(a): **T(n) = Θ(n^c log n)**
- If f(n) = Ω(n^c) where c > log_b(a): **T(n) = Θ(f(n))**

---

## Optimization Techniques

### Time Optimization
1. **Hash map** - O(n²) → O(n) for lookups
2. **Two pointers** - O(n²) → O(n) for sorted arrays
3. **Sliding window** - O(nk) → O(n) for fixed window
4. **Monotonic stack/deque** - O(n²) → O(n) for range queries
5. **Binary search** - O(n) → O(log n) for sorted data
6. **Memoization** - O(2ⁿ) → O(n²) or better for DP
7. **Union Find** - O(n²) → O(n α(n)) for connectivity

### Space Optimization
1. **Sliding window on DP** - O(n²) → O(n) space
2. **In-place algorithms** - O(n) → O(1) space
3. **Iterative vs recursive** - O(n) → O(1) stack space
4. **Bitmask** - O(2ⁿ × n) → O(2ⁿ) for state compression

---

## Interview Tips

### Complexity Analysis Steps
1. **Identify loops** - Each loop multiplies complexity
2. **Recursive depth** - Maximum call stack depth
3. **Per-operation cost** - What happens in each iteration
4. **Data structure operations** - Know the costs
5. **Dominant term** - Drop lower order terms

### Common Mistakes
- ❌ Forgetting about space for recursion stack
- ❌ Assuming hash map operations are always O(1) (can be O(n) worst case)
- ❌ Not accounting for sorting step
- ❌ Confusing n (input size) with different variables (m, k)
- ❌ Not distinguishing average vs worst case

### How to Communicate
1. **State assumptions**: "Assuming hash map operations are O(1)..."
2. **Break it down**: "The outer loop runs n times, inner loop log n times..."
3. **Justify**: "We visit each node once, so O(V), and each edge once, so O(E)..."
4. **Compare**: "This improves from O(n²) brute force to O(n log n)..."

---

## Quick Reference Table

| If you see... | Consider... | Typical Complexity |
|---------------|-------------|-------------------|
| Sorted array | Binary search | O(log n) |
| Two pointers needed | Two pointer technique | O(n) |
| Subarray sum | Prefix sum or sliding window | O(n) |
| K-th element | Heap | O(n log k) |
| Top K elements | Heap | O(n log k) |
| Common characters | Hash map / frequency array | O(n) |
| Palindrome | Two pointers or DP | O(n) or O(n²) |
| Tree traversal | DFS or BFS | O(n) |
| Graph shortest path | BFS (unweighted) or Dijkstra | O(V+E) or O((V+E)log V) |
| All pairs shortest | Floyd-Warshall | O(V³) |
| Connected components | DFS/BFS or Union Find | O(V+E) or O(Vα(V)) |
| Substring search | KMP or Rabin-Karp | O(n+m) |
| Permutations | Backtracking | O(n!) |
| Subsets | Backtracking or bit manipulation | O(2ⁿ) |
| Optimize over choices | DP | Varies (often O(n²)) |

---

## Space-Time Tradeoffs

Often you can trade space for time or vice versa:

| Problem | Time-optimized | Space-optimized |
|---------|---------------|-----------------|
| Fibonacci | O(n) time, O(n) space (memo) | O(n) time, O(1) space (iterative) |
| DP 2D | O(nm) time, O(nm) space | O(nm) time, O(n) space (rolling array) |
| Pathfinding | O(V+E) time, O(V) space | O(VE) time, O(1) space (edge relaxation) |

**Interview Strategy**: Start with time-optimized, mention space optimization if asked.

---

## Practice Problems by Complexity

### O(log n)
- Binary search variants
- Search in rotated sorted array
- Find peak element

### O(n)
- Two sum with hash map
- Sliding window problems
- Kadane's algorithm

### O(n log n)
- Merge sort
- Interval scheduling
- Line sweep algorithms

### O(n²)
- Two sum (brute force)
- Longest palindromic substring
- Triangle minimum path sum

### O(2ⁿ)
- Generate all subsets
- Word break (naive)
- Coin change (naive)

### O(V + E)
- Course schedule (topological sort)
- Clone graph
- Word ladder

Remember: The best solution isn't always the fastest—balance time, space, and code clarity based on constraints!

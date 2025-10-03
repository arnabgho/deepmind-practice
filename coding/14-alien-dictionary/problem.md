# 14. Alien Dictionary

**Difficulty**: Hard
**Category**: Graph, Topological Sort, BFS/DFS
**Similar to**: LeetCode 269

---

## Problem Statement

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are **sorted lexicographically** by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules. If there is no solution, return `""`. If there are multiple solutions, return **any of them**.

---

## Examples

### Example 1:
```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Explanation:
From "wrt" and "wrf", we can get 't' < 'f'
From "wrt" and "er", we can get 'w' < 'e'
From "er" and "ett", we can get 'r' < 't'
From "ett" and "rftt", we can get 'e' < 'r'
So one possible order is "wertf"
```

### Example 2:
```
Input: words = ["z","x"]
Output: "zx"
Explanation: From "z" and "x", we can get 'z' < 'x'
```

### Example 3:
```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return ""
Reason: From "z" and "x", we have 'z' < 'x'
        From "x" and "z", we have 'x' < 'z'
        This is a contradiction
```

### Example 4:
```
Input: words = ["abc","ab"]
Output: ""
Explanation: Invalid ordering - longer word cannot come before its prefix
```

---

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters

---

## Follow-up Questions

1. What if some letters don't appear in any ordering constraints?
2. How would you detect if the input is invalid (cycle or inconsistency)?
3. Can there be multiple valid orderings?
4. What if words are not guaranteed to be sorted correctly?

---

## Approach Hints

<details>
<summary>Hint 1 - Build Graph from Word Comparisons</summary>

**Key Insight**: Compare adjacent words to determine character order.

**Graph Building**:
```
words = ["wrt", "wrf", "er", "ett", "rftt"]

Compare "wrt" vs "wrf":
  w=w, r=r, t≠f → edge: t → f

Compare "wrf" vs "er":
  w≠e → edge: w → e

Compare "er" vs "ett":
  e=e, r≠t → edge: r → t

Compare "ett" vs "rftt":
  e≠r → edge: e → r

Graph: w→e, e→r, r→t, t→f
```

**Important Edge Cases**:
1. If word1 is prefix of word2: valid (word1 < word2)
2. If word2 is prefix of word1: **INVALID** (["abc", "ab"])
3. If no difference found and lengths equal: no new info

Time: O(C) where C is total characters in all words
</details>

<details>
<summary>Hint 2 - Topological Sort (BFS - Kahn's Algorithm)</summary>

After building graph, find topological order:

**Algorithm**:
```python
def alienOrder(words):
    # Build graph and count in-degrees
    graph = {c: set() for word in words for c in word}
    in_degree = {c: 0 for c in graph}

    # Add edges
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))

        # Check for invalid case
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""

        # Find first different character
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    # BFS - Kahn's algorithm
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle
    if len(result) != len(in_degree):
        return ""

    return "".join(result)
```

Time: O(C) for building graph + O(V+E) for topological sort
Space: O(V+E) for graph storage
</details>

<details>
<summary>Hint 3 - Topological Sort (DFS)</summary>

Alternative: DFS-based topological sort

**Algorithm**:
1. Build graph as before
2. Use DFS with three states: unvisited, visiting, visited
3. Detect cycles: if we visit a "visiting" node
4. Post-order DFS gives reverse topological order

```python
def alienOrder(words):
    graph = {c: [] for word in words for c in word}

    # Build graph (same as before)
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                break

    # DFS
    VISITING, VISITED = 1, 2
    state = {}
    result = []

    def dfs(node):
        if node in state:
            return state[node] == VISITED
        state[node] = VISITING
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        state[node] = VISITED
        result.append(node)
        return True

    for char in graph:
        if not dfs(char):
            return ""

    return "".join(result[::-1])  # reverse post-order
```
</details>

---

## Key Concepts to Review

1. **Topological Sort**
   - DAG (Directed Acyclic Graph) property
   - Kahn's algorithm (BFS)
   - DFS-based approach
   - Cycle detection

2. **Graph Building from Constraints**
   - Comparing adjacent pairs
   - Finding first differing character
   - Handling edge cases

3. **Lexicographical Ordering**
   - Dictionary order rules
   - Prefix relationships

4. **Invalid Cases**
   - Cycle detection (contradictory rules)
   - Prefix violation (longer before shorter)

---

## Test Cases to Consider

1. Simple order: `["z","x"]` → "zx"
2. Single word: `["abc"]` → "abc" or "acb" or any valid order
3. Cycle: `["z","x","z"]` → ""
4. Invalid prefix: `["abc","ab"]` → ""
5. No comparison needed: `["a","b","a"]` → valid (a < b established)
6. All same characters: `["aa","aaa","aaaa"]` → "a"
7. Complete graph: Can derive full order
8. Partial graph: Some letters unconstrained
9. Empty words: `[""]` → ""
10. Multiple valid answers: `["za","zb"]` → "abz" or "baz"

---

## Common Mistakes

1. ❌ Not checking for invalid prefix case (["abc", "ab"])
2. ❌ Not detecting cycles (contradictory orderings)
3. ❌ Creating edges for all character pairs (not just first difference)
4. ❌ Forgetting to include all characters that appear (not just those with edges)
5. ❌ Not handling equal words properly
6. ❌ Wrong order when comparing words (should be adjacent pairs)
7. ❌ Not handling case where valid order exists but it's partial
8. ❌ Creating duplicate edges (use set to avoid)
9. ❌ Forgetting to reverse DFS post-order result

---

## Complexity Analysis

### Topological Sort Approach:
- **Time Complexity**: O(C)
  - C = total characters in all words
  - Building graph: O(C) - must examine all characters
  - Topological sort: O(V + E)
    - V = number of unique characters ≤ 26
    - E = number of edges ≤ V²
  - O(C) dominates since C ≥ V

- **Space Complexity**: O(1) or O(V + E)
  - If considering character set fixed (26): O(1)
  - Otherwise: O(V + E) for graph
  - In practice: O(26 + edges) which is O(1)

### Detailed Breakdown:
- **Graph Building**: O(C)
  - Iterate through all word pairs: O(N) where N is number of words
  - For each pair, compare characters: O(min(len1, len2))
  - Total character comparisons bounded by C

- **Topological Sort**:
  - BFS (Kahn's): O(V + E)
  - DFS: O(V + E)
  - V ≤ 26, E ≤ 26² = 676

---

## Related Problems

- Course Schedule (Medium)
- Course Schedule II (Medium)
- Sequence Reconstruction (Medium)
- Minimum Height Trees (Medium)
- Sort Items by Groups Respecting Dependencies (Hard)
- Parallel Courses III (Hard)
- Alien Dictionary (Premium/Hard)

# 4. Word Ladder II

**Difficulty**: Hard
**Category**: BFS, Backtracking, Graph
**Similar to**: LeetCode 126

---

## Problem Statement

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return **all the shortest transformation sequences** from `beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words `[beginWord, s1, s2, ..., sk]`.

---

## Examples

### Example 1:
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```

### Example 2:
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

---

## Constraints

- `1 <= beginWord.length <= 5`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 500`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters
- `beginWord != endWord`
- All the words in `wordList` are unique
- The sum of all shortest transformation sequences does not exceed `10^5`

---

## Follow-up Questions

1. What if we want the longest transformation sequence instead?
2. How would you modify this to find sequences within k transformations?
3. Can you optimize for space if we only need to count the number of sequences?

---

## Approach Hints

<details>
<summary>Hint 1 - BFS for Shortest Path</summary>

Use BFS to find shortest distance from beginWord to all words:

1. Build graph: word → list of words one edit away
2. BFS from beginWord to find shortest distance to each word
3. Store distance in map: `word → distance from beginWord`

This tells us the shortest path length to each word.

Time: O(N × L²) where N = words, L = word length
</details>

<details>
<summary>Hint 2 - Backtracking for All Paths</summary>

Once we have distances, use DFS/backtracking to build all shortest paths:

1. Start from beginWord
2. At each step, only move to words that are:
   - One edit away
   - Distance is exactly +1 (staying on shortest path)
3. When we reach endWord, save the path
4. Backtrack and try other paths

This reconstructs all shortest paths.
</details>

<details>
<summary>Hint 3 - Bidirectional BFS (Optimization)</summary>

To speed up BFS:
1. Start BFS from both beginWord and endWord
2. Alternate between forward and backward search
3. Stop when the two searches meet
4. Build paths using the meeting point

This can reduce search space significantly.
</details>

<details>
<summary>Hint 4 - Graph Building Optimization</summary>

Instead of comparing every word pair (O(N²L)):

**Pattern-based approach:**
1. For each word, generate intermediate states: "hit" → "*it", "h*t", "hi*"
2. Build map: pattern → list of words matching that pattern
3. Words sharing a pattern are neighbors

Time to build graph: O(N × L²)
</details>

---

## Key Concepts to Review

1. **BFS for Shortest Path**
   - Level-by-level exploration
   - First time reaching node = shortest distance
   - Distance tracking

2. **Backtracking**
   - Try path → Recurse → Undo
   - Prune: only explore valid next steps
   - Base case: reached target

3. **Graph Construction**
   - Implicit graph (words are nodes)
   - Edge = one character difference
   - Optimization: intermediate patterns

4. **Combining BFS + Backtracking**
   - BFS: Find shortest distance
   - Backtracking: Reconstruct all paths

---

## Algorithm Outline

```python
def findLadders(beginWord, endWord, wordList):
    # Step 1: Build graph (word -> neighbors)
    graph = build_graph(wordList + [beginWord])

    # Step 2: BFS to find shortest distance to each word
    distances = bfs(beginWord, graph)

    # Step 3: Check if endWord is reachable
    if endWord not in distances:
        return []

    # Step 4: Backtrack to find all shortest paths
    result = []
    backtrack(beginWord, endWord, graph, distances, [beginWord], result)

    return result

def backtrack(current, target, graph, distances, path, result):
    if current == target:
        result.append(path[:])
        return

    for neighbor in graph[current]:
        # Only move forward on shortest path
        if distances[neighbor] == distances[current] + 1:
            path.append(neighbor)
            backtrack(neighbor, target, graph, distances, path, result)
            path.pop()
```

---

## Test Cases to Consider

1. No path exists (endWord not in wordList)
2. Single transformation: "hit" → "hot"
3. Multiple shortest paths (as in example 1)
4. Only one shortest path
5. beginWord == endWord
6. wordList contains beginWord
7. Very long shortest path (near 500 words)
8. Word length = 1

---

## Common Mistakes

1. ❌ Using DFS for finding shortest path (will find all paths, not just shortest)
2. ❌ Not pruning backtracking (exploring words at wrong distance)
3. ❌ Not handling case where endWord not in wordList
4. ❌ Modifying wordList during BFS (affects future searches)
5. ❌ O(N²) graph building (should be O(N × L²))
6. ❌ Revisiting words in same BFS level (can lead to duplicate paths)

---

## Optimization Tips

1. **Early termination**: Stop BFS when endWord is reached
2. **Bidirectional BFS**: Search from both ends
3. **Pattern map**: Use intermediate patterns for neighbor finding
4. **Set for wordList**: O(1) lookup instead of O(N)

---

## Complexity Analysis

**Naive approach:**
- Graph building: O(N² × L) comparing all pairs
- BFS: O(N + E) where E can be O(N²)
- Backtracking: O(paths × path_length)
- Total: O(N² × L)

**Optimized approach:**
- Graph building: O(N × L²) using pattern map
- BFS: O(N × L²)
- Backtracking: O(paths × path_length)
- Total: O(N × L²) + O(output)

---

## Related Problems

- Word Ladder (Medium) - Find length of shortest transformation
- Word Search II (Hard) - Find words on board with Trie
- Minimum Genetic Mutation (Medium) - Similar transformation problem

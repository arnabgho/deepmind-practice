# 18. Parallel Courses III

**Difficulty**: Hard
**Category**: Topological Sort, Dynamic Programming, Graph
**Similar to**: LeetCode 2050

---

## Problem Statement

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given a 2D integer array `relations` where `relations[j] = [prevCoursej, nextCoursej]` denotes that course `prevCoursej` has to be completed before course `nextCoursej` (prerequisite relationship).

Furthermore, you are given a **0-indexed** integer array `time` where `time[i]` denotes how many months it takes to complete the `(i+1)th` course.

You must find the **minimum number of months** needed to complete all the courses following these rules:
- You may start taking a course at any time if the prerequisites are met.
- **Any number of courses can be taken at the same time.**

Return the minimum number of months needed to complete all the courses.

**Note:** The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

---

## Examples

### Example 1:
```
Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
Output: 8
Explanation: The figure above represents the given graph and the time required to complete each course.
We start course 1 and course 2 simultaneously at month 0.
Course 1 takes 3 months and course 2 takes 2 months to complete respectively.
Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.
```

### Example 2:
```
Input: n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
Output: 12
Explanation: The figure above represents the given graph and the time required to complete each course.
You can start courses 1, 2, and 3 at month 0.
You can complete them after 1, 2, and 3 months respectively.
Course 4 should be taken after course 3 is completed, i.e., after 3 months. It is completed after 3 + 4 = 7 months.
Course 5 should be taken after courses 1, 2, 3, and 4 have been completed, i.e., after max(1,2,3,7) = 7 months.
Thus, the minimum time needed to complete all the courses is 7 + 5 = 12 months.
```

---

## Constraints

- `1 <= n <= 5 * 10^4`
- `0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)`
- `relations[j].length == 2`
- `1 <= prevCoursej, nextCoursej <= n`
- `prevCoursej != nextCoursej`
- All the pairs `[prevCoursej, nextCoursej]` are unique.
- `time.length == n`
- `1 <= time[i] <= 10^4`
- The given graph is a directed acyclic graph.

---

## Follow-up Questions

1. What if courses have different release dates?
2. How would you handle a limited number of parallel courses?
3. Can you find the critical path in the course dependency graph?
4. What if some courses can be taken partially in parallel?

---

## Approach Hints

<details>
<summary>Hint 1 - Topological Sort + DP</summary>

Use topological sort to process courses in dependency order:
1. Build adjacency list and compute in-degrees
2. Start with courses that have no prerequisites (in-degree = 0)
3. For each course, track the earliest time it can be completed
4. When a course completes, update dependent courses' start times

`dp[i]` = earliest time to complete course i
= max(dp[prerequisite] for all prerequisites) + time[i]

- Time: O(n + E) where E is number of relations
- Space: O(n + E)
</details>

<details>
<summary>Hint 2 - Kahn's Algorithm with Time Tracking</summary>

Extend Kahn's algorithm to track completion times:
```python
earliest_completion = [0] * (n + 1)
queue = [courses with in-degree 0]

for course in queue:
    earliest_completion[course] = max(earliest_completion[prereq]
                                      for prereq in prerequisites) + time[course]

    for next_course in dependents:
        in_degree[next_course] -= 1
        if in_degree[next_course] == 0:
            queue.append(next_course)

return max(earliest_completion)
```

- Time: O(n + E)
- Space: O(n + E)
</details>

<details>
<summary>Hint 3 - DFS with Memoization</summary>

Use DFS to compute the minimum time for each course:
```python
def dfs(course):
    if computed[course]:
        return dp[course]

    max_prereq_time = 0
    for prereq in prerequisites[course]:
        max_prereq_time = max(max_prereq_time, dfs(prereq))

    dp[course] = max_prereq_time + time[course]
    return dp[course]

return max(dfs(course) for course in all courses)
```

- Time: O(n + E)
- Space: O(n + E)
</details>

<details>
<summary>Hint 4 - Critical Path Method</summary>

This is the Critical Path Method (CPM) from project management:
1. Find the longest path from any source to each node
2. The answer is the maximum of all completion times
3. This represents the critical path through the dependency graph

- Time: O(n + E)
- Space: O(n + E)
</details>

---

## Key Concepts to Review

1. **Topological Sorting**
   - Kahn's algorithm (BFS-based)
   - DFS-based topological sort
   - Detecting cycles in directed graphs

2. **Dynamic Programming on DAG**
   - Computing longest/shortest paths
   - State definition on graph nodes
   - Memoization in recursive solutions

3. **Graph Representations**
   - Adjacency list
   - In-degree computation
   - Reverse graph for dependencies

4. **Critical Path Method**
   - Project scheduling
   - Earliest start/finish times
   - Latest start/finish times
   - Slack time calculation

---

## Test Cases to Consider

1. No dependencies: `relations = []` - All courses in parallel
2. Linear chain: `relations = [[1,2],[2,3],[3,4]]` - Sequential
3. Single course: `n = 1, relations = []`
4. Complete dependencies: Every course depends on all previous
5. Diamond shape: Multiple paths converge
6. Multiple independent chains
7. Maximum constraints: n = 50000
8. All courses take same time
9. One course takes very long time
10. Complex graph with multiple levels

---

## Related Problems

- Course Schedule (Medium)
- Course Schedule II (Medium)
- Parallel Courses (Medium)
- Minimum Height Trees (Medium)
- Longest Increasing Path in Matrix (Hard)
- Single-Threaded CPU (Medium)

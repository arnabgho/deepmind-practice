# 8. Course Schedule III

**Difficulty**: Hard
**Category**: Greedy, Priority Queue (Max-Heap)
**Similar to**: LeetCode 630

---

## Problem Statement

There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [durationi, lastDayi]` indicate that the i^th course should be taken **continuously** for `durationi` days and must be finished before or on `lastDayi`.

You will start on the 1^st day and you **cannot** take two or more courses simultaneously.

Return the **maximum number of courses** that you can take.

---

## Examples

### Example 1:
```
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3

Explanation:
There are totally 4 courses, but you can take 3 courses at most:
- First, take the 1st course, it costs 100 days so you will finish it on the 100th day.
- Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day.
- Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.

The 4th course cannot be taken now since you will finish it on the 3300th day, which exceeds the deadline.
```

### Example 2:
```
Input: courses = [[1,2]]
Output: 1
```

### Example 3:
```
Input: courses = [[3,2],[4,3]]
Output: 0

Explanation: No course can be taken (both deadlines are before duration)
```

---

## Constraints

- `1 <= courses.length <= 10^4`
- `1 <= durationi, lastDayi <= 10^4`

---

## Follow-up Questions

1. What if courses have different values/credits and we want to maximize total value?
2. What if some courses have prerequisites?
3. How would you modify this to find the actual schedule (list of courses)?

---

## Approach Hints

<details>
<summary>Hint 1 - Greedy Insight</summary>

**Key observation:**
- We want to take as many courses as possible (maximize count, not time saved)
- If we can't fit a course, maybe we can **swap it with a longer course** we already took

**Greedy strategy:**
1. Sort courses by deadline (earliest deadline first)
2. Try to take each course
3. If we exceed deadline, remove the longest course we've taken so far
4. The course we just added might be shorter, allowing more courses later

**Why sort by deadline?**
- Taking courses with earlier deadlines first gives us more flexibility later
- If we can't take a course by its deadline now, we definitely can't take it later
</details>

<details>
<summary>Hint 2 - Max-Heap for Longest Course</summary>

**Data structures:**
- Max-heap: Track durations of courses we've taken (longest on top)
- Current time: Track when we'd finish all selected courses

**Algorithm:**
```
1. Sort courses by lastDay (deadline)
2. For each course (duration, deadline):
   a. Add course duration to heap
   b. current_time += duration
   c. If current_time > deadline:
      - Remove longest course from heap
      - current_time -= longest_duration
3. Return heap size (number of courses taken)
```

**Why max-heap?**
- If we exceed deadline, removing the longest course gives us most time back
- This maximizes our chances to fit more courses later
</details>

<details>
<summary>Hint 3 - Implementation Details</summary>

```python
import heapq

def scheduleCourse(courses):
    # Sort by deadline
    courses.sort(key=lambda x: x[1])

    heap = []  # Max-heap (use negative values in Python)
    current_time = 0

    for duration, deadline in courses:
        # Try to take this course
        current_time += duration
        heapq.heappush(heap, -duration)  # Python has min-heap, so negate

        # If we exceed deadline, remove longest course
        if current_time > deadline:
            longest = -heapq.heappop(heap)
            current_time -= longest

    return len(heap)
```

Time: O(n log n) for sorting + O(n log n) for heap operations = **O(n log n)**
Space: O(n) for heap
</details>

<details>
<summary>Hint 4 - Why This Works</summary>

**Proof sketch:**

Claim: Greedy choice (swap longest if needed) is optimal.

**Intuition:**
- If we can take k courses with current strategy, we can't do better
- When we swap, we're replacing a longer course with a shorter one
- This can only help us (more time for future courses)
- We process in deadline order, so earlier courses don't affect later ones

**Example:**
```
courses = [[100,200], [200,1300], [1000,1250], [2000,3200]]

After sorting (already sorted by deadline):
[(100,200), (1000,1250), (200,1300), (2000,3200)]

Step 1: Take (100,200), time=100, heap=[100]
Step 2: Take (1000,1250), time=1100, heap=[100,1000]
Step 3: Take (200,1300), time=1300, heap=[100,1000,200]
Step 4: Try (2000,3200), time=3300 > 3200 (exceeds!)
        Remove longest=1000, time=2300, heap=[100,200,2000]
Result: 3 courses
```
</details>

---

## Key Concepts to Review

1. **Greedy Algorithms**
   - Local optimal choice leads to global optimum
   - Proof: Exchange argument
   - Sorting as a greedy preprocessing step

2. **Priority Queue (Heap)**
   - Max-heap: Get largest element in O(1)
   - Insert: O(log n)
   - Remove max: O(log n)
   - Python: Use negative values for max-heap

3. **Scheduling Problems**
   - Interval scheduling
   - Deadline-based sorting
   - Exchange argument for correctness

---

## Test Cases to Consider

1. All courses can be taken: `[[1,2],[2,3],[3,4]]`
2. No course can be taken: `[[5,1],[5,1]]`
3. Single course: `[[100,200]]`
4. Courses with same deadline: `[[1,5],[2,5],[3,5]]`
5. All same duration: `[[5,10],[5,20],[5,30]]`
6. Courses in random order (not sorted by deadline)
7. Large input (10^4 courses)
8. Course duration equals deadline: `[[5,5]]`

---

## Common Mistakes

1. ❌ Sorting by duration instead of deadline
2. ❌ Using min-heap instead of max-heap (we want longest course)
3. ❌ Not removing any course when exceeding deadline
4. ❌ Trying to maximize time instead of count
5. ❌ Not considering swap strategy (just skip if doesn't fit)
6. ❌ Forgetting to subtract removed course duration from current_time

---

## Why Sort by Deadline?

**Counter-example if we sort by duration:**

```
courses = [[5,15], [10,10]]

If sorted by duration:
1. Take [5,15], time=5
2. Try [10,10], time=15 > 10 (exceeds deadline!)
   Remove [5], time=10 (still exceeds!)
Result: 1 course

If sorted by deadline:
1. Try [10,10], time=10 ✓
2. Try [5,15], time=15 ✓
Result: 2 courses ✓
```

**Sorting by deadline ensures we process constraints in the right order.**

---

## Complexity Analysis

**Time Complexity: O(n log n)**
- Sorting: O(n log n)
- Heap operations: n insertions and at most n deletions, each O(log n)
- Total: O(n log n)

**Space Complexity: O(n)**
- Heap can contain up to n courses
- Sorting might use O(log n) or O(n) depending on implementation

---

## Greedy vs Dynamic Programming

**Why greedy works here:**
- Optimal substructure: Optimal solution for first k courses extends naturally
- Greedy choice property: Sorting by deadline + swap longest is optimal

**When DP might be needed:**
- If we want to maximize total value/credits (not just count)
- If courses have complex dependencies
- If we need to track multiple constraints

---

## Related Problems

- Course Schedule (Medium) - Topological sort, prerequisites
- Course Schedule II (Medium) - Return actual order
- Maximum Profit in Job Scheduling (Hard) - DP with binary search
- Minimum Number of Refueling Stops (Hard) - Similar greedy + heap
- Meeting Rooms II (Medium) - Interval scheduling

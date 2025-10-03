# 1. Merge K Sorted Lists

**Difficulty**: Hard
**Category**: Priority Queue, Divide & Conquer
**Similar to**: LeetCode 23

---

## Problem Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

## Examples

### Example 1:
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

### Example 2:
```
Input: lists = []
Output: []
```

### Example 3:
```
Input: lists = [[]]
Output: []
```

---

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order
- The sum of `lists[i].length` will not exceed `10^4`

---

## Follow-up Questions

1. Can you solve it with better than O(n × k) time complexity where n is the total number of nodes?
2. What if the linked lists are not given all at once but are streamed one at a time?

---

## Approach Hints

<details>
<summary>Hint 1 - Brute Force</summary>

Collect all values from all lists, sort them, then create a new linked list.
- Time: O(N log N) where N is total number of nodes
- Space: O(N)
</details>

<details>
<summary>Hint 2 - Min-Heap / Priority Queue</summary>

Use a min-heap to always get the smallest element among the k lists.
1. Add the first node of each list to the heap
2. Extract min, add to result
3. Add the next node from that list to heap
4. Repeat until heap is empty

- Time: O(N log k) where N is total nodes, k is number of lists
- Space: O(k) for the heap
</details>

<details>
<summary>Hint 3 - Divide and Conquer</summary>

Merge lists pairwise, similar to merge sort:
- Merge lists[0] with lists[1], lists[2] with lists[3], etc.
- Repeat with the merged results
- Continue until one list remains

- Time: O(N log k)
- Space: O(1) if not counting recursion stack
</details>

---

## Key Concepts to Review

1. **Priority Queue (Min-Heap)**
   - Insertion: O(log k)
   - Extract min: O(log k)
   - Heapify: O(k)

2. **Linked List Operations**
   - Node traversal
   - Pointer manipulation

3. **Divide and Conquer**
   - Breaking problem into subproblems
   - Merging results

---

## Test Cases to Consider

1. Empty input: `lists = []`
2. Single list: `lists = [[1,2,3]]`
3. Multiple empty lists: `lists = [[],[],[]]`
4. Lists with one element each: `lists = [[1],[2],[3]]`
5. Lists of varying lengths
6. All lists have same values
7. Negative numbers
8. Large k (10^4 lists)

---

## Related Problems

- Merge Two Sorted Lists (Easy)
- Ugly Number II (Medium)
- Find K Pairs with Smallest Sums (Medium)
- Smallest Range Covering Elements from K Lists (Hard)

# Problem 27: Design Time-Based Key-Value Store

## Difficulty: Medium

## Tags: Hash Table, Binary Search, Design, String

## Problem Description

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

- **`TimeMap()`**: Initializes the object of the data structure.

- **`void set(String key, String value, int timestamp)`**: Stores the key `key` with the value `value` at the given time `timestamp`.

- **`String get(String key, int timestamp)`**: Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

## Examples

### Example 1:

```
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" with value "bar" at timestamp = 1
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value at timestamp 3 and
                               // the largest timestamp that is ≤ 3 is 1 (value "bar")
timeMap.set("foo", "bar2", 4); // store the key "foo" with value "bar2" at timestamp = 4
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2", since the largest timestamp ≤ 5 is 4
```

### Example 2:

```
Input
["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
[[], ["love", "high", 10], ["love", "low", 20], ["love", 5], ["love", 10], ["love", 15], ["love", 20], ["love", 25]]

Output
[null, null, null, "", "high", "high", "low", "low"]
```

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 10^7`
- All the timestamps `timestamp` of `set` are strictly increasing.
- At most `2 * 10^5` calls will be made to `set` and `get`.

## Key Insights

1. **Strictly Increasing Timestamps**: The problem guarantees timestamps are strictly increasing for each key
2. **Binary Search**: Since timestamps are sorted, we can use binary search for efficient lookup
3. **HashMap Structure**: Use HashMap mapping key -> list of (timestamp, value) pairs
4. **Time-Based Versioning**: Similar to version control - finding the right version at a point in time
5. **Floor Operation**: get() essentially performs a floor operation on timestamp
6. **No Updates**: Once a (key, timestamp) pair is set, it's never updated (append-only)

## Approach

### Solution 1: HashMap + List + Binary Search

**Data Structure:**
```
map: HashMap<String, List<Pair<Integer, String>>>
  key -> [(timestamp1, value1), (timestamp2, value2), ...]
```

**Algorithm:**

1. **set(key, value, timestamp)**:
   - If key doesn't exist in map, create new list
   - Append (timestamp, value) to the key's list
   - Time: O(1) since we just append

2. **get(key, timestamp)**:
   - If key doesn't exist, return ""
   - Binary search the list for largest timestamp <= target
   - Return associated value or "" if no valid timestamp found
   - Time: O(log N) where N = number of entries for that key

**Space Complexity:**
- O(N * M) where N = number of unique keys, M = average entries per key

### Binary Search Implementation

**Template for finding floor (largest value <= target):**

```python
def binary_search_floor(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid][0] <= target:
            result = mid
            left = mid + 1  # try to find larger
        else:
            right = mid - 1

    return result
```

## Alternative Solutions

### Solution 2: TreeMap (If Not Guaranteed Sorted)

If timestamps weren't guaranteed to be increasing:
- Use TreeMap instead of List for each key
- TreeMap maintains sorted order automatically
- Use floorEntry() or lowerEntry() for queries
- Time: O(log N) for both set and get

### Solution 3: Multiple Data Structures

For more complex queries (range queries, etc.):
- Use segment tree or interval tree
- Supports more query types but adds complexity

## Implementation Details

### Python Implementation

```python
from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        # Use bisect_right to find insertion point
        i = bisect_right(arr, (timestamp, chr(255)))

        return arr[i-1][1] if i > 0 else ""
```

### Manual Binary Search

```python
def get(self, key: str, timestamp: int) -> str:
    if key not in self.store:
        return ""

    arr = self.store[key]
    left, right = 0, len(arr) - 1
    result = ""

    while left <= right:
        mid = (left + right) // 2
        if arr[mid][0] <= timestamp:
            result = arr[mid][1]
            left = mid + 1
        else:
            right = mid - 1

    return result
```

## Edge Cases

1. Key doesn't exist - return ""
2. Timestamp is smaller than all stored timestamps - return ""
3. Timestamp exactly matches a stored timestamp - return that value
4. Timestamp is larger than all stored timestamps - return most recent value
5. Single entry for a key
6. Multiple gets with same timestamp
7. Very large timestamp values

## Common Mistakes

1. Using linear search instead of binary search - O(N) vs O(log N)
2. Not handling case when key doesn't exist
3. Not handling case when timestamp is too small
4. Incorrect binary search implementation (not finding floor correctly)
5. Using wrong comparison in binary search (should be <=, not <)
6. Not considering that timestamps are strictly increasing
7. Off-by-one errors in binary search

## Optimization Techniques

1. **Built-in Binary Search**: Use language's built-in bisect/binarySearch functions
2. **Tuple Comparison**: Leverage tuple comparison for binary search
3. **Default Dict**: Use defaultdict to avoid checking key existence
4. **No Sorting Needed**: Since timestamps are strictly increasing, no need to sort
5. **Cache Optimization**: Could add caching layer for frequently accessed keys

## Time Complexity Summary

- `set(key, value, timestamp)`: O(1)
- `get(key, timestamp)`: O(log N) where N = number of entries for that key

## Space Complexity

- O(M) where M = total number of set operations across all keys

## Comparison with Similar Problems

| Problem | Key Difference |
|---------|---------------|
| Snapshot Array | Fixed indices vs dynamic keys |
| LRU Cache | No time dimension, fixed capacity |
| Design HashMap | No time dimension |
| Time-Based KV Store | Temporal versioning, no deletions |

## Related Problems

- LeetCode 981: Time Based Key-Value Store (this problem)
- LeetCode 1146: Snapshot Array
- LeetCode 1206: Design Skiplist
- LeetCode 146: LRU Cache
- LeetCode 244: Shortest Word Distance II
- LeetCode 170: Two Sum III - Data structure design
- Binary search problems on sorted arrays

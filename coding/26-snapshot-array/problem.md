# Problem 26: Snapshot Array

## Difficulty: Medium

## Tags: Array, Hash Table, Binary Search, Design

## Problem Description

Implement a SnapshotArray that supports the following interface:

- **`SnapshotArray(int length)`**: Initializes an array-like data structure with the given length. Initially, each element equals 0.

- **`void set(index, val)`**: Sets the element at the given `index` to be equal to `val`.

- **`int snap()`**: Takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus 1.

- **`int get(index, snap_id)`**: Returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`.

## Examples

### Example 1:

```
Input
["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]

Output
[null,null,0,null,5]

Explanation
SnapshotArray snapshotArr = new SnapshotArray(3);  // set the length to be 3
snapshotArr.set(0,5);   // Set array[0] = 5
snapshotArr.snap();     // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);   // Set array[0] = 6
snapshotArr.get(0,0);   // Get the value of array[0] with snap_id = 0, return 5
```

### Example 2:

```
Input
["SnapshotArray","set","snap","snap","snap","get","get","get","set","get"]
[[1],[0,15],[],[],[],[0,2],[0,0],[0,1],[0,13],[0,1]]

Output
[null,null,0,1,2,15,15,15,null,15]

Explanation
SnapshotArray snapshotArr = new SnapshotArray(1);
snapshotArr.set(0,15);
snapshotArr.snap();     // snap_id = 0
snapshotArr.snap();     // snap_id = 1
snapshotArr.snap();     // snap_id = 2
snapshotArr.get(0,2);   // return 15 (value at index 0 at snap_id 2)
snapshotArr.get(0,0);   // return 15 (value at index 0 at snap_id 0)
snapshotArr.get(0,1);   // return 15 (value at index 0 at snap_id 1)
snapshotArr.set(0,13);  // update current value
snapshotArr.get(0,1);   // return 15 (snap_id 1 still has old value)
```

## Constraints

- `1 <= length <= 5 * 10^4`
- `0 <= index < length`
- `0 <= snap_id < (the total number of times we call snap())`
- `0 <= val <= 10^9`
- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

## Key Insights

1. **Sparse Storage**: Don't copy entire array on each snapshot - most indices don't change
2. **Version History**: Each index needs to track its history of changes across snapshots
3. **Binary Search**: Use binary search to find the correct value for a given snap_id
4. **Lazy Snapshotting**: Only record changes, not entire array state
5. **Time-Based Lookup**: Getting a value at a specific snap_id is similar to time-based key-value lookup
6. **Default Values**: Indices not explicitly set have value 0

## Approach

### Solution 1: Array of Lists with Binary Search

**Data Structure:**
- Array of lists where each index stores a list of (snap_id, value) pairs
- Current snap_id counter

**Algorithm:**

1. **Constructor**:
   - Initialize array of empty lists (one per index)
   - Set snap_id counter to 0
   - Time: O(N) where N = length

2. **set(index, val)**:
   - If no entry exists for current snap_id at this index, append (snap_id, val)
   - If entry exists for current snap_id, update the value
   - Time: O(1) amortized

3. **snap()**:
   - Increment and return snap_id
   - Time: O(1)

4. **get(index, snap_id)**:
   - Binary search the list at index for largest snap_id <= requested snap_id
   - Return corresponding value, or 0 if not found
   - Time: O(log S) where S = number of snapshots for that index

**Space Complexity:**
- O(N + M) where N = array length, M = total number of set operations

### Solution 2: HashMap of HashMaps

**Alternative approach:**
- Use HashMap: snap_id -> HashMap: index -> value
- Each snapshot stores only changed values
- get() checks current and previous snapshots until value found

**Pros:** Intuitive structure
**Cons:** Less efficient for queries (no binary search benefit)

### Solution 3: Copy-on-Write (Naive)

**Approach:**
- Copy entire array on each snap()
- Store all snapshots

**Pros:** Simple implementation
**Cons:** O(N) space per snapshot, O(N) time per snap() - not scalable

## Implementation Details

### Efficient Set Operation

```python
def set(self, index, val):
    history = self.array[index]
    # If already modified in current snapshot, update value
    if history and history[-1][0] == self.snap_id:
        history[-1] = (self.snap_id, val)
    else:
        history.append((self.snap_id, val))
```

### Binary Search for Get

```python
def get(self, index, snap_id):
    history = self.array[index]
    if not history:
        return 0

    # Binary search for largest snap_id <= requested snap_id
    left, right = 0, len(history) - 1
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if history[mid][0] <= snap_id:
            result = history[mid][1]
            left = mid + 1
        else:
            right = mid - 1

    return result
```

## Edge Cases

1. Getting value before any set operations (should return 0)
2. Getting value for snap_id before the index was first modified
3. Multiple sets on same index in same snapshot
4. Snapping without any set operations
5. Getting value at the most recent snapshot
6. Array with length 1
7. Large snap_id values

## Common Mistakes

1. Copying entire array on snap() - too slow and memory intensive
2. Not using binary search for get() - linear search is too slow
3. Not handling default value 0 for unmodified indices
4. Storing redundant snapshots for unchanged values
5. Not optimizing for multiple sets in same snapshot before snap()
6. Off-by-one errors in binary search
7. Not considering sparse array access patterns

## Optimization Techniques

1. **Lazy Evaluation**: Only store changes, not full array copies
2. **Binary Search**: O(log S) lookup instead of O(S) iteration
3. **In-Place Update**: Update last entry if snap_id matches (avoid duplicates)
4. **Space Optimization**: Use arrays instead of objects for (snap_id, val) pairs
5. **Compression**: For indices that never change, don't store any history

## Time Complexity Summary

- `SnapshotArray(length)`: O(N)
- `set(index, val)`: O(1) amortized
- `snap()`: O(1)
- `get(index, snap_id)`: O(log S) where S = number of times index was modified

## Space Complexity

- O(N + M) where:
  - N = array length (initial allocation)
  - M = total number of set operations

## Related Problems

- LeetCode 1146: Snapshot Array (this problem)
- LeetCode 981: Time Based Key-Value Store
- LeetCode 1206: Design Skiplist
- LeetCode 716: Max Stack
- LeetCode 895: Maximum Frequency Stack
- Design problems involving versioning and history tracking

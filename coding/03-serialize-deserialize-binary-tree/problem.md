# 3. Serialize and Deserialize Binary Tree

**Difficulty**: Hard
**Category**: Tree, DFS, BFS, Design
**Similar to**: LeetCode 297

---

## Problem Statement

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Implement:**
- `serialize(root)`: Encodes a tree to a single string
- `deserialize(data)`: Decodes your encoded data to tree

---

## Examples

### Example 1:
```
Input: root = [1,2,3,null,null,4,5]

    1
   / \
  2   3
     / \
    4   5

Output: [1,2,3,null,null,4,5]
Explanation: Your serialize method should return a string that can be passed to deserialize to reconstruct the tree.
```

### Example 2:
```
Input: root = []
Output: []
```

### Example 3:
```
Input: root = [1]
Output: [1]
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`
- `-1000 <= Node.val <= 1000`

---

## Follow-up Questions

1. What if node values can contain the delimiter character?
2. How would you optimize for space if the tree is very sparse?
3. Can you support serialization of a binary tree with parent pointers?
4. How would you handle serialization of a forest (multiple trees)?

---

## Approach Hints

<details>
<summary>Hint 1 - DFS Preorder Traversal</summary>

Use preorder traversal (root → left → right):
```
serialize: "1,2,null,null,3,4,null,null,5,null,null"
```

**Serialize:**
1. If node is None, append "null"
2. Otherwise, append node value
3. Recursively serialize left subtree
4. Recursively serialize right subtree

**Deserialize:**
1. Split string into list
2. Use iterator/index to consume values
3. Read value: if "null", return None
4. Create node, recursively deserialize left and right

Time: O(n), Space: O(n)
</details>

<details>
<summary>Hint 2 - BFS Level-Order Traversal</summary>

Use level-order traversal (breadth-first):
```
serialize: "1,2,3,null,null,4,5,null,null,null,null"
```

**Serialize:**
1. Use queue, start with root
2. For each node: append value (or "null"), add children to queue
3. Can optimize by removing trailing nulls

**Deserialize:**
1. Split string into list
2. First value is root
3. Use queue to build tree level by level
4. For each parent, next two values are its children

Time: O(n), Space: O(n)
</details>

<details>
<summary>Hint 3 - Optimizations</summary>

**Space optimizations:**
1. Remove trailing nulls
2. Use shorter null representation: "#", "N"
3. For complete trees, can use array indexing

**Handling special cases:**
1. Empty tree: return empty string or special marker
2. Delimiter choice: comma, space, or custom
3. Negative numbers: ensure delimiter doesn't conflict

**Validation:**
1. Check if deserialized tree structure is valid
2. Handle malformed input
</details>

---

## Key Concepts to Review

1. **Tree Traversals**
   - Preorder: Root → Left → Right
   - Inorder: Left → Root → Right (can't uniquely reconstruct without additional info)
   - Postorder: Left → Right → Root
   - Level-order (BFS)

2. **Serialization Techniques**
   - String building and parsing
   - Delimiter handling
   - Null representation

3. **DFS vs BFS for Trees**
   - DFS: Simpler code, recursion
   - BFS: Level-by-level, queue

---

## Test Cases to Consider

1. Empty tree: `root = None`
2. Single node: `root = [1]`
3. Complete binary tree
4. Skewed tree (all left or all right)
5. Tree with negative values
6. Large tree (10^4 nodes)
7. Tree where values contain numbers that look like delimiters
8. Sparse tree (many nulls)

---

## Common Mistakes

1. ❌ Using inorder traversal alone (not unique without structure info)
2. ❌ Not handling null nodes properly
3. ❌ Delimiter conflicts with node values
4. ❌ Not maintaining state during deserialization (use iterator or index)
5. ❌ Forgetting to handle empty tree case
6. ❌ Off-by-one errors in level-order deserialization

---

## Implementation Tips

**Using iterator for deserialization:**
```python
def deserialize(self, data):
    def helper(nodes):
        val = next(nodes)
        if val == 'null':
            return None
        node = TreeNode(int(val))
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node

    return helper(iter(data.split(',')))
```

**Using index for deserialization:**
```python
def deserialize(self, data):
    self.index = 0
    def helper(values):
        if self.index >= len(values) or values[self.index] == 'null':
            self.index += 1
            return None
        node = TreeNode(int(values[self.index]))
        self.index += 1
        node.left = helper(values)
        node.right = helper(values)
        return node

    return helper(data.split(','))
```

---

## Related Problems

- Serialize and Deserialize BST (Medium)
- Encode and Decode Strings (Medium)
- Serialize and Deserialize N-ary Tree (Hard)
- Construct Binary Tree from Preorder and Inorder Traversal (Medium)

# Problem 25: Design In-Memory File System

## Difficulty: Hard

## Tags: HashMap, Tree, Design, String

## Problem Description

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

- **`FileSystem()`**: Initializes the object of the system.

- **`List<String> ls(String path)`**:
  - If `path` is a file path, returns a list that only contains this file's name.
  - If `path` is a directory path, returns the list of file and directory names in this directory.
  - The answer should be in lexicographic order.

- **`void mkdir(String path)`**: Makes a new directory according to the given `path`. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.

- **`void addContentToFile(String filePath, String content)`**:
  - If `filePath` does not exist, creates that file containing given `content`.
  - If `filePath` already exists, appends the given `content` to original content.

- **`String readContentFromFile(String filePath)`**: Returns the content in the file at `filePath`.

## Examples

### Example 1:

```
Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");                 // create directory /a/b/c
fileSystem.addContentToFile("/a/b/c/d", "hello");  // create file /a/b/c/d with content "hello"
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
```

### Example 2:

```
Input
["FileSystem", "mkdir", "mkdir", "ls", "ls", "mkdir", "ls"]
[[], ["/a"], ["/a/b"], ["/a"], ["/a/b"], ["/a/b/c"], ["/a/b"]]

Output
[null, null, null, ["b"], [], null, ["c"]]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.mkdir("/a");
fileSystem.mkdir("/a/b");
fileSystem.ls("/a");      // return ["b"]
fileSystem.ls("/a/b");    // return []
fileSystem.mkdir("/a/b/c");
fileSystem.ls("/a/b");    // return ["c"]
```

## Constraints

- `1 <= path.length, filePath.length <= 100`
- `path` and `filePath` are absolute paths which begin with `'/'` and do not end with `'/'` except that the path is just `"/"`.
- You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
- You can assume that all operations will be valid. For example, a directory cannot be deleted, renamed, or moved to another directory.
- `1 <= content.length <= 50`
- At most `300` calls will be made to `ls`, `mkdir`, `addContentToFile`, and `readContentFromFile`.

## Key Insights

1. **Tree Structure**: File system naturally forms a tree where directories are internal nodes and files are leaf nodes
2. **HashMap for Children**: Each node (directory) contains a HashMap mapping names to child nodes
3. **Node Types**: Need to distinguish between file and directory nodes
4. **Path Parsing**: Must parse paths by splitting on '/' character
5. **Lazy Creation**: When creating nested directories, parent directories should be created automatically
6. **Content Storage**: Files store string content, directories do not
7. **Lexicographic Sorting**: ls() results must be sorted alphabetically

## Approach

### Solution 1: Tree with HashMap Nodes

**Data Structure:**
```
class Node {
    boolean isFile;
    String content;  // only for files
    Map<String, Node> children;  // only for directories
}
```

**Algorithm:**

1. **ls(path)**:
   - Parse path to navigate to target node
   - If node is file: return list with just filename
   - If node is directory: return sorted list of children keys
   - Time: O(P + N log N) where P = path length, N = children count

2. **mkdir(path)**:
   - Parse path into components
   - For each component, create node if it doesn't exist
   - Time: O(P) where P = path length

3. **addContentToFile(filePath, content)**:
   - Navigate to parent directory (create if needed)
   - Find or create file node
   - Append content
   - Time: O(P + C) where P = path length, C = content length

4. **readContentFromFile(filePath)**:
   - Navigate to file node
   - Return stored content
   - Time: O(P) where P = path length

**Space Complexity:**
- O(N * P) where N = number of files/directories, P = average path depth

### Solution 2: Flat HashMap with Full Paths

**Alternative approach:**
- Use single HashMap mapping full path -> content/type
- Simpler but less memory efficient
- Harder to implement ls() efficiently

## Implementation Details

### Path Parsing

```python
def parse_path(path):
    if path == "/":
        return []
    return path.split("/")[1:]  # Skip first empty string
```

### Node Navigation

```python
def get_node(path):
    if path == "/":
        return root

    parts = path.split("/")[1:]
    node = root
    for part in parts:
        if part not in node.children:
            return None
        node = node.children[part]
    return node
```

### Creating Intermediate Directories

```python
def mkdir(path):
    parts = path.split("/")[1:]
    node = root
    for part in parts:
        if part not in node.children:
            node.children[part] = Node(isFile=False)
        node = node.children[part]
```

## Edge Cases

1. Root directory "/" listing
2. Creating nested directories in one call
3. Appending to existing file vs creating new file
4. Listing single file vs directory with same name prefix
5. Empty directory listing
6. Path with multiple '/' characters
7. Very deep directory structures

## Common Mistakes

1. Not sorting ls() results lexicographically
2. Not creating intermediate directories in mkdir()
3. Not handling root directory "/" as special case
4. Confusing file listing (returns [filename]) with directory listing (returns children)
5. Not properly splitting paths and handling leading '/'
6. Not distinguishing between file and directory nodes
7. Overwriting file content instead of appending

## Time Complexity Summary

- `ls(path)`: O(P + N log N) where P = path length, N = number of items in directory
- `mkdir(path)`: O(P) where P = path length
- `addContentToFile(filePath, content)`: O(P + C) where P = path length, C = content length
- `readContentFromFile(filePath)`: O(P) where P = path length

## Space Complexity

- O(N * P * M) where:
  - N = total number of files and directories
  - P = average path depth
  - M = average content size per file

## Related Problems

- LeetCode 588: Design In-Memory File System (this problem)
- LeetCode 208: Implement Trie (Prefix Tree)
- LeetCode 1166: Design File System
- LeetCode 635: Design Log Storage System
- Design problems involving tree structures and path navigation

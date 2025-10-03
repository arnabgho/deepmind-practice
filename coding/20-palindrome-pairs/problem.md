# 20. Palindrome Pairs

**Difficulty**: Hard
**Category**: Trie, String Manipulation, Hash Table
**Similar to**: LeetCode 336

---

## Problem Statement

You are given a **0-indexed** array of **unique** strings `words`.

A **palindrome pair** is a pair of integers `(i, j)` such that:
- `0 <= i, j < words.length`
- `i != j`
- `words[i] + words[j]` (the concatenation of the two strings) is a palindrome

Return an array of all the palindrome pairs of `words`.

You must write an algorithm with `O(n × k²)` time complexity, where `n` is the number of words and `k` is the average length of a word.

---

## Examples

### Example 1:
```
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
```

### Example 2:
```
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
```

### Example 3:
```
Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]
```

---

## Constraints

- `1 <= words.length <= 5000`
- `0 <= words[i].length <= 300`
- `words[i]` consists of lowercase English letters
- All strings in `words` are **unique**

---

## Follow-up Questions

1. How would you optimize for very long strings?
2. Can you find palindrome triples (three words)?
3. What if words can be repeated?
4. How to find the longest palindrome pair?

---

## Approach Hints

<details>
<summary>Hint 1 - Brute Force</summary>

Check every pair and verify if concatenation is palindrome:
```python
result = []
for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            concat = words[i] + words[j]
            if concat == concat[::-1]:
                result.append([i, j])
```

- Time: O(n² × k) where k is average word length
- Space: O(1)
- Too slow for constraints!
</details>

<details>
<summary>Hint 2 - Hash Map with String Analysis</summary>

For each word, consider three cases:
1. **Case 1**: Another word is the reverse of current word
2. **Case 2**: Split word into left and right:
   - If left is palindrome, check if reverse of right exists
3. **Case 3**: If right is palindrome, check if reverse of left exists

Use hash map to store word -> index mapping for O(1) lookup.

- Time: O(n × k²)
- Space: O(n × k)
</details>

<details>
<summary>Hint 3 - Detailed Algorithm</summary>

```python
word_map = {word: i for i, word in enumerate(words)}
result = []

for i, word in enumerate(words):
    # Case 1: Check for complete reverse
    reverse = word[::-1]
    if reverse in word_map and word_map[reverse] != i:
        result.append([i, word_map[reverse]])

    # Case 2 & 3: Check all splits
    for j in range(len(word) + 1):
        left, right = word[:j], word[j:]

        # If left is palindrome, find reverse of right
        if is_palindrome(left):
            rev_right = right[::-1]
            if rev_right in word_map and word_map[rev_right] != i:
                result.append([word_map[rev_right], i])

        # If right is palindrome, find reverse of left
        if j != len(word) and is_palindrome(right):
            rev_left = left[::-1]
            if rev_left in word_map and word_map[rev_left] != i:
                result.append([i, word_map[rev_left]])
```

- Time: O(n × k²)
- Space: O(n × k)
</details>

<details>
<summary>Hint 4 - Trie Optimization</summary>

Build a Trie of reversed words:
1. For each word, insert its reverse into Trie
2. While inserting, also store indices where suffix is a palindrome
3. For each word, search in Trie:
   - If we finish the word and reach a node with indices, those are matches
   - If we finish traversing but word continues, check if remaining is palindrome

Trie can optimize prefix matching but doesn't improve worst-case complexity.

- Time: O(n × k²)
- Space: O(n × k)
</details>

---

## Key Concepts to Review

1. **String Palindrome Check**
   - Two-pointer technique
   - Reverse and compare
   - Manacher's algorithm (advanced)

2. **Trie (Prefix Tree)**
   - Insertion and search
   - Storing additional info at nodes
   - Suffix/prefix matching

3. **Hash Table Optimization**
   - Word to index mapping
   - O(1) lookup for reverse
   - Handling duplicates

4. **String Splitting**
   - Enumerate all split positions
   - Prefix and suffix analysis
   - Avoiding duplicate pairs

5. **Edge Cases**
   - Empty strings
   - Single character strings
   - Complete palindromes
   - No valid pairs

---

## Test Cases to Consider

1. Empty string: `words = ["a", ""]`
2. No pairs: `words = ["abc", "def", "ghi"]`
3. All palindromes: `words = ["aa", "bb", "cc"]`
4. Single word: `words = ["abc"]`
5. Two words reverse of each other: `words = ["abc", "cba"]`
6. Multiple valid pairs per word
7. Long words (length 300)
8. Maximum words (5000)
9. All single characters
10. Words with common prefixes/suffixes

### Example Walkthrough:
```
words = ["abcd", "dcba", "lls", "s", "sssll"]

For "abcd":
- Reverse "dcba" exists -> [0,1]

For "dcba":
- Reverse "abcd" exists -> [1,0]

For "lls":
- Split: "" + "lls" (right is palindrome)
  - Need reverse of left "" at front: "" exists? No
- Split: "l" + "ls"
- Split: "ll" + "s" (left "ll" is palindrome)
  - Need reverse of right "s" at front: "s" exists at index 3 -> [3,2]

For "s":
- Split: "" + "s" (right is palindrome)
  - Need reverse of left "" at front: "" exists? No
- Split: "s" + ""

For "sssll":
- Split: "ss" + "sll" (left "ss" is palindrome)
  - Need reverse of right "sll" at front: "lls" exists at index 2 -> [2,4]
```

---

## Related Problems

- Longest Palindromic Substring (Medium)
- Palindrome Partitioning II (Hard)
- Shortest Palindrome (Hard)
- Palindrome Partitioning (Medium)
- Valid Palindrome II (Easy)
- Longest Palindromic Subsequence (Medium)

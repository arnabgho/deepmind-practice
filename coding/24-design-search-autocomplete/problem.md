# Problem 24: Design Search Autocomplete System

## Difficulty: Hard

## Tags: Trie, Priority Queue, Streaming, Design

## Problem Description

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array `sentences` and an integer array `times` both of length n where `sentences[i]` is a previously typed sentence and `times[i]` is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

- The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
- The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
- If less than 3 hot sentences exist, return as many as you can.
- When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Your system should:

**`AutocompleteSystem(String[] sentences, int[] times)`**: Initializes the system with the given `sentences` and their corresponding `times`.

**`List<String> input(char c)`**: This indicates that the user typed the character `c`.
- Returns an empty list `[]` if `c == '#'`.
- Otherwise, returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. Note that the user's input ends with the character `#`.

## Examples

### Example 1:

```
Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]

Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]
                // There are four sentences that have prefix "i". Among them, "iroman" and "i love leetcode" have same hot degree.
                // Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "iroman".
                // Also we only need to output top 3 hot sentences, so "iroman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]
                // There are only two sentences that have prefix "i ".
obj.input("a"); // return []
                // There are no sentences that have prefix "i a".
obj.input("#"); // return []
                // The user finished the input, the sentence "i a" should be saved as a historical sentence in system.
                // And the following input will be counted as a new search.
```

## Constraints

- `n == sentences.length`
- `n == times.length`
- `1 <= n <= 100`
- `1 <= sentences[i].length <= 100`
- `1 <= times[i] <= 50`
- `c` is a lowercase English letter, a hash '#', or space ' '.
- Each tested sentence will be a sequence of characters `c` that end with the character '#'.
- Each tested sentence will have a length in the range `[1, 200]`.
- The words in each input sentence are separated by single spaces.
- At most `5000` calls will be made to `input`.

## Key Insights

1. **Trie Structure**: Use a Trie to efficiently store and retrieve sentences with common prefixes
2. **Hot Degree Tracking**: Each Trie node or sentence mapping needs to track frequency counts
3. **Priority Queue**: Use a heap/priority queue to maintain top 3 results efficiently
4. **Streaming Input**: Track the current input prefix as characters stream in
5. **Custom Sorting**: Implement custom comparator for sorting by frequency (descending) then ASCII order (ascending)
6. **State Management**: Maintain current search state between input() calls until '#' is encountered

## Approach

### Solution 1: Trie + HashMap + Priority Queue

**Data Structures:**
- Trie to store sentences for prefix matching
- HashMap to store sentence -> frequency mapping
- String buffer to track current input
- Priority queue for selecting top 3 results

**Algorithm:**
1. **Initialization**:
   - Build Trie from all sentences
   - Create frequency map from sentences and times

2. **Input Processing**:
   - If `c == '#'`: Save current sentence to Trie and frequency map, reset buffer, return []
   - Otherwise: Append c to current buffer
   - Find all sentences matching current prefix
   - Use priority queue to select top 3 by (frequency desc, ASCII asc)
   - Return top 3 results

**Time Complexity:**
- Initialization: O(N * L) where N = number of sentences, L = average length
- Input: O(M * log(3)) where M = number of matching sentences (usually small)
  - Priority queue maintains only 3 elements, so operations are O(log 3) = O(1)

**Space Complexity:**
- O(N * L) for Trie and frequency map

### Solution 2: HashMap Only with Prefix Search

**Alternative approach without Trie:**
- Store all sentences in HashMap with frequencies
- For each input, iterate through all sentences to find prefix matches
- Sort and return top 3

This is simpler but less efficient for large datasets.

**Time Complexity:**
- Input: O(N * L + M log M) where M = matching sentences

## Edge Cases

1. No matching sentences for a prefix
2. Less than 3 matching sentences
3. Multiple sentences with same frequency (use ASCII ordering)
4. Special characters (space, #)
5. Empty input or single character searches
6. New sentence that already exists (increment frequency)

## Common Mistakes

1. Not handling ASCII ordering correctly when frequencies are equal
2. Forgetting to reset input buffer after '#'
3. Not properly storing new sentences typed by user
4. Inefficient sorting on every input character
5. Not handling space character correctly in prefix matching

## Related Problems

- LeetCode 208: Implement Trie (Prefix Tree)
- LeetCode 211: Design Add and Search Words Data Structure
- LeetCode 212: Word Search II
- LeetCode 642: Design Search Autocomplete System (this problem)
- LeetCode 692: Top K Frequent Words

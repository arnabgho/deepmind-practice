# Getting Started with DeepMind Coding Interview Prep

Welcome to your structured 30-problem coding interview preparation curriculum for Google DeepMind!

---

## 📁 Directory Structure

```
coding/
├── README.md                      # Main index with progress tracker
├── GETTING_STARTED.md            # This file - start here!
├── patterns.md                    # Pattern recognition guide
├── complexity-reference.md        # Big-O complexity cheat sheet
│
├── 01-merge-k-sorted-lists/
│   ├── problem.md                # Problem statement & hints
│   ├── solution.py               # Your solution (template provided)
│   ├── test.py                   # Test cases (template provided)
│   └── notes.md                  # Your notes & learnings
│
├── 02-lru-cache/
│   └── ... (same structure)
│
└── ... (30 problems total)
```

---

## 🚀 Quick Start

### 1. Start with Problem 1
```bash
cd 01-merge-k-sorted-lists
```

### 2. Read the Problem
```bash
cat problem.md  # or open in your editor
```

### 3. Attempt Solution (45-60 minutes)
- Try to solve without hints first
- Think about edge cases
- Consider time/space complexity

### 4. Implement in `solution.py`
```python
# Template is already provided - fill in the TODO sections
class Solution:
    def solve(self, ...):
        # Your implementation here
        pass
```

### 5. Write Test Cases in `test.py`
```bash
python test.py
```

### 6. Document Your Learnings in `notes.md`
- What approach did you use?
- What was the complexity?
- What mistakes did you make?
- Alternative solutions?

### 7. Update Progress in README.md
Change ⬜ to ✅ for completed problems

---

## 📚 Study Approach

### Recommended Schedule

**Week 1-2: Phase 1 (Problems 1-8) - Foundations**
- Goal: 1 problem per day
- Focus: Core data structures, build confidence
- Don't rush - understanding > speed

**Week 3-4: Phase 2 (Problems 9-15) - Advanced Single-Concept**
- Goal: 1 problem per day
- Focus: Deep dive into complex applications

**Week 5-6: Phase 3 (Problems 16-23) - Hybrid Problems**
- Goal: 1 problem per day
- Focus: Combining techniques (DP + graphs, etc.)

**Week 7: Phase 4 (Problems 24-27) - Novel Data Structures**
- Goal: 1 problem per day
- Focus: System design, custom structures

**Week 8: Phase 5 (Problems 28-30) - Advanced Combinations**
- Goal: 1 problem per day
- Focus: Most challenging problems

**Week 9-10: Review & Mock Interviews**
- Redo problems without looking at solutions
- Time yourself (45 minutes each)
- Practice explaining out loud

---

## 🎯 How to Approach Each Problem

### Before Coding (10-15 minutes)

1. **Understand the problem**
   - Read carefully, identify input/output
   - What are we optimizing? (time, space, count, etc.)
   - What are the constraints? (n ≤ 10^4 means O(n²) is ok, n ≤ 10^6 needs O(n log n))

2. **Think about examples**
   - Work through example by hand
   - Think of edge cases
   - Draw diagrams if helpful

3. **Identify patterns**
   - Check [patterns.md](./patterns.md)
   - Does this look like BFS? DP? Greedy?
   - What data structures might help?

4. **Explain your approach**
   - Say it out loud (interview simulation)
   - What's the time/space complexity?
   - Are there tradeoffs?

### During Coding (20-30 minutes)

5. **Start simple**
   - Write brute force first if needed
   - Then optimize
   - Use helper functions for clarity

6. **Test as you go**
   - Run test cases frequently
   - Add print statements to debug
   - Think about edge cases

### After Coding (10-15 minutes)

7. **Analyze complexity**
   - Count loops, recursive calls
   - Check [complexity-reference.md](./complexity-reference.md)
   - Can it be optimized further?

8. **Document learnings**
   - What patterns did you use?
   - What mistakes did you make?
   - What would you do differently?

---

## 🔍 Using the Resources

### [patterns.md](./patterns.md)
**When to use:** When you're stuck identifying which approach to use

Contains:
- Pattern recognition for different problem types
- When to use each data structure
- Template code for common patterns
- Problem-solving framework

### [complexity-reference.md](./complexity-reference.md)
**When to use:** When analyzing your solution's complexity

Contains:
- Common time complexities explained
- Data structure operation costs
- Algorithm complexity reference
- Quick lookup tables

### [README.md](./README.md)
**When to use:** For overview and progress tracking

Contains:
- Full problem list with categories
- Progress tracker
- Quick summary of each problem
- Data structure/algorithm coverage map

---

## 💡 Tips for Success

### General Tips
1. **Don't look at solutions too quickly** - Struggle is where learning happens
2. **Practice explaining out loud** - You'll do this in real interviews
3. **Focus on patterns, not memorization** - Learn to recognize problem types
4. **Do problems in order** - They're designed with increasing complexity
5. **Take breaks** - Your brain needs time to consolidate learning

### When Stuck (after 30-45 minutes)
1. Read "Hint 1" in problem.md (usually high-level approach)
2. Still stuck? Read "Hint 2" (more specific)
3. Still stuck? Read full solution, then try again tomorrow
4. **Don't copy code** - Type it yourself, understand every line

### Before Interview
1. Redo 5-10 problems without looking at solutions
2. Practice with timer (45 minutes per problem)
3. Review patterns.md - common patterns should be automatic
4. Review complexity-reference.md - be able to analyze on the fly

---

## 🧪 Running Tests

### Run Single Test File
```bash
cd 01-merge-k-sorted-lists
python test.py
```

### Run with Verbose Output
```bash
python test.py -v
```

### Run Specific Test
```bash
python test.py TestMergeKSortedLists.test_example1
```

### Add More Tests
Edit `test.py` and add more test methods:
```python
def test_my_edge_case(self):
    result = self.solution.solve(...)
    self.assertEqual(result, expected)
```

---

## 📊 Progress Tracking

### Update README.md After Each Problem
Change status from:
```markdown
**Status**: ⬜ Not Started
```
to:
```markdown
**Status**: ✅ Completed
```

### Track Your Stats
Keep track in notes.md:
- Time taken (first attempt)
- Number of hints used
- Bugs encountered
- Would you get this right in an interview?

---

## 🎓 Interview Simulation

### Once You've Done 10-15 Problems

**Practice like a real interview:**

1. **Pick a problem you solved 1+ weeks ago**
2. **Set timer: 45 minutes**
3. **Open empty solution.py**
4. **Pretend interviewer is watching:**
   - Explain your approach out loud before coding
   - Talk through your thought process while coding
   - Mention time/space complexity
   - Discuss trade-offs

5. **After timer:**
   - Did you finish?
   - Was code bug-free?
   - Did you analyze complexity correctly?
   - How was your communication?

---

## 🔗 Problem Dependencies

Some problems build on concepts from earlier ones:

- **Problem 2 (LRU Cache)** uses concepts helpful for **Problem 26 (Snapshot Array)**
- **Problem 7 (Union Find)** is foundational - master this early
- **Problem 9 (DFS + Memo)** prepares you for **Problem 17 (3D DP)**
- **Problem 11 (Monotonic Deque)** prepares for **Problem 21 (Monotonic Stack)**
- **Problem 14 (Topological Sort)** prepares for **Problem 18 (Topo + DP)**

**Recommendation:** Do problems in order to build on previous concepts.

---

## 🆘 When to Ask for Help

**Absolutely stuck after 60+ minutes?**
1. Check patterns.md for similar problems
2. Read problem.md hints (in order)
3. Search for the algorithm name (e.g., "Dijkstra's algorithm")
4. Read solution, understand it, then code from memory
5. Do similar problem next day without hints

**Remember:** Struggling is normal and valuable. Some problems will take multiple attempts!

---

## 📈 After Completing All 30 Problems

### Review Phase (2 weeks)
1. **Redo problems** without looking at solutions
2. **Focus on patterns** - can you identify problem type quickly?
3. **Time yourself** - aim for 45 minutes per problem
4. **Mock interviews** with friends or online platforms

### What You'll Have Learned
✅ Priority queues, heaps, and greedy algorithms
✅ Union Find with path compression
✅ DFS, BFS, and graph algorithms
✅ Dijkstra's algorithm and variations
✅ Dynamic programming (1D, 2D, 3D, bitmask, tree)
✅ Monotonic stack and deque
✅ Topological sort
✅ Trie and string algorithms
✅ Custom data structure design
✅ State-space search and optimization

### You'll Be Ready For
- Google DeepMind coding interviews
- LeetCode Hard problems
- Novel problem types combining multiple algorithms
- System design with custom data structures

---

## 🎉 Good Luck!

Remember:
- **Consistency > Intensity** - 1 problem per day beats 10 problems once a week
- **Understanding > Memorization** - Learn patterns, not specific solutions
- **Communication matters** - Practice explaining your thought process
- **Mistakes are learning** - Debug, analyze, improve

**You've got this! Start with Problem 1 and take it one step at a time.**

---

## 📞 Need Help?

- Check `problem.md` for hints
- Review `patterns.md` for approaches
- Study `complexity-reference.md` for analysis
- Revisit earlier problems for foundational concepts

Happy coding! 🚀

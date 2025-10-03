# Getting Started with DeepMind ML Interview Prep

Welcome to your structured 20-topic machine learning fundamentals curriculum for Google DeepMind!

---

## Directory Structure

```
ml/
├── README.md                      # Main index with progress tracker
├── GETTING_STARTED.md            # This file - start here!
├── concepts-reference.md          # Quick formula lookup
├── foundations-guide.md           # Deep dive into calculus & statistics
│
├── 01-derivatives-gradients/
│   ├── topic.md                  # Theory, derivations, examples
│   ├── exercises.py              # Coding exercises with tests
│   ├── solutions.py              # Complete solutions
│   └── notes.md                  # Your learning notes
│
├── 02-chain-rule-backprop/
│   └── ... (same structure)
│
└── ... (20 topics total)
```

---

## Quick Start

### 1. Assess Your Prerequisites

**Do you need calculus review?**
```bash
cat foundations-guide.md  # Read if you need calculus/stats refresher
```

**Want a formula reference?**
```bash
cat concepts-reference.md  # Keep this open for quick lookups
```

### 2. Start with Topic 1
```bash
cd 01-derivatives-gradients
cat topic.md
```

### 3. Study the Theory (30-45 min)
- Read the theory section
- Study the Mermaid diagrams
- Work through mathematical derivations by hand
- Understand the intuition, not just formulas

### 4. Complete Exercises (30-45 min)
```bash
python exercises.py  # Run to see failing tests
```

Edit `exercises.py` and implement the functions:
```python
def compute_gradient(f, x):
    # TODO: Implement
    pass
```

Run again until all tests pass:
```bash
python exercises.py
```

### 5. Review Solutions
```bash
cat solutions.py  # Compare with your implementation
```

### 6. Document Learning (10-15 min)
Edit `notes.md`:
- Key insights
- Formulas to remember
- Confusing points (revisit these)
- Connection to previous topics

### 7. Update Progress
Update status in `ml/README.md`:
```markdown
**Status**: ⬜ Not Started  →  **Status**: ✅ Completed
```

---

## Study Approach

### For Theory-Heavy Topics (Topics 1-5, 13-17)

**Focus on understanding WHY, not just WHAT**

1. **First pass (15 min)**: Skim the entire topic.md
2. **Second pass (30 min)**: Read deeply, work through derivations
3. **Third pass (20 min)**: Implement concepts in code
4. **Practice (15 min)**: Explain concept out loud without notes

### For Implementation-Heavy Topics (Topics 6-12, 18-20)

**Focus on building intuition through code**

1. **Understand the theory (20 min)**: Read topic.md
2. **Implement from scratch (40 min)**: Complete exercises.py using only NumPy
3. **Test thoroughly (15 min)**: Add your own test cases
4. **Compare (10 min)**: Review solutions.py for best practices

---

## Recommended Schedules

### 4-Week Intensive Plan (4-5 hours/day)

**Week 1: Mathematical Foundations**
- Mon: Topic 1 (Derivatives & Gradients)
- Tue: Topic 2 (Chain Rule & Backprop Math)
- Wed: Topic 3 (Partial Derivatives & Jacobians)
- Thu: Topic 4 (Probability & Statistics)
- Fri: Topic 5 (Maximum Likelihood Estimation)
- Weekend: Review week 1, redo challenging parts

**Week 2: Deep Learning Fundamentals (Part 1)**
- Mon: Topic 6 (Neural Network Forward Pass)
- Tue: Topic 7 (Backpropagation Algorithm)
- Wed: Topic 8 (Activation Functions)
- Thu: Topic 9 (Loss Functions)
- Fri: Topic 10 (Optimization Algorithms)
- Weekend: Implement a full neural network from scratch

**Week 3: Deep Learning Fundamentals (Part 2) + Advanced**
- Mon: Topic 11 (Weight Initialization)
- Tue: Topic 12 (Regularization)
- Wed: Topic 13 (Batch/Layer Normalization)
- Thu: Topic 14 (CNNs Mathematics)
- Fri: Topic 15 (RNNs & Gradient Flow)
- Weekend: Review and consolidate weeks 2-3

**Week 4: Advanced + Practical**
- Mon: Topic 16 (Attention Mechanisms)
- Tue: Topic 17 (Transformers)
- Wed: Topic 18 (Bias-Variance Tradeoff)
- Thu: Topic 19 (Evaluation Metrics)
- Fri: Topic 20 (Model Debugging)
- Weekend: Full review, practice explaining all concepts

### 6-Week Comfortable Plan (2-3 hours/day)

**Weeks 1-2: Phase 1** (Topics 1-5)
- 2-3 topics per week
- Deep focus on mathematical foundations
- Work through all derivations multiple times

**Weeks 3-4: Phase 2** (Topics 6-12)
- 3-4 topics per week
- Implement everything from scratch
- Build complete neural network by end of week 4

**Week 5: Phase 3** (Topics 13-17)
- 1 topic per day
- Focus on modern architectures
- Understand attention mechanisms deeply

**Week 6: Phase 4 + Review** (Topics 18-20)
- First 3 days: Complete remaining topics
- Last 2 days: Full curriculum review
- Weekend: Mock interview practice

---

## How to Approach Each Topic

### Before Starting (5 min)

1. **Review prerequisites**
   - Check if topic builds on previous topics
   - Review relevant formulas in concepts-reference.md
   - Have paper and pen ready for derivations

2. **Set learning goals**
   - What should I understand after this topic?
   - What can I implement?
   - What interview questions can I answer?

### During Study (60-90 min)

3. **Theory first (30-45 min)**
   - Read topic.md completely
   - Study Mermaid diagrams carefully
   - Work through derivations by hand
   - Don't move forward if confused

4. **Code second (30-45 min)**
   - Implement exercises without looking at solutions
   - Use only NumPy, no deep learning frameworks
   - Test your implementation thoroughly
   - Debug and understand errors

### After Completing (15-20 min)

5. **Consolidate learning**
   - Compare your code with solutions.py
   - Document key insights in notes.md
   - Try explaining concept without notes
   - Identify what needs more review

6. **Connect concepts**
   - How does this relate to previous topics?
   - What concepts will this enable later?
   - Where would you use this in practice?

---

## Using the Resources

### topic.md Structure

Each topic.md contains:

1. **Overview** - High-level intuition
2. **Mathematical Foundation** - Formal definitions and derivations
3. **Visual Explanations** - Mermaid diagrams
4. **Examples** - Concrete worked examples
5. **Implementation Notes** - How to code this
6. **Common Mistakes** - Pitfalls to avoid
7. **Interview Questions** - Practice questions with answers
8. **Further Reading** - Resources for deeper understanding

### exercises.py Structure

```python
# Each exercise file contains:

import numpy as np
import unittest

# Function stubs for you to implement
def function_to_implement():
    """
    Detailed docstring explaining:
    - What to implement
    - Input/output specifications
    - Hints for implementation
    """
    # TODO: Your implementation here
    pass

# Unit tests to verify your implementation
class TestExercises(unittest.TestCase):
    def test_basic_case(self):
        # Test cases provided
        pass

    def test_edge_case(self):
        # Edge case tests
        pass

if __name__ == '__main__':
    unittest.main()
```

### solutions.py Structure

```python
# Complete implementations with:
# - Best practices
# - Explanatory comments
# - Multiple approaches when applicable
# - Complexity analysis

def function_implementation():
    """
    Complete solution with explanation.

    Time Complexity: O(...)
    Space Complexity: O(...)
    """
    # Implementation with detailed comments
    pass
```

---

## Mathematical Prerequisites

### Required Knowledge

You should be comfortable with:

**Basic Calculus**
- Derivatives of polynomials, exponentials, logarithms
- Chain rule
- Partial derivatives

**Linear Algebra**
- Matrix multiplication
- Matrix/vector dimensions
- Dot products

**Probability**
- Basic probability rules
- Common distributions (normal, uniform)
- Expectation and variance

### If You Need Review

```bash
# Comprehensive review of prerequisites
cat foundations-guide.md

# Quick formula reference
cat concepts-reference.md
```

**Don't skip foundations!** If calculus/statistics are rusty, spend extra time on Phase 1.

---

## Tips for Success

### Study Habits

**Do's ✓**
- Write out derivations by hand
- Implement from scratch (no copy-paste)
- Explain concepts out loud (Feynman technique)
- Connect theory to code
- Take breaks (Pomodoro technique)
- Review previous topics regularly

**Don'ts ✗**
- Don't just read passively
- Don't skip mathematical derivations
- Don't use deep learning frameworks for exercises
- Don't move on if confused
- Don't cram - consistent study beats intensive marathons

### When Stuck

**After 30 minutes of struggle:**

1. Re-read relevant section in topic.md
2. Check concepts-reference.md for formulas
3. Review related previous topics
4. Draw diagrams to visualize
5. Take a break and return with fresh eyes

**Still stuck after 1 hour?**

1. Look at solutions.py hints (don't copy code)
2. Search for the specific concept online
3. Review foundations-guide.md for math review
4. Move on and return tomorrow with fresh perspective

**Remember**: Struggling is part of learning. Don't get discouraged!

---

## From Theory to Implementation

### Understanding the Connection

Each mathematical concept has a code implementation:

| Math Concept | Code Implementation |
|-------------|-------------------|
| Derivative ∂f/∂x | Gradient computation |
| Chain rule | Backpropagation |
| Matrix multiplication | np.dot() or @ |
| Summation Σ | np.sum() |
| Element-wise operation | NumPy broadcasting |
| Argmax | np.argmax() |

### Implementation Best Practices

1. **Start with dimensions**
   ```python
   # Always know your shapes!
   X.shape  # (batch_size, input_dim)
   W.shape  # (input_dim, output_dim)
   y.shape  # (batch_size, output_dim)
   ```

2. **Verify with simple examples**
   ```python
   # Test with small inputs first
   X = np.array([[1, 2], [3, 4]])  # 2x2 matrix
   # Work through calculation by hand
   # Verify code matches hand calculation
   ```

3. **Check gradient numerically**
   ```python
   # Numerical gradient checking
   def numerical_gradient(f, x, eps=1e-7):
       grad = np.zeros_like(x)
       for i in range(x.size):
           x[i] += eps
           fxh = f(x)
           x[i] -= 2*eps
           fxl = f(x)
           x[i] += eps
           grad[i] = (fxh - fxl) / (2*eps)
       return grad
   ```

---

## Interview Preparation

### Types of ML Interview Questions

**1. Conceptual Understanding**
- "Explain backpropagation"
- "Why does batch normalization help?"
- "What's the difference between L1 and L2 regularization?"

**2. Mathematical Derivations**
- "Derive the gradient of sigmoid function"
- "Show the backprop equations for a 2-layer network"
- "Compute the gradient of cross-entropy loss"

**3. Implementation Questions**
- "Implement softmax from scratch"
- "Code the forward pass of a conv layer"
- "Write gradient descent optimizer"

**4. Practical Problem-Solving**
- "Your model isn't converging, what could be wrong?"
- "How would you detect overfitting?"
- "When would you use which optimizer?"

### Preparation Strategy

**3 Weeks Before Interview**
- Complete all 20 topics
- Focus on weak areas
- Redo key derivations

**2 Weeks Before**
- Review all topic.md files
- Practice whiteboard derivations
- Explain concepts out loud

**1 Week Before**
- Review concepts-reference.md daily
- Practice common interview questions from each topic
- Mock interview with friend (explain concepts on whiteboard)

**3 Days Before**
- Light review of key concepts
- Review your notes.md files
- Practice confidence-building exercises

**1 Day Before**
- Quick skim of concepts-reference.md
- Prepare questions for interviewer
- Get good rest

### Mock Interview Practice

**After completing 10+ topics**, practice like a real interview:

1. **Pick a topic you studied 1+ weeks ago**
2. **Set timer: 20-30 minutes**
3. **Whiteboard/paper only** (no computer)
4. **Explain as if teaching**:
   - Start with intuition
   - Show mathematical derivation
   - Discuss implementation
   - Mention practical considerations

5. **Self-evaluate**:
   - Was explanation clear?
   - Did you remember key formulas?
   - Could you derive from first principles?
   - Did you connect theory to practice?

---

## Combining with Coding Prep

### Parallel Study Strategy

**Morning (2-3 hours): Coding Prep**
- Fresh mind for algorithm problems
- 1-2 LeetCode problems
- Focus on problem-solving

**Afternoon/Evening (2-3 hours): ML Prep**
- Theory and derivations
- 1 ML topic
- Focus on understanding

**Benefits**:
- Different types of thinking (algorithmic vs mathematical)
- Prevents burnout from single topic
- Complete preparation for DeepMind interview

### Weekly Balance

**Weekdays**:
- Morning: Coding problem
- Evening: ML topic

**Weekends**:
- Saturday: Review coding patterns + ML review
- Sunday: Mock interviews for both

---

## Progress Tracking

### After Each Topic

Update `ml/README.md`:
```markdown
### 01. Derivatives & Gradients
**Status**: ⬜ Not Started  →  **Status**: ✅ Completed
```

### In Your notes.md

Track:
- **Time spent**: How long did this take?
- **Difficulty**: Easy / Medium / Hard
- **Confidence**: Could you explain this in an interview?
- **Review needed**: Flag topics that need more review

### Weekly Review

Every Sunday, ask yourself:
- Can I explain each completed topic without notes?
- Can I derive key equations?
- Can I implement concepts from scratch?
- Which topics need more work?

---

## Common Challenges & Solutions

### Challenge 1: "Math is too hard"

**Solution**:
- Spend extra time on foundations-guide.md
- Work through derivations multiple times
- Use visual diagrams (Mermaid)
- Connect to concrete code examples
- Remember: Understanding > memorization

### Challenge 2: "Can't implement from scratch"

**Solution**:
- Start with simpler version
- Test with small examples
- Check dimensions frequently
- Compare with mathematical equations
- Review solutions.py for hints

### Challenge 3: "Forgetting previous topics"

**Solution**:
- Review notes.md files regularly
- Redo key derivations weekly
- Explain concepts to others
- Connect new topics to old ones
- Use spaced repetition

### Challenge 4: "Not enough time"

**Solution**:
- Focus on Phase 1 & Phase 2 first (core concepts)
- Study Phase 3 as time permits
- Quality > quantity (understand 10 topics deeply > skim 20)
- Use concepts-reference.md for quick review

---

## What Success Looks Like

### After Phase 1 (Topics 1-5)
✓ Can explain gradient descent geometrically
✓ Can derive simple derivatives
✓ Understand backpropagation mathematics
✓ Comfortable with basic probability

### After Phase 2 (Topics 6-12)
✓ Can implement neural network from scratch
✓ Understand all components (forward, backward, optimization)
✓ Can explain why techniques work (not just what they do)
✓ Can debug training issues

### After Phase 3 (Topics 13-17)
✓ Understand modern architectures (CNNs, RNNs, Transformers)
✓ Can explain attention mechanisms
✓ Know when to use which architecture
✓ Understand normalization techniques

### After Phase 4 (Topics 18-20)
✓ Can diagnose model issues
✓ Know how to improve performance
✓ Understand evaluation metrics
✓ Can discuss tradeoffs

---

## Ready to Start?

### Your First Steps:

1. **Assess prerequisites**: Do you need math review?
   ```bash
   cat foundations-guide.md
   ```

2. **Bookmark formula reference**:
   ```bash
   cat concepts-reference.md
   ```

3. **Read the full topic list**:
   ```bash
   cat README.md
   ```

4. **Begin Topic 1**:
   ```bash
   cd 01-derivatives-gradients
   cat topic.md
   ```

---

## Additional Tips

### For Visual Learners
- Study Mermaid diagrams carefully
- Draw your own diagrams
- Visualize gradient flow
- Plot functions and their derivatives

### For Hands-On Learners
- Code examples while reading theory
- Experiment with different parameters
- Break things intentionally to understand limits
- Build mini-projects combining multiple topics

### For Theory-First Learners
- Read topic.md multiple times before coding
- Work through derivations completely
- Understand proofs
- Connect to theoretical foundations

---

**You've got this! Start with Topic 1 and take it one concept at a time.**

**Good luck with your Google DeepMind ML interview preparation!**

---

## Need Help?

- Check topic.md for detailed explanations
- Review concepts-reference.md for formulas
- Study foundations-guide.md for prerequisite math
- Review related topics for connections
- Take breaks and return with fresh perspective

Happy learning!

# Mathematical Foundations for Deep Learning

A comprehensive review of calculus and statistics fundamentals needed for ML interviews.

**Use this guide if you need to refresh mathematical prerequisites!**

---

## Table of Contents

1. [Calculus Foundations](#calculus-foundations)
2. [Multivariable Calculus](#multivariable-calculus)
3. [Optimization Basics](#optimization-basics)
4. [Linear Algebra Essentials](#linear-algebra-essentials)
5. [Probability Theory](#probability-theory)
6. [Statistics Fundamentals](#statistics-fundamentals)
7. [Information Theory Basics](#information-theory-basics)

---

## Calculus Foundations

### What is a Derivative?

**Intuition**: Rate of change, slope of tangent line

**Formal definition**:
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

**Geometric interpretation**: Slope of the tangent line at point $x$

**Physical interpretation**: Instantaneous rate of change

### Why Derivatives Matter in ML

- **Gradients** tell us how to update parameters to reduce loss
- **Backpropagation** is repeated application of the chain rule
- **Optimization** uses derivatives to find minima

### Common Derivatives

**Power rule**:
$$\frac{d}{dx}(x^n) = nx^{n-1}$$

**Example**: $\frac{d}{dx}(x^3) = 3x^2$

**Exponential**:
$$\frac{d}{dx}(e^x) = e^x$$

**Natural log**:
$$\frac{d}{dx}(\ln x) = \frac{1}{x}$$

**Trigonometric**:
$$\frac{d}{dx}(\sin x) = \cos x$$
$$\frac{d}{dx}(\cos x) = -\sin x$$

### Rules of Differentiation

**Sum rule**:
$$\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)$$

**Product rule**:
$$\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$$

**Quotient rule**:
$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$$

**Chain rule** (most important for ML!):
$$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

### Chain Rule Examples

**Example 1**: $f(x) = (x^2 + 1)^3$

Let $u = x^2 + 1$, then $f = u^3$

$$\frac{df}{dx} = \frac{df}{du} \cdot \frac{du}{dx} = 3u^2 \cdot 2x = 6x(x^2 + 1)^2$$

**Example 2**: $f(x) = e^{x^2}$

Let $u = x^2$, then $f = e^u$

$$\frac{df}{dx} = e^u \cdot 2x = 2xe^{x^2}$$

**Example 3**: $f(x) = \sin(3x + 1)$

Let $u = 3x + 1$, then $f = \sin u$

$$\frac{df}{dx} = \cos u \cdot 3 = 3\cos(3x + 1)$$

### Chain Rule in Neural Networks

Neural network: $y = f_3(f_2(f_1(x)))$

By chain rule:
$$\frac{dy}{dx} = \frac{dy}{df_3} \cdot \frac{df_3}{df_2} \cdot \frac{df_2}{df_1} \cdot \frac{df_1}{dx}$$

This is **backpropagation**!

---

## Multivariable Calculus

### Partial Derivatives

For function $f(x, y)$, partial derivative with respect to $x$:

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

**Intuition**: Rate of change in $x$ direction, holding $y$ constant

**Example**: $f(x, y) = x^2y + 3xy^2$

$$\frac{\partial f}{\partial x} = 2xy + 3y^2$$
$$\frac{\partial f}{\partial y} = x^2 + 6xy$$

### Gradient Vector

The gradient is a vector of all partial derivatives:

$$\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$$

**Key property**: The gradient points in the direction of steepest ascent

**Negative gradient**: Points in direction of steepest descent (used in gradient descent!)

**Example**: $f(x, y) = x^2 + y^2$

$$\nabla f = \begin{bmatrix} 2x \\ 2y \end{bmatrix}$$

At point $(1, 2)$: $\nabla f = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$

### Directional Derivative

Rate of change in direction $\mathbf{v}$:

$$D_{\mathbf{v}}f = \nabla f \cdot \frac{\mathbf{v}}{\|\mathbf{v}\|}$$

**Maximum rate of change**: In direction of $\nabla f$

**Magnitude**: $\|\nabla f\|$

### Jacobian Matrix

For vector-valued function $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$:

$$J = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n} \end{bmatrix}$$

**Example**:
$$\mathbf{f}(x, y) = \begin{bmatrix} x^2 + y \\ xy \end{bmatrix}$$

$$J = \begin{bmatrix} 2x & 1 \\ y & x \end{bmatrix}$$

**Use in ML**: Jacobians appear in backpropagation through layers

### Hessian Matrix

Matrix of second partial derivatives:

$$H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$$

**Use**: Understanding curvature, second-order optimization

**Example**: $f(x, y) = x^2 + xy + y^2$

$$H = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

---

## Optimization Basics

### Local vs Global Minima

**Local minimum**: $f(x^*) \leq f(x)$ for all $x$ near $x^*$

**Global minimum**: $f(x^*) \leq f(x)$ for all $x$

**Critical point**: Where $\nabla f = 0$

### First-Order Optimality Condition

At a minimum: $\nabla f(x^*) = 0$

**Why**: Gradient is zero at flat points (minima, maxima, saddle points)

### Second-Order Optimality Condition

At a minimum:
1. $\nabla f(x^*) = 0$ (first-order)
2. $H$ is positive semi-definite (second-order)

**Positive definite Hessian**: Local minimum
**Negative definite Hessian**: Local maximum
**Indefinite Hessian**: Saddle point

### Gradient Descent

**Idea**: Move in direction opposite to gradient

$$x_{k+1} = x_k - \alpha \nabla f(x_k)$$

where $\alpha$ is the learning rate

**Why it works**: $-\nabla f$ points toward decreasing function values

**Convergence**: For convex functions with appropriate $\alpha$, converges to global minimum

### Convexity

**Convex function**: Line segment between any two points lies above the graph

**Mathematically**: $f(\lambda x + (1-\lambda)y) \leq \lambda f(x) + (1-\lambda)f(y)$ for $\lambda \in [0,1]$

**Key property**: Local minimum is global minimum

**In ML**: Most loss functions are non-convex, but often have good local minima

---

## Linear Algebra Essentials

### Vectors

**Vector**: Array of numbers

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$$

**Norm (length)**:
$$\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}$$

**Unit vector**: $\|\mathbf{v}\| = 1$

**Normalization**: $\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$

### Dot Product

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i b_i = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta$$

**Geometric interpretation**: Projection of one vector onto another

**Perpendicular vectors**: $\mathbf{a} \cdot \mathbf{b} = 0$

**Use in ML**: Computing similarity, attention scores

### Matrices

**Matrix**: 2D array of numbers

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$

**Dimensions**: $m \times n$ (rows × columns)

### Matrix Multiplication

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$:

$$C = AB, \quad C_{ij} = \sum_{k=1}^n A_{ik}B_{kj}$$

**Key requirement**: Inner dimensions must match

**Result dimensions**: $(m \times n) \times (n \times p) = (m \times p)$

**Not commutative**: $AB \neq BA$ in general

**Use in ML**: Linear transformations in neural networks

### Matrix Transpose

Flip rows and columns:

$$(A^T)_{ij} = A_{ji}$$

**Properties**:
- $(A^T)^T = A$
- $(AB)^T = B^T A^T$

### Identity Matrix

$$I = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}$$

**Property**: $AI = IA = A$

### Matrix Inverse

$A^{-1}$ such that $AA^{-1} = A^{-1}A = I$

**Only square matrices** can have inverses

**Not all square matrices** have inverses (singular matrices)

### Eigenvalues and Eigenvectors

For square matrix $A$:

$$A\mathbf{v} = \lambda\mathbf{v}$$

- $\mathbf{v}$: eigenvector
- $\lambda$: eigenvalue

**Interpretation**: $A$ stretches $\mathbf{v}$ by factor $\lambda$ without changing direction

**Use in ML**: Understanding covariance matrices, PCA

---

## Probability Theory

### Basic Probability

**Sample space** $\Omega$: Set of all possible outcomes

**Event** $A$: Subset of $\Omega$

**Probability** $P(A)$: Number in $[0, 1]$

**Axioms**:
1. $P(A) \geq 0$
2. $P(\Omega) = 1$
3. $P(A \cup B) = P(A) + P(B)$ if $A$ and $B$ are disjoint

### Conditional Probability

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

**Interpretation**: Probability of $A$ given that $B$ occurred

**Example**:
- $P(\text{spam} | \text{contains "free"})$
- $P(\text{disease} | \text{positive test})$

### Independence

Events $A$ and $B$ are independent if:

$$P(A \cap B) = P(A)P(B)$$

Equivalently: $P(A|B) = P(A)$

**Interpretation**: Knowing $B$ doesn't change probability of $A$

### Bayes' Theorem

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

**Alternative form**:
$$P(A|B) = \frac{P(B|A)P(A)}{P(B|A)P(A) + P(B|\neg A)P(\neg A)}$$

**Use in ML**:
- Bayesian inference
- Naive Bayes classifier
- Updating beliefs with evidence

**Example**: Medical diagnosis
- $P(\text{disease}|\text{positive})$ = ?
- Given: $P(\text{positive}|\text{disease})$, $P(\text{disease})$, $P(\text{positive})$

### Random Variables

**Random variable**: Function from outcomes to real numbers

**Discrete**: Takes countable values (e.g., dice roll)

**Continuous**: Takes uncountable values (e.g., height)

### Probability Distributions

**Discrete**: Probability mass function (PMF)
$$P(X = x)$$

**Continuous**: Probability density function (PDF)
$$f(x), \quad P(a \leq X \leq b) = \int_a^b f(x)dx$$

**Cumulative distribution function (CDF)**:
$$F(x) = P(X \leq x)$$

### Common Discrete Distributions

**Bernoulli**: Single binary outcome
$$P(X = 1) = p, \quad P(X = 0) = 1-p$$

**Binomial**: Number of successes in $n$ trials
$$P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$$

**Categorical**: One of $K$ classes
$$P(X = i) = p_i, \quad \sum_{i=1}^K p_i = 1$$

### Common Continuous Distributions

**Uniform**: Equal probability in interval $[a, b]$
$$f(x) = \frac{1}{b-a}$$

**Gaussian (Normal)**:
$$\mathcal{N}(x|\mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

**Standard normal**: $\mu = 0, \sigma = 1$

**Exponential**:
$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

### Expectation (Mean)

**Discrete**:
$$E[X] = \sum_i x_i P(X = x_i)$$

**Continuous**:
$$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$

**Properties**:
- $E[aX + b] = aE[X] + b$
- $E[X + Y] = E[X] + E[Y]$
- If $X, Y$ independent: $E[XY] = E[X]E[Y]$

**Interpretation**: Average value, center of mass

### Variance

$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$

**Standard deviation**: $\sigma = \sqrt{\text{Var}(X)}$

**Properties**:
- $\text{Var}(aX + b) = a^2\text{Var}(X)$
- If $X, Y$ independent: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$

**Interpretation**: Spread, dispersion

### Covariance

$$\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])]$$

**Alternative**: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$

**Interpretation**:
- Positive: $X$ and $Y$ tend to increase together
- Negative: When $X$ increases, $Y$ tends to decrease
- Zero: No linear relationship (but may be non-linear dependence!)

**If independent**: $\text{Cov}(X, Y) = 0$ (converse not always true)

### Correlation

$$\rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

**Range**: $[-1, 1]$

**Interpretation**:
- $\rho = 1$: Perfect positive linear relationship
- $\rho = -1$: Perfect negative linear relationship
- $\rho = 0$: No linear relationship

---

## Statistics Fundamentals

### Population vs Sample

**Population**: Entire group of interest

**Sample**: Subset of population

**Goal**: Use sample to make inferences about population

### Estimators

**Point estimate**: Single value estimate of parameter

**Sample mean**: $\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$ estimates $\mu$

**Sample variance**: $s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2$ estimates $\sigma^2$

**Why $n-1$?** Bessel's correction for unbiased estimate

### Maximum Likelihood Estimation (MLE)

**Idea**: Choose parameters that maximize probability of observed data

**Likelihood**: $L(\theta) = P(data | \theta) = \prod_{i=1}^n P(x_i | \theta)$

**Log-likelihood**: $\ell(\theta) = \log L(\theta) = \sum_{i=1}^n \log P(x_i | \theta)$

**MLE**: $\theta^* = \arg\max_\theta \ell(\theta)$

**Why log?**: Turns products into sums, easier to optimize

**Example**: Estimating mean of Gaussian

Given data from $\mathcal{N}(\mu, \sigma^2)$, MLE gives:
$$\hat{\mu} = \frac{1}{n}\sum_{i=1}^n x_i = \bar{x}$$

### Bias and Variance

**Bias**: $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$

**Variance**: $\text{Var}(\hat{\theta}) = E[(\hat{\theta} - E[\hat{\theta}])^2]$

**Mean Squared Error**:
$$\text{MSE} = \text{Bias}^2 + \text{Variance}$$

**Unbiased estimator**: $E[\hat{\theta}] = \theta$

**In ML**: Bias-variance tradeoff is fundamental

### Central Limit Theorem

**Statement**: For large $n$, sample mean approaches normal distribution:

$$\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$

**Importance**:
- Justifies use of normal distribution
- Foundation for confidence intervals
- Explains why many phenomena are normally distributed

### Law of Large Numbers

As sample size increases, sample mean converges to population mean:

$$\bar{X}_n \to \mu \text{ as } n \to \infty$$

**Why it matters**: More data → better estimates

---

## Information Theory Basics

### Entropy

**Discrete**:
$$H(X) = -\sum_i P(x_i) \log P(x_i)$$

**Interpretation**: Average amount of information/surprise

**Properties**:
- $H(X) \geq 0$
- Maximum when uniform distribution
- Minimum (0) when deterministic

**Example**: Fair coin
$$H = -\frac{1}{2}\log\frac{1}{2} - \frac{1}{2}\log\frac{1}{2} = 1 \text{ bit}$$

### Cross-Entropy

$$H(p, q) = -\sum_i p(x_i) \log q(x_i)$$

**Interpretation**: Average number of bits needed to encode data from $p$ using code from $q$

**In ML**: Cross-entropy loss measures how well predicted distribution $q$ matches true distribution $p$

### KL Divergence

$$D_{KL}(p \| q) = \sum_i p(x_i) \log\frac{p(x_i)}{q(x_i)}$$

**Alternative**: $D_{KL}(p \| q) = H(p, q) - H(p)$

**Properties**:
- $D_{KL}(p \| q) \geq 0$
- $D_{KL}(p \| q) = 0$ iff $p = q$
- **Not symmetric**: $D_{KL}(p \| q) \neq D_{KL}(q \| p)$

**Interpretation**: How much information is lost using $q$ instead of $p$

**In ML**:
- Measuring distance between distributions
- Variational inference
- Regularization

---

## Practice Problems

### Calculus

1. **Compute**: $\frac{d}{dx}(x^3\sin x)$
   <details><summary>Answer</summary>
   Product rule: $3x^2\sin x + x^3\cos x$
   </details>

2. **Chain rule**: $\frac{d}{dx}\log(1 + e^x)$
   <details><summary>Answer</summary>
   $\frac{1}{1 + e^x} \cdot e^x = \frac{e^x}{1 + e^x} = \sigma(x)$ (sigmoid!)
   </details>

3. **Gradient**: $f(x, y) = x^2y + xy^2$, find $\nabla f$ at $(1, 2)$
   <details><summary>Answer</summary>
   $\nabla f = [2xy + y^2, x^2 + 2xy] = [8, 5]$ at $(1, 2)$
   </details>

### Linear Algebra

4. **Matrix multiply**: $\begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}\begin{bmatrix}5\\6\end{bmatrix}$
   <details><summary>Answer</summary>
   $\begin{bmatrix}17\\39\end{bmatrix}$
   </details>

5. **Dimensions**: If $A$ is $3 \times 4$ and $B$ is $4 \times 2$, what is dimension of $AB$?
   <details><summary>Answer</summary>
   $3 \times 2$
   </details>

### Probability

6. **Bayes**: $P(\text{spam}) = 0.3$, $P(\text{"free"}|\text{spam}) = 0.8$, $P(\text{"free"}|\neg\text{spam}) = 0.1$. Find $P(\text{spam}|\text{"free"})$.
   <details><summary>Answer</summary>
   $P(\text{"free"}) = 0.8(0.3) + 0.1(0.7) = 0.31$
   $P(\text{spam}|\text{"free"}) = \frac{0.8 \times 0.3}{0.31} \approx 0.77$
   </details>

7. **Expectation**: $X \sim \text{Bernoulli}(p)$. Find $E[X]$ and $\text{Var}(X)$.
   <details><summary>Answer</summary>
   $E[X] = p$, $\text{Var}(X) = p(1-p)$
   </details>

---

## Connection to Deep Learning

### Calculus → Backpropagation

- **Derivatives** → Gradients of loss with respect to weights
- **Chain rule** → Backpropagation algorithm
- **Gradient descent** → Optimization algorithm

### Linear Algebra → Neural Networks

- **Matrix multiplication** → Linear layers
- **Vectors** → Activations, gradients
- **Matrix dimensions** → Tensor shapes in code

### Probability → Machine Learning

- **Distributions** → Modeling data
- **MLE** → Loss functions (cross-entropy)
- **Bayes' theorem** → Bayesian ML
- **Expectation** → Risk minimization

### Statistics → Model Evaluation

- **Bias-variance** → Underfitting/overfitting
- **Estimators** → Learning algorithms
- **Sampling** → Training/validation splits

---

## Tips for Learning

### If Calculus is Weak

1. Focus on chain rule (most important!)
2. Practice computing gradients
3. Work through backprop by hand
4. Connect derivatives to code

### If Linear Algebra is Weak

1. Master matrix multiplication
2. Understand dimensions/shapes
3. Practice with small examples
4. Verify calculations with NumPy

### If Probability is Weak

1. Start with discrete distributions
2. Build intuition with examples
3. Practice Bayes' theorem
4. Connect to ML loss functions

### Study Strategy

1. **Don't memorize** formulas, understand concepts
2. **Work through examples** by hand
3. **Connect to code** (NumPy implementations)
4. **Visualize** when possible
5. **Practice regularly** (spaced repetition)

---

**After reviewing this guide, you should be ready to tackle the ML topics!**

Return to [GETTING_STARTED.md](./GETTING_STARTED.md) to begin the curriculum.

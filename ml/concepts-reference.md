# ML Concepts Quick Reference

A quick lookup guide for formulas, concepts, and equations you'll need during interviews.

**Keep this open while studying!**

---

## Table of Contents

1. [Calculus Essentials](#calculus-essentials)
2. [Probability & Statistics](#probability--statistics)
3. [Linear Algebra](#linear-algebra)
4. [Activation Functions](#activation-functions)
5. [Loss Functions](#loss-functions)
6. [Optimization Algorithms](#optimization-algorithms)
7. [Neural Network Equations](#neural-network-equations)
8. [Regularization](#regularization)
9. [Normalization](#normalization)
10. [CNN Operations](#cnn-operations)
11. [RNN Equations](#rnn-equations)
12. [Attention & Transformers](#attention--transformers)
13. [Evaluation Metrics](#evaluation-metrics)
14. [Common Gradients](#common-gradients)

---

## Calculus Essentials

### Derivatives (Common Functions)

| Function | Derivative |
|----------|-----------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln(x)$ | $\frac{1}{x}$ |
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ |

### Chain Rule

$$\frac{df(g(x))}{dx} = \frac{df}{dg} \cdot \frac{dg}{dx}$$

**Example**: $f(x) = e^{x^2}$

$$\frac{df}{dx} = e^{x^2} \cdot 2x$$

### Product Rule

$$\frac{d(uv)}{dx} = u\frac{dv}{dx} + v\frac{du}{dx}$$

### Quotient Rule

$$\frac{d(\frac{u}{v})}{dx} = \frac{v\frac{du}{dx} - u\frac{dv}{dx}}{v^2}$$

### Partial Derivatives

For $f(x, y)$:

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

### Gradient Vector

$$\nabla f = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$$

### Jacobian Matrix

For $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$:

$$J = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n} \end{bmatrix}$$

---

## Probability & Statistics

### Probability Basics

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

### Bayes' Theorem

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

### Expectation

**Discrete**: $E[X] = \sum_i x_i P(x_i)$

**Continuous**: $E[X] = \int x f(x) dx$

### Variance

$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$

### Standard Deviation

$$\sigma = \sqrt{\text{Var}(X)}$$

### Covariance

$$\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])]$$

### Gaussian Distribution

$$\mathcal{N}(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

### Maximum Likelihood Estimation

$$\theta^* = \arg\max_\theta \prod_{i=1}^n P(x_i | \theta)$$

**Log-likelihood**:

$$\theta^* = \arg\max_\theta \sum_{i=1}^n \log P(x_i | \theta)$$

---

## Linear Algebra

### Matrix Multiplication

For $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$:

$$C = AB, \quad C_{ij} = \sum_{k=1}^n A_{ik}B_{kj}$$

### Dot Product

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i b_i = \|\mathbf{a}\| \|\mathbf{b}\| \cos\theta$$

### Matrix Transpose

$$(AB)^T = B^T A^T$$

### Trace

$$\text{tr}(A) = \sum_{i=1}^n A_{ii}$$

**Properties**:
- $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$
- $\text{tr}(AB) = \text{tr}(BA)$
- $\text{tr}(A) = \sum_i \lambda_i$ (sum of eigenvalues)

### Determinant

$$\det(AB) = \det(A)\det(B)$$

**Properties**:
- $\det(A^T) = \det(A)$
- $\det(A) = \prod_i \lambda_i$ (product of eigenvalues)
- $\det(A) = 0$ iff $A$ is singular (not invertible)

### Frobenius Norm

$$\|A\|_F = \sqrt{\sum_{i,j} A_{ij}^2} = \sqrt{\text{tr}(A^T A)}$$

### Eigenvalues & Eigenvectors

$$A\mathbf{v} = \lambda\mathbf{v}$$

**Characteristic equation**: $\det(A - \lambda I) = 0$

**Properties**:
- $\det(A) = \prod_i \lambda_i$
- $\text{tr}(A) = \sum_i \lambda_i$
- Symmetric matrix → real eigenvalues, orthogonal eigenvectors

### Eigendecomposition

$$A = V\Lambda V^{-1}$$

- $V$: eigenvector matrix (columns are eigenvectors)
- $\Lambda$: diagonal matrix of eigenvalues

**For symmetric matrices**: $A = Q\Lambda Q^T$ where $Q$ is orthogonal

### Singular Value Decomposition (SVD)

$$A = U\Sigma V^T$$

- $U \in \mathbb{R}^{m \times m}$: left singular vectors
- $\Sigma \in \mathbb{R}^{m \times n}$: singular values (diagonal)
- $V \in \mathbb{R}^{n \times n}$: right singular vectors

**Relationship**:
- Singular values = $\sqrt{\text{eigenvalues of } A^T A}$
- $V$ = eigenvectors of $A^T A$
- $U$ = eigenvectors of $AA^T$

### Positive Definite Matrix

**Definition**: $\mathbf{x}^T A \mathbf{x} > 0$ for all $\mathbf{x} \neq 0$

**Equivalent conditions**:
- All eigenvalues $> 0$
- All leading principal minors $> 0$
- Cholesky decomposition exists: $A = LL^T$

### Condition Number

$$\kappa(A) = \frac{\sigma_{max}}{\sigma_{min}} = \frac{|\lambda_{max}|}{|\lambda_{min}|}$$

**Interpretation**:
- $\kappa \approx 1$: Well-conditioned
- $\kappa \gg 1$: Ill-conditioned (numerical instability, slow convergence)

### Matrix Rank

$$\text{rank}(A) = \text{number of linearly independent columns (or rows)}$$

**Properties**:
- $\text{rank}(A) \leq \min(m, n)$ for $m \times n$ matrix
- $\text{rank}(A) = \text{rank}(A^T)$
- $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$

### Orthogonal Matrix

$$Q^T Q = QQ^T = I$$

**Properties**:
- Preserves lengths: $\|Q\mathbf{x}\| = \|\mathbf{x}\|$
- Preserves angles
- $\det(Q) = \pm 1$
- Eigenvalues have magnitude 1

---

## Activation Functions

### Sigmoid (Logistic)

$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

**Derivative**: $\sigma'(x) = \sigma(x)(1 - \sigma(x))$

**Range**: $(0, 1)$

**Use**: Binary classification output

### Tanh (Hyperbolic Tangent)

$$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

**Derivative**: $\tanh'(x) = 1 - \tanh^2(x)$

**Range**: $(-1, 1)$

**Use**: Hidden layers (zero-centered)

### ReLU (Rectified Linear Unit)

$$\text{ReLU}(x) = \max(0, x)$$

**Derivative**:
$$\text{ReLU}'(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x \leq 0 \end{cases}$$

**Range**: $[0, \infty)$

**Use**: Default choice for hidden layers

### Leaky ReLU

$$\text{LeakyReLU}(x) = \max(\alpha x, x)$$

where $\alpha$ is small (e.g., 0.01)

**Derivative**:
$$\text{LeakyReLU}'(x) = \begin{cases} 1 & \text{if } x > 0 \\ \alpha & \text{if } x \leq 0 \end{cases}$$

### Softmax

$$\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^n e^{x_j}}$$

**Properties**:
- $\sum_i \text{softmax}(x_i) = 1$
- Converts logits to probability distribution

**Use**: Multi-class classification output

---

## Loss Functions

### Mean Squared Error (MSE)

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$

**Gradient**: $\frac{\partial \text{MSE}}{\partial \hat{y}_i} = \frac{2}{n}(\hat{y}_i - y_i)$

**Use**: Regression tasks

### Binary Cross-Entropy

$$\text{BCE} = -\frac{1}{n}\sum_{i=1}^n [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]$$

**Gradient**: $\frac{\partial \text{BCE}}{\partial \hat{y}_i} = -\frac{y_i}{\hat{y}_i} + \frac{1-y_i}{1-\hat{y}_i}$

**Use**: Binary classification

### Categorical Cross-Entropy

$$\text{CCE} = -\sum_{i=1}^n y_i \log(\hat{y}_i)$$

where $y$ is one-hot encoded

**Combined with softmax**: $\frac{\partial \text{CCE}}{\partial z_i} = \hat{y}_i - y_i$

**Use**: Multi-class classification

### Hinge Loss (SVM)

$$L = \max(0, 1 - y \cdot \hat{y})$$

**Use**: Support vector machines

---

## Optimization Algorithms

### Gradient Descent

$$\theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t)$$

- $\eta$: learning rate
- $\nabla_\theta L$: gradient of loss

### Stochastic Gradient Descent (SGD)

$$\theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t; x^{(i)}, y^{(i)})$$

Uses single example (or mini-batch) per update

### SGD with Momentum

$$v_{t+1} = \beta v_t + \nabla_\theta L(\theta_t)$$
$$\theta_{t+1} = \theta_t - \eta v_{t+1}$$

- $\beta$: momentum coefficient (typically 0.9)

### RMSprop

$$s_{t+1} = \beta s_t + (1-\beta)(\nabla_\theta L)^2$$
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{s_{t+1} + \epsilon}} \nabla_\theta L$$

- $\beta$: decay rate (typically 0.9)
- $\epsilon$: small constant for numerical stability ($10^{-8}$)

### Adam (Adaptive Moment Estimation)

$$m_{t+1} = \beta_1 m_t + (1-\beta_1)\nabla_\theta L$$ (first moment)
$$v_{t+1} = \beta_2 v_t + (1-\beta_2)(\nabla_\theta L)^2$$ (second moment)

**Bias correction**:
$$\hat{m}_{t+1} = \frac{m_{t+1}}{1-\beta_1^{t+1}}$$
$$\hat{v}_{t+1} = \frac{v_{t+1}}{1-\beta_2^{t+1}}$$

**Update**:
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_{t+1}} + \epsilon} \hat{m}_{t+1}$$

**Default hyperparameters**:
- $\beta_1 = 0.9$
- $\beta_2 = 0.999$
- $\epsilon = 10^{-8}$
- $\eta = 0.001$

---

## Neural Network Equations

### Forward Pass (Single Layer)

$$z = Wx + b$$
$$a = \sigma(z)$$

- $W$: weight matrix
- $b$: bias vector
- $\sigma$: activation function
- $z$: pre-activation
- $a$: activation

### Backpropagation (Single Layer)

Given $\frac{\partial L}{\partial a}$:

$$\frac{\partial L}{\partial z} = \frac{\partial L}{\partial a} \odot \sigma'(z)$$
$$\frac{\partial L}{\partial W} = \frac{\partial L}{\partial z} \cdot x^T$$
$$\frac{\partial L}{\partial b} = \frac{\partial L}{\partial z}$$
$$\frac{\partial L}{\partial x} = W^T \cdot \frac{\partial L}{\partial z}$$

where $\odot$ is element-wise multiplication

### Multi-Layer Network

**Forward**:
$$a^{[0]} = x$$
$$z^{[l]} = W^{[l]}a^{[l-1]} + b^{[l]}$$
$$a^{[l]} = \sigma(z^{[l]})$$

**Backward**:
$$\delta^{[L]} = \frac{\partial L}{\partial a^{[L]}} \odot \sigma'(z^{[L]})$$
$$\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot \sigma'(z^{[l]})$$

---

## Regularization

### L2 Regularization (Weight Decay)

$$L_{total} = L_{data} + \frac{\lambda}{2}\sum_i w_i^2$$

**Gradient**: $\frac{\partial L_{total}}{\partial w_i} = \frac{\partial L_{data}}{\partial w_i} + \lambda w_i$

**Update**: $w_{t+1} = (1-\eta\lambda)w_t - \eta\frac{\partial L_{data}}{\partial w_t}$

### L1 Regularization

$$L_{total} = L_{data} + \lambda\sum_i |w_i|$$

**Gradient**: $\frac{\partial L_{total}}{\partial w_i} = \frac{\partial L_{data}}{\partial w_i} + \lambda \cdot \text{sign}(w_i)$

### Dropout

**Training**: $a^{[l]} = d^{[l]} \odot a^{[l]}$ where $d^{[l]} \sim \text{Bernoulli}(p)$

**Inference**: $a^{[l]} = p \cdot a^{[l]}$ (or scale during training by $\frac{1}{p}$)

---

## Normalization

### Batch Normalization

**Training**:
$$\mu_B = \frac{1}{m}\sum_{i=1}^m x_i$$
$$\sigma_B^2 = \frac{1}{m}\sum_{i=1}^m (x_i - \mu_B)^2$$
$$\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$
$$y_i = \gamma\hat{x}_i + \beta$$

**Inference**: Use running averages $\mu_{avg}$ and $\sigma_{avg}^2$

### Layer Normalization

Same as batch norm, but compute statistics over features (not batch):

$$\mu = \frac{1}{d}\sum_{i=1}^d x_i$$
$$\sigma^2 = \frac{1}{d}\sum_{i=1}^d (x_i - \mu)^2$$

---

## CNN Operations

### Convolution Output Size

$$O = \left\lfloor \frac{I + 2P - K}{S} \right\rfloor + 1$$

- $I$: input size
- $P$: padding
- $K$: kernel size
- $S$: stride
- $O$: output size

### Pooling

**Max pooling**: $y = \max(x_{window})$

**Average pooling**: $y = \frac{1}{|window|}\sum x_{window}$

### Number of Parameters (Conv Layer)

$$\text{params} = (K_h \times K_w \times C_{in} + 1) \times C_{out}$$

- $K_h, K_w$: kernel height/width
- $C_{in}$: input channels
- $C_{out}$: output channels
- $+1$: bias term

---

## RNN Equations

### Vanilla RNN

$$h_t = \tanh(W_{hh}h_{t-1} + W_{xh}x_t + b_h)$$
$$y_t = W_{hy}h_t + b_y$$

### LSTM (Long Short-Term Memory)

**Forget gate**: $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$

**Input gate**: $i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$

**Candidate**: $\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$

**Cell state**: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$

**Output gate**: $o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$

**Hidden state**: $h_t = o_t \odot \tanh(C_t)$

### GRU (Gated Recurrent Unit)

**Update gate**: $z_t = \sigma(W_z \cdot [h_{t-1}, x_t])$

**Reset gate**: $r_t = \sigma(W_r \cdot [h_{t-1}, x_t])$

**Candidate**: $\tilde{h}_t = \tanh(W \cdot [r_t \odot h_{t-1}, x_t])$

**Hidden state**: $h_t = (1-z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$

---

## Attention & Transformers

### Scaled Dot-Product Attention

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

- $Q$: queries
- $K$: keys
- $V$: values
- $d_k$: dimension of keys

### Multi-Head Attention

$$\text{MultiHead}(Q, K, V) = \text{Concat}(head_1, ..., head_h)W^O$$

where $head_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$

### Positional Encoding

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right)$$
$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d}}\right)$$

---

## Evaluation Metrics

### Classification

**Accuracy**: $\frac{TP + TN}{TP + TN + FP + FN}$

**Precision**: $\frac{TP}{TP + FP}$

**Recall**: $\frac{TP}{TP + FN}$

**F1 Score**: $2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$

### Regression

**MAE**: $\frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$

**RMSE**: $\sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}$

**R²**: $1 - \frac{SS_{res}}{SS_{tot}}$ where $SS_{res} = \sum(y_i - \hat{y}_i)^2$, $SS_{tot} = \sum(y_i - \bar{y})^2$

---

## Common Gradients

### Softmax + Cross-Entropy

Combined gradient:
$$\frac{\partial L}{\partial z_i} = \hat{y}_i - y_i$$

where $\hat{y} = \text{softmax}(z)$ and $y$ is one-hot

### Sigmoid Gradient

$$\frac{d\sigma}{dx} = \sigma(x)(1-\sigma(x))$$

### Tanh Gradient

$$\frac{d\tanh}{dx} = 1 - \tanh^2(x) = \text{sech}^2(x)$$

### ReLU Gradient

$$\frac{d\text{ReLU}}{dx} = \begin{cases} 1 & x > 0 \\ 0 & x \leq 0 \end{cases}$$

### Matrix-Vector Product Gradient

For $y = Wx$:
- $\frac{\partial L}{\partial W} = \frac{\partial L}{\partial y} x^T$
- $\frac{\partial L}{\partial x} = W^T \frac{\partial L}{\partial y}$

---

## Weight Initialization

### Xavier/Glorot (tanh, sigmoid)

$$W \sim \mathcal{N}\left(0, \frac{2}{n_{in} + n_{out}}\right)$$

or

$$W \sim U\left[-\sqrt{\frac{6}{n_{in} + n_{out}}}, \sqrt{\frac{6}{n_{in} + n_{out}}}\right]$$

### He Initialization (ReLU)

$$W \sim \mathcal{N}\left(0, \frac{2}{n_{in}}\right)$$

---

## Learning Rate Schedules

### Step Decay

$$\eta_t = \eta_0 \cdot \gamma^{\lfloor t/k \rfloor}$$

### Exponential Decay

$$\eta_t = \eta_0 e^{-\lambda t}$$

### Cosine Annealing

$$\eta_t = \eta_{min} + \frac{1}{2}(\eta_{max} - \eta_{min})\left(1 + \cos\left(\frac{t}{T}\pi\right)\right)$$

---

## Quick Tips

### Dimensions to Remember

**Fully connected layer**:
- Input: $(batch, n_{in})$
- Weights: $(n_{in}, n_{out})$
- Output: $(batch, n_{out})$

**Convolutional layer**:
- Input: $(batch, channels_{in}, height, width)$
- Filters: $(channels_{out}, channels_{in}, kernel_h, kernel_w)$
- Output: $(batch, channels_{out}, height_{out}, width_{out})$

### Gradient Checking

Numerical gradient:
$$\frac{\partial f}{\partial x} \approx \frac{f(x + \epsilon) - f(x - \epsilon)}{2\epsilon}$$

Use $\epsilon = 10^{-7}$ typically

---

**Bookmark this page for quick reference during study and interviews!**

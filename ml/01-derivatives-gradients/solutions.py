"""
Topic 01: Derivatives & Gradients - Solutions

Complete solutions with explanations.
"""

import numpy as np


# ============================================================================
# Solution 1: Numerical Derivative
# ============================================================================

def numerical_derivative(f, x, h=1e-7):
    """
    Compute the numerical derivative of f at x using the symmetric difference formula.

    The symmetric difference formula is more accurate than the forward difference:
    - Forward difference: (f(x+h) - f(x)) / h  [O(h) error]
    - Symmetric difference: (f(x+h) - f(x-h)) / (2h)  [O(h²) error]

    Time Complexity: O(1) - two function evaluations
    Space Complexity: O(1)
    """
    return (f(x + h) - f(x - h)) / (2 * h)


# ============================================================================
# Solution 2: Numerical Gradient
# ============================================================================

def numerical_gradient(f, x, h=1e-7):
    """
    Compute the numerical gradient of f at x.

    Approach:
    1. Initialize gradient vector with zeros
    2. For each dimension i:
       - Perturb x in dimension i by +h
       - Perturb x in dimension i by -h
       - Compute symmetric difference
    3. Return gradient vector

    Time Complexity: O(n) where n = dimension of x
    Space Complexity: O(n)
    """
    grad = np.zeros_like(x, dtype=float)

    for i in range(len(x)):
        # Create perturbation vector (only i-th element is non-zero)
        x_plus = x.copy()
        x_plus[i] += h

        x_minus = x.copy()
        x_minus[i] -= h

        # Compute partial derivative using symmetric difference
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * h)

    return grad


# Alternative vectorized implementation (more advanced)
def numerical_gradient_vectorized(f, x, h=1e-7):
    """
    Vectorized version using identity matrix trick.

    This is more elegant but essentially does the same computation.
    """
    n = len(x)
    grad = np.zeros(n)
    identity = np.eye(n)

    for i in range(n):
        grad[i] = (f(x + h * identity[i]) - f(x - h * identity[i])) / (2 * h)

    return grad


# ============================================================================
# Solution 3: Gradient Descent Step
# ============================================================================

def gradient_descent_step(f, x, learning_rate=0.01, h=1e-7):
    """
    Perform one step of gradient descent.

    Gradient descent update rule:
    x_new = x - η * ∇f(x)

    where:
    - η (eta) is the learning rate (step size)
    - ∇f(x) is the gradient at current point

    Why negative gradient?
    - Gradient points uphill (direction of steepest ascent)
    - We want to minimize, so go downhill (negative gradient)

    Time Complexity: O(n) for computing gradient
    Space Complexity: O(n)
    """
    # Compute gradient at current point
    grad = numerical_gradient(f, x, h)

    # Update using gradient descent rule
    x_new = x - learning_rate * grad

    return x_new


# ============================================================================
# Solution 4: Directional Derivative
# ============================================================================

def directional_derivative(f, x, direction, h=1e-7):
    """
    Compute the directional derivative of f at x in the given direction.

    Formula: D_u f = ∇f · u
    where u is the unit vector in the given direction

    Steps:
    1. Normalize direction to unit vector
    2. Compute gradient
    3. Take dot product

    Alternative formula: D_u f = ||∇f|| cos(θ)
    where θ is angle between ∇f and direction

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Normalize direction to unit vector
    u = direction / np.linalg.norm(direction)

    # Compute gradient
    grad = numerical_gradient(f, x, h)

    # Directional derivative is dot product
    return np.dot(grad, u)


# ============================================================================
# Solution 5: Find Steepest Ascent Direction
# ============================================================================

def steepest_ascent_direction(f, x, h=1e-7):
    """
    Find the direction of steepest ascent at point x.

    The gradient ∇f points in the direction of steepest ascent.
    We normalize it to get a unit vector.

    For steepest DESCENT (minimization), return negative: -∇f / ||∇f||

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Compute gradient
    grad = numerical_gradient(f, x, h)

    # Normalize to unit vector
    return grad / np.linalg.norm(grad)


# ============================================================================
# Additional Helper Functions
# ============================================================================

def check_gradient(f, grad_f, x, h=1e-7, tolerance=1e-5):
    """
    Check if analytical gradient matches numerical gradient.

    This is called "gradient checking" and is crucial for verifying
    backpropagation implementations.

    Args:
        f: Function
        grad_f: Function that computes analytical gradient
        x: Point to check
        h: Step size for numerical gradient
        tolerance: Maximum allowed difference

    Returns:
        bool: True if gradients match within tolerance
    """
    numerical_grad = numerical_gradient(f, x, h)
    analytical_grad = grad_f(x)

    diff = np.linalg.norm(numerical_grad - analytical_grad)
    relative_error = diff / (np.linalg.norm(numerical_grad) + np.linalg.norm(analytical_grad))

    print(f"Numerical gradient: {numerical_grad}")
    print(f"Analytical gradient: {analytical_grad}")
    print(f"Relative error: {relative_error}")

    return relative_error < tolerance


def gradient_descent(f, x0, learning_rate=0.01, max_iters=1000, tolerance=1e-6):
    """
    Run gradient descent until convergence.

    Args:
        f: Function to minimize
        x0: Initial point
        learning_rate: Step size
        max_iters: Maximum iterations
        tolerance: Stop when ||gradient|| < tolerance

    Returns:
        x: Minimum found
        history: List of (x, f(x)) at each iteration
    """
    x = x0.copy()
    history = [(x.copy(), f(x))]

    for i in range(max_iters):
        grad = numerical_gradient(f, x)

        # Check for convergence
        if np.linalg.norm(grad) < tolerance:
            print(f"Converged after {i} iterations")
            break

        # Update
        x = x - learning_rate * grad
        history.append((x.copy(), f(x)))

    return x, history


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    print("Solution Examples for Topic 01: Derivatives & Gradients")
    print("=" * 60)

    # Example 1: Numerical derivative
    print("\n1. Numerical Derivative")
    print("-" * 40)
    f = lambda x: x**2
    x = 3.0
    derivative = numerical_derivative(f, x)
    print(f"f(x) = x²")
    print(f"f'({x}) = {derivative:.6f} (expected: 6.0)")

    # Example 2: Numerical gradient
    print("\n2. Numerical Gradient")
    print("-" * 40)
    f = lambda x: x[0]**2 + x[1]**2
    x = np.array([1.0, 2.0])
    grad = numerical_gradient(f, x)
    print(f"f(x, y) = x² + y²")
    print(f"∇f({x}) = {grad} (expected: [2.0, 4.0])")

    # Example 3: Gradient descent
    print("\n3. Gradient Descent on f(x,y) = x² + y²")
    print("-" * 40)
    f = lambda x: x[0]**2 + x[1]**2
    x0 = np.array([10.0, 10.0])
    print(f"Starting point: {x0}, f(x0) = {f(x0):.6f}")

    for i in range(10):
        x0 = gradient_descent_step(f, x0, learning_rate=0.1)
        print(f"Step {i+1}: x = {x0}, f(x) = {f(x0):.6f}")

    # Example 4: Directional derivative
    print("\n4. Directional Derivative")
    print("-" * 40)
    f = lambda x: x[0]**2 + x[1]**2
    x = np.array([1.0, 2.0])
    direction = np.array([1.0, 0.0])
    dir_deriv = directional_derivative(f, x, direction)
    print(f"f(x, y) = x² + y²")
    print(f"At point ({x[0]}, {x[1]}), direction [1, 0]")
    print(f"Directional derivative: {dir_deriv:.6f} (expected: 2.0)")

    # Example 5: Steepest ascent
    print("\n5. Steepest Ascent Direction")
    print("-" * 40)
    f = lambda x: x[0]**2 + x[1]**2
    x = np.array([3.0, 4.0])
    direction = steepest_ascent_direction(f, x)
    print(f"f(x, y) = x² + y²")
    print(f"At point ({x[0]}, {x[1]})")
    print(f"Steepest ascent direction: {direction}")
    print(f"Expected: [0.6, 0.8] (normalized [6, 8])")
    print(f"||direction|| = {np.linalg.norm(direction):.6f} (should be 1.0)")

    # Example 6: Gradient checking
    print("\n6. Gradient Checking")
    print("-" * 40)
    f = lambda x: x[0]**2 + 2*x[1]**2 + 3*x[2]**2
    grad_f = lambda x: np.array([2*x[0], 4*x[1], 6*x[2]])
    x = np.array([1.0, 2.0, 3.0])
    matches = check_gradient(f, grad_f, x)
    print(f"Gradients match: {matches}")

    # Example 7: Full gradient descent
    print("\n7. Full Gradient Descent")
    print("-" * 40)
    f = lambda x: (x[0] - 2)**2 + (x[1] - 3)**2  # Minimum at [2, 3]
    x0 = np.array([0.0, 0.0])
    x_min, history = gradient_descent(f, x0, learning_rate=0.1, max_iters=100)
    print(f"Starting point: {x0}")
    print(f"Minimum found: {x_min}")
    print(f"Expected: [2.0, 3.0]")
    print(f"f(x_min) = {f(x_min):.10f} (expected: 0.0)")
    print(f"Number of iterations: {len(history)}")

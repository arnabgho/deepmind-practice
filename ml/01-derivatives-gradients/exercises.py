"""
Topic 01: Derivatives & Gradients - Exercises

Complete the functions below and run this file to check your implementations.
"""

import numpy as np
import unittest


# ============================================================================
# Exercise 1: Numerical Derivative
# ============================================================================

def numerical_derivative(f, x, h=1e-7):
    """
    Compute the numerical derivative of f at x using the symmetric difference formula.

    Formula: f'(x) ≈ (f(x + h) - f(x - h)) / (2h)

    Args:
        f: Function to differentiate
        x: Point at which to compute derivative (scalar)
        h: Small step size (default: 1e-7)

    Returns:
        Approximate derivative (scalar)

    Example:
        >>> f = lambda x: x**2
        >>> numerical_derivative(f, 3.0)  # Should be ≈ 6.0
    """
    # TODO: Implement the symmetric difference formula
    pass


# ============================================================================
# Exercise 2: Numerical Gradient
# ============================================================================

def numerical_gradient(f, x, h=1e-7):
    """
    Compute the numerical gradient of f at x.

    The gradient is a vector of partial derivatives:
    ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]

    For each dimension i:
    ∂f/∂xᵢ ≈ (f(x + hₑᵢ) - f(x - hₑᵢ)) / (2h)
    where eᵢ is the unit vector in dimension i

    Args:
        f: Function to differentiate (takes numpy array, returns scalar)
        x: Point at which to compute gradient (numpy array)
        h: Small step size (default: 1e-7)

    Returns:
        Gradient vector (numpy array with same shape as x)

    Example:
        >>> f = lambda x: x[0]**2 + x[1]**2
        >>> numerical_gradient(f, np.array([1.0, 2.0]))  # Should be ≈ [2.0, 4.0]
    """
    # TODO: Implement numerical gradient computation
    # Hint: Use np.zeros_like(x) to create gradient vector
    # Hint: Create unit vectors by modifying single element
    pass


# ============================================================================
# Exercise 3: Gradient Descent Step
# ============================================================================

def gradient_descent_step(f, x, learning_rate=0.01, h=1e-7):
    """
    Perform one step of gradient descent.

    Update rule: x_new = x - learning_rate * ∇f(x)

    Args:
        f: Function to minimize
        x: Current point (numpy array)
        learning_rate: Step size (default: 0.01)
        h: Step size for numerical gradient (default: 1e-7)

    Returns:
        Updated point after one gradient descent step (numpy array)

    Example:
        >>> f = lambda x: x[0]**2 + x[1]**2
        >>> x = np.array([10.0, 10.0])
        >>> x_new = gradient_descent_step(f, x, learning_rate=0.1)
        >>> # x_new should be closer to [0, 0] than x
    """
    # TODO: Implement gradient descent step
    # Hint: Use numerical_gradient from Exercise 2
    pass


# ============================================================================
# Exercise 4: Directional Derivative
# ============================================================================

def directional_derivative(f, x, direction, h=1e-7):
    """
    Compute the directional derivative of f at x in the given direction.

    Formula: D_u f = ∇f · u
    where u is a unit vector in the given direction

    Args:
        f: Function to differentiate (takes numpy array, returns scalar)
        x: Point at which to compute directional derivative (numpy array)
        direction: Direction vector (numpy array, need not be unit length)
        h: Step size for numerical gradient (default: 1e-7)

    Returns:
        Directional derivative (scalar)

    Example:
        >>> f = lambda x: x[0]**2 + x[1]**2
        >>> x = np.array([1.0, 2.0])
        >>> direction = np.array([1.0, 0.0])  # x direction
        >>> directional_derivative(f, x, direction)  # Should be ≈ 2.0
    """
    # TODO: Implement directional derivative
    # Hint: First normalize the direction vector to unit length
    # Hint: Compute gradient and take dot product with unit direction
    pass


# ============================================================================
# Exercise 5: Find Steepest Ascent Direction
# ============================================================================

def steepest_ascent_direction(f, x, h=1e-7):
    """
    Find the direction of steepest ascent at point x.

    The direction of steepest ascent is the normalized gradient: ∇f / ||∇f||

    Args:
        f: Function (takes numpy array, returns scalar)
        x: Point at which to find steepest direction (numpy array)
        h: Step size for numerical gradient (default: 1e-7)

    Returns:
        Unit vector in direction of steepest ascent (numpy array)

    Example:
        >>> f = lambda x: x[0]**2 + x[1]**2
        >>> x = np.array([3.0, 4.0])
        >>> direction = steepest_ascent_direction(f, x)
        >>> # direction should be ≈ [0.6, 0.8] (normalized [3, 4])
    """
    # TODO: Implement steepest ascent direction
    # Hint: Compute gradient and normalize it
    pass


# ============================================================================
# Unit Tests
# ============================================================================

class TestDerivativesGradients(unittest.TestCase):

    def test_numerical_derivative(self):
        """Test numerical derivative computation"""
        # Test f(x) = x^2, f'(x) = 2x
        f = lambda x: x**2
        self.assertAlmostEqual(numerical_derivative(f, 3.0), 6.0, places=5)
        self.assertAlmostEqual(numerical_derivative(f, -2.0), -4.0, places=5)

        # Test f(x) = sin(x), f'(x) = cos(x)
        f = lambda x: np.sin(x)
        self.assertAlmostEqual(numerical_derivative(f, 0.0), 1.0, places=5)
        self.assertAlmostEqual(numerical_derivative(f, np.pi), -1.0, places=5)

    def test_numerical_gradient(self):
        """Test numerical gradient computation"""
        # Test f(x, y) = x^2 + y^2, ∇f = [2x, 2y]
        f = lambda x: x[0]**2 + x[1]**2
        grad = numerical_gradient(f, np.array([1.0, 2.0]))
        expected = np.array([2.0, 4.0])
        np.testing.assert_array_almost_equal(grad, expected, decimal=5)

        # Test f(x, y, z) = x^2 + 2y^2 + 3z^2, ∇f = [2x, 4y, 6z]
        f = lambda x: x[0]**2 + 2*x[1]**2 + 3*x[2]**2
        grad = numerical_gradient(f, np.array([1.0, 1.0, 1.0]))
        expected = np.array([2.0, 4.0, 6.0])
        np.testing.assert_array_almost_equal(grad, expected, decimal=5)

    def test_gradient_descent_step(self):
        """Test gradient descent step"""
        # Test f(x, y) = x^2 + y^2 (minimum at [0, 0])
        f = lambda x: x[0]**2 + x[1]**2
        x = np.array([10.0, 10.0])
        x_new = gradient_descent_step(f, x, learning_rate=0.1)

        # Check that we moved closer to minimum
        self.assertLess(np.linalg.norm(x_new), np.linalg.norm(x))

        # Check that loss decreased
        self.assertLess(f(x_new), f(x))

    def test_directional_derivative(self):
        """Test directional derivative computation"""
        # Test f(x, y) = x^2 + y^2, ∇f = [2x, 2y]
        # At (1, 2), gradient is [2, 4]
        f = lambda x: x[0]**2 + x[1]**2
        x = np.array([1.0, 2.0])

        # Direction along x-axis: [1, 0]
        dir_x = directional_derivative(f, x, np.array([1.0, 0.0]))
        self.assertAlmostEqual(dir_x, 2.0, places=5)

        # Direction along y-axis: [0, 1]
        dir_y = directional_derivative(f, x, np.array([0.0, 1.0]))
        self.assertAlmostEqual(dir_y, 4.0, places=5)

        # Direction [1, 1] (45 degrees)
        dir_45 = directional_derivative(f, x, np.array([1.0, 1.0]))
        expected = (2.0 + 4.0) / np.sqrt(2)  # (∇f · [1,1]) / ||[1,1]||
        self.assertAlmostEqual(dir_45, expected, places=5)

    def test_steepest_ascent_direction(self):
        """Test steepest ascent direction"""
        # Test f(x, y) = x^2 + y^2
        # At (3, 4), gradient is [6, 8], normalized: [0.6, 0.8]
        f = lambda x: x[0]**2 + x[1]**2
        x = np.array([3.0, 4.0])
        direction = steepest_ascent_direction(f, x)
        expected = np.array([0.6, 0.8])
        np.testing.assert_array_almost_equal(direction, expected, decimal=5)

        # Check that it's a unit vector
        self.assertAlmostEqual(np.linalg.norm(direction), 1.0, places=5)


if __name__ == '__main__':
    print("Running tests for Topic 01: Derivatives & Gradients")
    print("=" * 60)
    unittest.main(verbosity=2)

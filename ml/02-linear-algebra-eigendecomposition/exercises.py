"""
Topic 02: Linear Algebra & Eigendecomposition - Exercises

Complete the functions below and run this file to check your implementations.
"""

import numpy as np
import unittest


# ============================================================================
# Exercise 1: Compute Eigenvalues for 2x2 Matrix
# ============================================================================

def compute_eigenvalues_2x2(A):
    """
    Compute eigenvalues of a 2x2 matrix using the characteristic equation.

    For 2x2 matrix: det(A - λI) = 0
    This gives: λ² - trace(A)λ + det(A) = 0

    Use quadratic formula: λ = (trace ± sqrt(trace² - 4*det)) / 2

    Args:
        A: 2x2 numpy array

    Returns:
        Tuple of two eigenvalues (λ1, λ2)
        May be complex numbers!

    Example:
        >>> A = np.array([[4, 1], [2, 3]])
        >>> compute_eigenvalues_2x2(A)
        (5.0, 2.0)
    """
    # TODO: Implement eigenvalue computation
    # Hint: Use np.trace(), np.linalg.det()
    # Hint: For square root of potentially negative number, use np.sqrt with complex type
    pass


# ============================================================================
# Exercise 2: Power Iteration
# ============================================================================

def power_iteration(A, num_iterations=100, tolerance=1e-6):
    """
    Find the dominant eigenvalue and eigenvector using power iteration.

    Algorithm:
    1. Start with random vector v
    2. Repeatedly compute: v = A @ v, then normalize v
    3. Eigenvalue = v^T @ A @ v (Rayleigh quotient)

    Args:
        A: Square numpy array
        num_iterations: Maximum number of iterations
        tolerance: Stop when change in eigenvalue < tolerance

    Returns:
        Tuple (eigenvalue, eigenvector)

    Example:
        >>> A = np.array([[4, 1], [2, 3]])
        >>> eigenvalue, eigenvector = power_iteration(A)
        >>> # Should converge to largest eigenvalue (5.0)
    """
    # TODO: Implement power iteration
    # Hint: v = np.random.randn(A.shape[0])
    # Hint: v = v / np.linalg.norm(v) for normalization
    # Hint: eigenvalue = v.T @ A @ v (Rayleigh quotient)
    pass


# ============================================================================
# Exercise 3: Check if Matrix is Symmetric
# ============================================================================

def is_symmetric(A, tolerance=1e-9):
    """
    Check if a matrix is symmetric (A = A^T).

    Args:
        A: Square numpy array
        tolerance: Maximum allowed difference

    Returns:
        Boolean: True if symmetric

    Example:
        >>> A = np.array([[1, 2], [2, 3]])
        >>> is_symmetric(A)
        True
    """
    # TODO: Implement symmetry check
    # Hint: Compare A with A.T
    # Hint: Use np.allclose() for numerical comparison
    pass


# ============================================================================
# Exercise 4: Check if Matrix is Positive Definite
# ============================================================================

def is_positive_definite(A):
    """
    Check if a symmetric matrix is positive definite.

    A matrix is positive definite if all eigenvalues > 0.

    Args:
        A: Square numpy array (should be symmetric)

    Returns:
        Boolean: True if positive definite

    Example:
        >>> A = np.array([[2, 0], [0, 3]])  # Positive definite
        >>> is_positive_definite(A)
        True
        >>> B = np.array([[1, 0], [0, -1]])  # Not positive definite
        >>> is_positive_definite(B)
        False
    """
    # TODO: Implement positive definite check
    # Hint: Compute eigenvalues and check if all > 0
    # Hint: Use np.linalg.eigvalsh() for symmetric matrices
    pass


# ============================================================================
# Exercise 5: Matrix Power Using Eigendecomposition
# ============================================================================

def matrix_power_eigen(A, k):
    """
    Compute A^k efficiently using eigendecomposition.

    Method:
    1. Compute A = V @ Λ @ V^(-1)
    2. A^k = V @ Λ^k @ V^(-1)
    3. Λ^k is diagonal, easy to compute

    Args:
        A: Square numpy array (diagonalizable)
        k: Integer power

    Returns:
        A^k as numpy array

    Example:
        >>> A = np.array([[2, 0], [0, 3]])
        >>> matrix_power_eigen(A, 3)
        array([[8, 0], [0, 27]])
    """
    # TODO: Implement matrix power using eigendecomposition
    # Hint: eigenvalues, eigenvectors = np.linalg.eig(A)
    # Hint: Create diagonal matrix: Lambda = np.diag(eigenvalues)
    # Hint: Lambda^k = np.diag(eigenvalues ** k)
    # Hint: A^k = V @ Lambda^k @ V^(-1)
    pass


# ============================================================================
# Exercise 6: Principal Component Analysis (PCA)
# ============================================================================

def pca_transform(X, n_components):
    """
    Perform PCA dimensionality reduction using eigendecomposition.

    Steps:
    1. Center the data (subtract mean)
    2. Compute covariance matrix: C = (1/n) X^T @ X
    3. Compute eigendecomposition of C
    4. Sort eigenvalues/eigenvectors by eigenvalue (descending)
    5. Keep top n_components eigenvectors
    6. Project data: X_reduced = X @ V_k

    Args:
        X: Data matrix (n_samples, n_features)
        n_components: Number of components to keep

    Returns:
        Tuple (X_reduced, explained_variance_ratio)
        - X_reduced: Transformed data (n_samples, n_components)
        - explained_variance_ratio: Proportion of variance explained by each component

    Example:
        >>> X = np.random.randn(100, 10)
        >>> X_reduced, variance_ratio = pca_transform(X, 3)
        >>> X_reduced.shape
        (100, 3)
    """
    # TODO: Implement PCA using eigendecomposition
    # Hint: Center data: X = X - X.mean(axis=0)
    # Hint: Covariance: C = (X.T @ X) / (X.shape[0] - 1)
    # Hint: eigenvalues, eigenvectors = np.linalg.eigh(C)
    # Hint: Sort by eigenvalue descending: idx = np.argsort(eigenvalues)[::-1]
    # Hint: Variance ratio: eigenvalues[idx[:n_components]] / eigenvalues.sum()
    pass


# ============================================================================
# Exercise 7: Compute Condition Number
# ============================================================================

def condition_number(A):
    """
    Compute the condition number of a matrix.

    Condition number = λ_max / λ_min (ratio of largest to smallest singular value)

    For symmetric positive definite matrices, this equals the ratio of
    largest to smallest eigenvalue.

    Args:
        A: Square numpy array

    Returns:
        Condition number (float)

    Example:
        >>> A = np.array([[10, 0], [0, 1]])  # Stretched transformation
        >>> condition_number(A)
        10.0
    """
    # TODO: Implement condition number computation
    # Hint: Use singular values: s = np.linalg.svd(A, compute_uv=False)
    # Hint: Condition number = s.max() / s.min()
    pass


# ============================================================================
# Exercise 8: Reconstruct Matrix from Eigendecomposition
# ============================================================================

def reconstruct_from_eigen(eigenvalues, eigenvectors):
    """
    Reconstruct original matrix from eigendecomposition.

    Given eigenvalues Λ and eigenvectors V, compute: A = V @ Λ @ V^(-1)

    Args:
        eigenvalues: Array of eigenvalues
        eigenvectors: Matrix whose columns are eigenvectors

    Returns:
        Reconstructed matrix A

    Example:
        >>> A = np.array([[4, 1], [2, 3]])
        >>> eigenvalues, eigenvectors = np.linalg.eig(A)
        >>> A_reconstructed = reconstruct_from_eigen(eigenvalues, eigenvectors)
        >>> np.allclose(A, A_reconstructed)
        True
    """
    # TODO: Implement matrix reconstruction
    # Hint: Lambda = np.diag(eigenvalues)
    # Hint: A = eigenvectors @ Lambda @ np.linalg.inv(eigenvectors)
    pass


# ============================================================================
# Unit Tests
# ============================================================================

class TestLinearAlgebraEigendecomposition(unittest.TestCase):

    def test_compute_eigenvalues_2x2(self):
        """Test eigenvalue computation for 2x2 matrices"""
        A = np.array([[4, 1], [2, 3]])
        eigs = compute_eigenvalues_2x2(A)
        expected = np.sort(np.linalg.eigvals(A))
        computed = np.sort(np.array(eigs))
        np.testing.assert_array_almost_equal(computed, expected, decimal=5)

        # Test with diagonal matrix
        A = np.array([[3, 0], [0, 5]])
        eigs = compute_eigenvalues_2x2(A)
        self.assertIn(3.0, eigs)
        self.assertIn(5.0, eigs)

    def test_power_iteration(self):
        """Test power iteration finds dominant eigenvalue"""
        A = np.array([[4, 1], [2, 3]], dtype=float)
        eigenvalue, eigenvector = power_iteration(A)

        # Check eigenvalue (should be close to 5.0, the largest)
        expected_eigenvalue = np.max(np.linalg.eigvals(A))
        self.assertAlmostEqual(eigenvalue, expected_eigenvalue, places=3)

        # Check eigenvector equation: A @ v ≈ λ @ v
        Av = A @ eigenvector
        lambda_v = eigenvalue * eigenvector
        np.testing.assert_array_almost_equal(Av, lambda_v, decimal=3)

    def test_is_symmetric(self):
        """Test symmetry check"""
        # Symmetric matrix
        A = np.array([[1, 2], [2, 3]])
        self.assertTrue(is_symmetric(A))

        # Non-symmetric matrix
        B = np.array([[1, 2], [3, 4]])
        self.assertFalse(is_symmetric(B))

        # Identity is symmetric
        I = np.eye(3)
        self.assertTrue(is_symmetric(I))

    def test_is_positive_definite(self):
        """Test positive definite check"""
        # Positive definite
        A = np.array([[2, 0], [0, 3]])
        self.assertTrue(is_positive_definite(A))

        # Not positive definite (has negative eigenvalue)
        B = np.array([[1, 0], [0, -1]])
        self.assertFalse(is_positive_definite(B))

        # Positive semi-definite (has zero eigenvalue)
        C = np.array([[1, 0], [0, 0]])
        self.assertFalse(is_positive_definite(C))

    def test_matrix_power_eigen(self):
        """Test matrix power using eigendecomposition"""
        A = np.array([[2, 0], [0, 3]])
        A_cubed = matrix_power_eigen(A, 3)
        expected = np.array([[8, 0], [0, 27]])
        np.testing.assert_array_almost_equal(A_cubed, expected, decimal=5)

        # Test with non-diagonal matrix
        A = np.array([[4, 1], [2, 3]], dtype=float)
        A_squared = matrix_power_eigen(A, 2)
        expected = A @ A
        np.testing.assert_array_almost_equal(A_squared, expected, decimal=5)

    def test_pca_transform(self):
        """Test PCA transformation"""
        # Create data with known structure
        np.random.seed(42)
        X = np.random.randn(100, 5)

        # Transform to 2 components
        X_reduced, variance_ratio = pca_transform(X, 2)

        # Check dimensions
        self.assertEqual(X_reduced.shape, (100, 2))
        self.assertEqual(len(variance_ratio), 2)

        # Check variance ratios sum to less than 1
        self.assertLess(variance_ratio.sum(), 1.0)
        self.assertGreater(variance_ratio.sum(), 0.0)

        # Variance ratios should be in descending order
        self.assertGreaterEqual(variance_ratio[0], variance_ratio[1])

    def test_condition_number(self):
        """Test condition number computation"""
        # Identity has condition number 1
        I = np.eye(3)
        self.assertAlmostEqual(condition_number(I), 1.0, places=5)

        # Diagonal matrix with known condition number
        A = np.array([[10, 0], [0, 1]], dtype=float)
        self.assertAlmostEqual(condition_number(A), 10.0, places=5)

    def test_reconstruct_from_eigen(self):
        """Test matrix reconstruction from eigendecomposition"""
        A = np.array([[4, 1], [2, 3]], dtype=float)
        eigenvalues, eigenvectors = np.linalg.eig(A)
        A_reconstructed = reconstruct_from_eigen(eigenvalues, eigenvectors)
        np.testing.assert_array_almost_equal(A, A_reconstructed, decimal=5)


if __name__ == '__main__':
    print("Running tests for Topic 02: Linear Algebra & Eigendecomposition")
    print("=" * 60)
    unittest.main(verbosity=2)

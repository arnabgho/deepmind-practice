"""
Topic 02: Linear Algebra & Eigendecomposition - Solutions

Complete solutions with explanations.
"""

import numpy as np


# ============================================================================
# Solution 1: Compute Eigenvalues for 2x2 Matrix
# ============================================================================

def compute_eigenvalues_2x2(A):
    """
    Compute eigenvalues using characteristic equation for 2x2 matrix.

    For 2x2 matrix [[a,b],[c,d]]:
    - Characteristic equation: λ² - (a+d)λ + (ad-bc) = 0
    - Using quadratic formula: λ = ((a+d) ± sqrt((a+d)² - 4(ad-bc))) / 2
    - Simplified: λ = (trace ± sqrt(trace² - 4*det)) / 2

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    trace = np.trace(A)  # a + d
    det = np.linalg.det(A)  # ad - bc

    # Discriminant: might be negative (complex eigenvalues)
    discriminant = trace**2 - 4*det

    # Use complex square root to handle negative discriminant
    sqrt_disc = np.sqrt(discriminant + 0j)  # +0j ensures complex type

    lambda1 = (trace + sqrt_disc) / 2
    lambda2 = (trace - sqrt_disc) / 2

    # Convert back to real if imaginary part is negligible
    if np.abs(np.imag(lambda1)) < 1e-10:
        lambda1 = np.real(lambda1)
    if np.abs(np.imag(lambda2)) < 1e-10:
        lambda2 = np.real(lambda2)

    return (lambda1, lambda2)


# ============================================================================
# Solution 2: Power Iteration
# ============================================================================

def power_iteration(A, num_iterations=100, tolerance=1e-6):
    """
    Power iteration to find dominant eigenvalue and eigenvector.

    Intuition:
    - Repeatedly multiply by A amplifies component in direction of largest eigenvalue
    - After normalization, converges to eigenvector with largest |λ|

    Convergence rate depends on ratio |λ₁/λ₂| (faster if ratio is large)

    Time Complexity: O(n² * num_iterations) for n×n matrix
    Space Complexity: O(n)
    """
    n = A.shape[0]

    # Start with random vector
    v = np.random.randn(n)
    v = v / np.linalg.norm(v)  # Normalize

    eigenvalue = 0
    for i in range(num_iterations):
        # Apply transformation
        v_new = A @ v

        # Normalize
        v_new = v_new / np.linalg.norm(v_new)

        # Compute eigenvalue (Rayleigh quotient)
        eigenvalue_new = v_new.T @ A @ v_new

        # Check convergence
        if np.abs(eigenvalue_new - eigenvalue) < tolerance:
            break

        v = v_new
        eigenvalue = eigenvalue_new

    return eigenvalue, v


# Alternative: Rayleigh quotient iteration (faster convergence)
def rayleigh_quotient_iteration(A, num_iterations=20):
    """
    Rayleigh quotient iteration - cubic convergence!

    Faster than power iteration, but requires matrix inverse at each step.
    """
    n = A.shape[0]
    v = np.random.randn(n)
    v = v / np.linalg.norm(v)

    for _ in range(num_iterations):
        # Rayleigh quotient
        eigenvalue = v.T @ A @ v

        # Solve (A - λI)v_new = v for v_new
        try:
            v_new = np.linalg.solve(A - eigenvalue * np.eye(n), v)
            v = v_new / np.linalg.norm(v_new)
        except np.linalg.LinAlgError:
            break  # Singular matrix, already converged

    eigenvalue = v.T @ A @ v
    return eigenvalue, v


# ============================================================================
# Solution 3: Check if Matrix is Symmetric
# ============================================================================

def is_symmetric(A, tolerance=1e-9):
    """
    Check if matrix equals its transpose.

    Using np.allclose() handles floating-point errors.

    Time Complexity: O(n²)
    Space Complexity: O(n²) for transpose
    """
    if A.shape[0] != A.shape[1]:
        return False  # Must be square

    return np.allclose(A, A.T, atol=tolerance)


# ============================================================================
# Solution 4: Check if Matrix is Positive Definite
# ============================================================================

def is_positive_definite(A):
    """
    Check positive definiteness by verifying all eigenvalues > 0.

    For symmetric matrices, use eigvalsh (faster, guaranteed real eigenvalues).

    Alternative methods:
    1. Try Cholesky decomposition (fails if not positive definite)
    2. Check all principal minors > 0
    3. Check x^T A x > 0 for random vectors x

    Time Complexity: O(n³) for eigendecomposition
    Space Complexity: O(n²)
    """
    # First check if symmetric (requirement for positive definite)
    if not is_symmetric(A):
        return False

    try:
        # Compute eigenvalues (use eigvalsh for symmetric matrices)
        eigenvalues = np.linalg.eigvalsh(A)

        # Check if all eigenvalues are positive
        return np.all(eigenvalues > 0)
    except np.linalg.LinAlgError:
        return False


# Alternative: Cholesky decomposition method (faster!)
def is_positive_definite_cholesky(A):
    """
    Faster method using Cholesky decomposition.

    Cholesky decomposition A = L @ L.T only exists for positive definite matrices.
    """
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False


# ============================================================================
# Solution 5: Matrix Power Using Eigendecomposition
# ============================================================================

def matrix_power_eigen(A, k):
    """
    Compute A^k using eigendecomposition: A = V Λ V^(-1)

    Then A^k = V Λ^k V^(-1)

    Λ^k is diagonal, very easy to compute: just raise each eigenvalue to power k

    Why this is faster:
    - Direct: O(n³) per multiplication, need k multiplications = O(k * n³)
    - Eigendecomposition: O(n³) for decomposition, O(n) for Λ^k = O(n³) total

    For large k, this is much faster!

    Time Complexity: O(n³)
    Space Complexity: O(n²)
    """
    # Eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Λ^k: raise each eigenvalue to power k
    Lambda_k = np.diag(eigenvalues ** k)

    # Reconstruct: A^k = V @ Λ^k @ V^(-1)
    V_inv = np.linalg.inv(eigenvectors)
    A_k = eigenvectors @ Lambda_k @ V_inv

    # Clean up small imaginary parts (from numerical errors)
    if np.allclose(np.imag(A_k), 0):
        A_k = np.real(A_k)

    return A_k


# ============================================================================
# Solution 6: Principal Component Analysis (PCA)
# ============================================================================

def pca_transform(X, n_components):
    """
    PCA using eigendecomposition of covariance matrix.

    Steps:
    1. Center data (mean = 0)
    2. Compute covariance: C = X^T X / (n-1)
    3. Eigendecomposition: C = V Λ V^T
    4. Sort by eigenvalue (descending)
    5. Keep top k eigenvectors
    6. Project: X_reduced = X @ V_k

    Why eigenvectors of covariance matrix?
    - Covariance matrix C measures variance/correlation structure
    - Eigenvectors of C point in directions of maximum variance
    - Eigenvalues tell us how much variance in each direction

    Time Complexity: O(min(n², d²) + d³) where n=samples, d=features
    Space Complexity: O(d²)
    """
    n_samples = X.shape[0]

    # Step 1: Center the data
    X_centered = X - X.mean(axis=0)

    # Step 2: Compute covariance matrix
    # C = (1/(n-1)) * X^T @ X
    C = (X_centered.T @ X_centered) / (n_samples - 1)

    # Step 3: Eigendecomposition (use eigh for symmetric matrices)
    eigenvalues, eigenvectors = np.linalg.eigh(C)

    # Step 4: Sort by eigenvalue (descending)
    # eigh returns ascending order, so reverse
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Step 5: Keep top n_components eigenvectors
    V_k = eigenvectors[:, :n_components]
    eigenvalues_k = eigenvalues[:n_components]

    # Step 6: Project data onto principal components
    X_reduced = X_centered @ V_k

    # Compute explained variance ratio
    explained_variance_ratio = eigenvalues_k / eigenvalues.sum()

    return X_reduced, explained_variance_ratio


# Alternative: SVD-based PCA (more numerically stable)
def pca_transform_svd(X, n_components):
    """
    PCA using SVD (more stable for ill-conditioned data).

    X = U Σ V^T
    - Right singular vectors V are eigenvectors of X^T X (covariance matrix)
    - Singular values σ² / (n-1) are eigenvalues of covariance matrix
    """
    n_samples = X.shape[0]

    # Center data
    X_centered = X - X.mean(axis=0)

    # SVD
    U, s, Vt = np.linalg.svd(X_centered, full_matrices=False)

    # V (right singular vectors) are principal components
    V = Vt.T
    V_k = V[:, :n_components]

    # Project
    X_reduced = X_centered @ V_k

    # Explained variance
    eigenvalues = (s ** 2) / (n_samples - 1)
    explained_variance_ratio = eigenvalues[:n_components] / eigenvalues.sum()

    return X_reduced, explained_variance_ratio


# ============================================================================
# Solution 7: Compute Condition Number
# ============================================================================

def condition_number(A):
    """
    Condition number = ratio of largest to smallest singular value.

    κ(A) = σ_max / σ_min

    For square matrices: κ(A) = ||A|| * ||A^(-1)||

    Interpretation:
    - κ ≈ 1: Well-conditioned (numerical operations stable)
    - κ >> 1: Ill-conditioned (small changes in input → large changes in output)

    Time Complexity: O(min(m²n, mn²)) for m×n matrix
    Space Complexity: O(min(m,n))
    """
    # Compute singular values only (faster than full SVD)
    singular_values = np.linalg.svd(A, compute_uv=False)

    # Condition number
    kappa = singular_values.max() / singular_values.min()

    return kappa


# ============================================================================
# Solution 8: Reconstruct Matrix from Eigendecomposition
# ============================================================================

def reconstruct_from_eigen(eigenvalues, eigenvectors):
    """
    Reconstruct A from eigendecomposition: A = V Λ V^(-1)

    Verification that eigendecomposition is correct!

    Time Complexity: O(n³)
    Space Complexity: O(n²)
    """
    # Create diagonal matrix of eigenvalues
    Lambda = np.diag(eigenvalues)

    # Reconstruct: A = V @ Λ @ V^(-1)
    V_inv = np.linalg.inv(eigenvectors)
    A = eigenvectors @ Lambda @ V_inv

    # Clean up small imaginary parts
    if np.allclose(np.imag(A), 0):
        A = np.real(A)

    return A


# For symmetric matrices: simpler reconstruction
def reconstruct_from_eigen_symmetric(eigenvalues, eigenvectors):
    """
    For symmetric matrices: A = Q Λ Q^T (Q is orthogonal, Q^(-1) = Q^T)
    """
    Lambda = np.diag(eigenvalues)
    A = eigenvectors @ Lambda @ eigenvectors.T
    return A


# ============================================================================
# Additional Utility Functions
# ============================================================================

def visualize_eigenvectors_2d(A):
    """
    Visualize eigenvectors of 2x2 matrix (for educational purposes).

    Returns information about transformation.
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("Matrix A:")
    print(A)
    print("\nEigenvalues:", eigenvalues)
    print("\nEigenvectors (as columns):")
    print(eigenvectors)

    for i, (val, vec) in enumerate(zip(eigenvalues, eigenvectors.T)):
        print(f"\nEigenvector {i+1}: {vec}")
        print(f"Eigenvalue {i+1}: {val}")
        print(f"Verification: A @ v = λ @ v")
        Av = A @ vec
        lambda_v = val * vec
        print(f"  A @ v = {Av}")
        print(f"  λ @ v = {lambda_v}")
        print(f"  Match: {np.allclose(Av, lambda_v)}")


def analyze_matrix_properties(A):
    """
    Comprehensive analysis of a matrix.
    """
    print("=" * 60)
    print("MATRIX ANALYSIS")
    print("=" * 60)

    print("\nMatrix:")
    print(A)

    print(f"\nShape: {A.shape}")
    print(f"Determinant: {np.linalg.det(A):.6f}")
    print(f"Trace: {np.trace(A):.6f}")
    print(f"Rank: {np.linalg.matrix_rank(A)}")

    print(f"\nSymmetric: {is_symmetric(A)}")
    if is_symmetric(A):
        print(f"Positive Definite: {is_positive_definite(A)}")

    eigenvalues = np.linalg.eigvals(A)
    print(f"\nEigenvalues: {eigenvalues}")
    print(f"Condition Number: {condition_number(A):.2f}")

    singular_values = np.linalg.svd(A, compute_uv=False)
    print(f"\nSingular Values: {singular_values}")


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == '__main__':
    print("Solution Examples for Topic 02: Linear Algebra & Eigendecomposition")
    print("=" * 60)

    # Example 1: Compute eigenvalues of 2x2 matrix
    print("\n1. Computing Eigenvalues (2x2 Matrix)")
    print("-" * 40)
    A = np.array([[4, 1], [2, 3]])
    eigs = compute_eigenvalues_2x2(A)
    print(f"Matrix:\n{A}")
    print(f"Eigenvalues: {eigs}")
    print(f"Verification with NumPy: {np.linalg.eigvals(A)}")

    # Example 2: Power iteration
    print("\n2. Power Iteration")
    print("-" * 40)
    A = np.array([[4, 1], [2, 3]], dtype=float)
    eigenvalue, eigenvector = power_iteration(A, num_iterations=50)
    print(f"Matrix:\n{A}")
    print(f"Dominant eigenvalue: {eigenvalue:.6f}")
    print(f"Dominant eigenvector: {eigenvector}")
    print(f"Verification: A @ v = {A @ eigenvector}")
    print(f"              λ @ v = {eigenvalue * eigenvector}")

    # Example 3: Positive definite check
    print("\n3. Positive Definite Check")
    print("-" * 40)
    A_pos = np.array([[2, 0], [0, 3]])
    A_neg = np.array([[1, 0], [0, -1]])
    print(f"Matrix A:\n{A_pos}")
    print(f"Is positive definite: {is_positive_definite(A_pos)}")
    print(f"\nMatrix B:\n{A_neg}")
    print(f"Is positive definite: {is_positive_definite(A_neg)}")

    # Example 4: Matrix power
    print("\n4. Matrix Power using Eigendecomposition")
    print("-" * 40)
    A = np.array([[2, 0], [0, 3]], dtype=float)
    k = 5
    A_k = matrix_power_eigen(A, k)
    print(f"Matrix A:\n{A}")
    print(f"A^{k} using eigendecomposition:\n{A_k}")
    print(f"Verification (direct computation):\n{np.linalg.matrix_power(A, k)}")

    # Example 5: PCA
    print("\n5. Principal Component Analysis")
    print("-" * 40)
    np.random.seed(42)
    # Create correlated data
    mean = [0, 0, 0]
    cov = [[3, 1, 0.5],
           [1, 2, 0.3],
           [0.5, 0.3, 1]]
    X = np.random.multivariate_normal(mean, cov, size=100)
    print(f"Original data shape: {X.shape}")

    X_reduced, variance_ratio = pca_transform(X, n_components=2)
    print(f"Reduced data shape: {X_reduced.shape}")
    print(f"Explained variance ratio: {variance_ratio}")
    print(f"Total variance explained: {variance_ratio.sum():.2%}")

    # Example 6: Condition number
    print("\n6. Condition Number Analysis")
    print("-" * 40)
    A_well = np.eye(3)
    A_ill = np.array([[1000, 0], [0, 1]], dtype=float)

    print(f"Well-conditioned matrix (Identity):")
    print(f"  Condition number: {condition_number(A_well):.2f}")

    print(f"\nIll-conditioned matrix:")
    print(A_ill)
    print(f"  Condition number: {condition_number(A_ill):.2f}")

    # Example 7: Eigendecomposition visualization
    print("\n7. Eigendecomposition Visualization")
    print("-" * 40)
    A = np.array([[3, 1], [0, 2]], dtype=float)
    visualize_eigenvectors_2d(A)

    # Example 8: Complete matrix analysis
    print("\n8. Complete Matrix Analysis")
    A = np.array([[2, 1], [1, 2]], dtype=float)
    analyze_matrix_properties(A)

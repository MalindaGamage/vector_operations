"""
Vector and Matrix Operations with Visualization

This script demonstrates various vector and matrix operations using NumPy,
and visualizes 2D vectors using Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def perform_vector_operations():
    """Demonstrate basic vector operations."""
    # Define vectors
    v1 = np.array([2, 1])
    v2 = np.array([1, 3])

    print("\n=== Vector Operations ===")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    # Vector addition
    v_add = v1 + v2
    print(f"\nVector Addition (v1 + v2): {v_add}")

    # Vector subtraction
    v_sub = v1 - v2
    print(f"Vector Subtraction (v1 - v2): {v_sub}")

    # Scalar multiplication
    scalar = 3
    v_scaled = scalar * v1
    print(f"\nScalar Multiplication ({scalar} * v1): {v_scaled}")

    # Dot product
    dot_product = np.dot(v1, v2)
    print(f"\nDot Product (v1 · v2): {dot_product}")

    # Magnitude
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)
    print(f"\nMagnitude of v1: {magnitude_v1:.2f}")
    print(f"Magnitude of v2: {magnitude_v2:.2f}")


def perform_matrix_operations():
    """Demonstrate basic matrix operations."""
    # Define matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    print("\n=== Matrix Operations ===")
    print(f"Matrix A:\n{A}")
    print(f"\nMatrix B:\n{B}")

    # Matrix addition
    C = A + B
    print("\nMatrix Addition (A + B):\n", C)

    # Matrix subtraction
    D = A - B
    print("\nMatrix Subtraction (A - B):\n", D)

    # Matrix multiplication
    E = np.dot(A, B)
    print("\nMatrix Multiplication (A × B):\n", E)

    # Scalar multiplication
    k = 2
    F = k * A
    print(f"\nScalar Multiplication (k={k} × A):\n", F)

    # Transpose
    A_T = A.T
    print("\nTranspose of A:\n", A_T)

    # Determinant
    det_A = np.linalg.det(A)
    print(f"\nDeterminant of A: {det_A:.2f}")


def plot_vectors():
    """Visualize vectors using Matplotlib."""
    # Define vectors to plot
    v1 = np.array([2, 1])
    v2 = np.array([1, 3])

    # Create plot
    plt.figure(figsize=(8, 6))

    # Plot vectors
    plt.quiver(0, 0, v1[0], v1[1],
               angles='xy', scale_units='xy', scale=1,
               color='r', width=0.005, label='v1 = [2, 1]')
    plt.quiver(0, 0, v2[0], v2[1],
               angles='xy', scale_units='xy', scale=1,
               color='b', width=0.005, label='v2 = [1, 3]')

    # Plot settings
    plt.xlim(-1, 5)
    plt.ylim(-1, 5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('2D Vector Visualization', pad=20)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    # Save plot
    plot_path = 'images/vector_plot.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nVector plot saved as {plot_path}")


if __name__ == "__main__":
    print("=== Vector and Matrix Operations Demo ===")
    perform_vector_operations()
    perform_matrix_operations()
    plot_vectors()
    print("\nAll operations completed successfully!")
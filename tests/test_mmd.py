import pytest
from qcbm.mmd import mmd_loss
import numpy as np


def test_non_negative():
    """Test that MMD is non-negative for random distributions."""
    np.random.seed(42)
    X = np.random.randn(100, 2)
    Y = np.random.randn(100, 2)
    sigma = 1.0
    mmd = mmd_loss(sigma, X, Y)
    assert mmd >= 0.0, "MMD should be non-negative"


def test_mmd_zero_for_identical_distributions():
    """Test that MMD is approximately zero for identical distributions."""
    np.random.seed(42)
    X = np.random.randn(100, 2)
    sigma = 1.0
    mmd = mmd_loss(sigma, X, X)
    assert np.isclose(
        mmd, 0.0, atol=1e-5), "MMD should be close to zero for identical distributions"


def test_mmd_increases_for_different_distributions():
    """Test that MMD is larger when distributions are different."""
    np.random.seed(42)
    X = np.random.randn(100, 2)
    Y = np.random.randn(100, 2) + 5  # Shifted by 5 units
    sigma = 1.0
    mmd = mmd_loss(sigma, X, Y)
    assert mmd > 0.0, "MMD should be greater than zero for different distributions"


def test_mmd_symmetric():
    """Test that MMD is symmetric, i.e., MMD(X, Y) == MMD(Y, X)."""
    np.random.seed(42)
    X = np.random.randn(100, 2)
    Y = np.random.randn(100, 2)
    sigma = 1.0
    mmd_xy = mmd_loss(sigma, X, Y)
    mmd_yx = mmd_loss(sigma, Y, X)
    assert np.isclose(mmd_xy, mmd_yx, atol=1e-5), "MMD should be symmetric"


def test_mmd_empty_distributions():
    """Test that MMD handles empty input gracefully."""
    X = np.array([]).reshape(0, 2)  # Empty array
    Y = np.array([]).reshape(0, 2)  # Empty array
    sigma = 1.0
    mmd = mmd_loss(sigma, X, Y)
    assert mmd == 0.0, "MMD should be zero for empty distributions"


def test_mmd_small_distributions():
    """Test MMD for very small distributions."""
    X = np.array([[0.0, 0.0]])  # One-point distribution
    Y = np.array([[1.0, 1.0]])  # One-point distribution
    sigma = 1.0
    mmd = mmd_loss(sigma, X, Y)
    assert mmd > 0.0, "MMD should be greater than zero for small distributions"
